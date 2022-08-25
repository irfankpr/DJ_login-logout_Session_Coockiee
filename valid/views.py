from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

# Create your views here.
# valid . views

name = "abin"
passw = 'abin123'



def index(request):
    if request.COOKIES.get("username") and request.COOKIES.get("password"):
        Cname = request.COOKIES.get('username')
        Cpassw = request.COOKIES.get('password')
        Sname = request.session['Username']
        Spassw = request.session['Password']
        if Cname == Sname and Cpassw == Spassw:
            return redirect('/home')
    else:
        return render(request, 'user-form.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        if username == name and password == passw:
            res = redirect('/')
            res.set_cookie('username', username)
            res.set_cookie('password', password)
            request.session['Username'] = username
            request.session['Password'] = password
            return res
        else:
            return render(request, 'user-form.html', {'err': "invalid credentials"})


def signout(request):
    del request.session
    res = redirect('/')
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
            return redirect('/')


