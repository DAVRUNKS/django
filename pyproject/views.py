from django.shortcuts import render

def sign_up(request):
	context={}
	return render(request, 'users/signup.html', context)

def login_user(request):
         context={}
         return render(request, 'users/login.html',context)

def login_user(request):
        pass