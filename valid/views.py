from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

# Create your views here.
# valid . views

name = "abin"
passw = 'abin123'


@never_cache
def userform(request):
    if request.COOKIES.get("username") and request.COOKIES.get("password"):
        Cname = request.COOKIES.get('username')
        Cpassw = request.COOKIES.get('password')
        Sname = request.session['Username']
        Spassw = request.session['Password']
        if Cname == Sname and Cpassw == Spassw:
            return redirect('/home')
    else:
        return render(request, 'user-form.html')


@never_cache
def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        if username == name and password == passw:
            res = redirect('/home')
            res.set_cookie('username', username)
            res.set_cookie('password', password)
            request.session['Username'] = username
            request.session['Password'] = password
            return res
        else:
            return render(request, 'user-form.html', {'err': "invalid credentials"})


@never_cache
def signout(request):
    del request.session
    res = redirect('/sout')
    res.delete_cookie("username")
    res.delete_cookie('password')
    return res


@never_cache
def home(request):
        Cname = request.COOKIES.get('username')
        Cpassw = request.COOKIES.get('password')
        Sname = request.session['Username']
        Spassw = request.session['Password']
        if Cname == Sname and Cpassw == Spassw:
            return render(request, 'home.html', {'name': Cname})
        else:
            return redirect('/sout')


def sout(request):
    return render(request, 'user-form.html')
