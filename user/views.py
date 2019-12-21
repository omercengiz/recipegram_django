from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        #for automatically login after registeration  
        login(request,newUser)
        messages.info(request,"You registered successfully")
        return redirect("index")
                 
    context = {
        "form" : form
    }
    return render(request,"register.html",context)

    #     if form.is_valid():
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")
    #         newUser = User(username = username)
    #         newUser.set_password(password)

    #         newUser.save()
    #         #for automatically login after registeration  
    #         login(request,newUser)
            
    #         return redirect("index")


            
    # else:
    #     form = RegisterForm()

    #     context = {
    #         "form" : form
    #     }
    #     return render(request,"register.html",context)
    


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request,"Username or password is not found")
            return render(request,"login.html",context)
        
        messages.success(request,"You login successfully")
        login(request,user)

        return redirect("index")

    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"You log out successfully")
    return redirect("index")
    
 
  
   
    
     
      
       
        
         
          
