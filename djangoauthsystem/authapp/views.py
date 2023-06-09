from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request,'home.html')

def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        
        #create user
        myuser=User.objects.create_user(username,email,password)   
        myuser.first_name=fname         
        myuser.last_name=lname  
        myuser.save()
        print("Account created")  
        return redirect('home')
    else:
      return HttpResponse('page not found')

def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpass)
    return HttpResponse('login successfully')

def handlelogout(request):
    logout(request)
    return redirect('home')
    return HttpResponse('logout successfully')


    
    
