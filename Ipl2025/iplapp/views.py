from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Player
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
 # Import your model


# Create your views here.
@login_required(login_url='login')
def home_view(request):
  return render(request,"iplapp/home.html")

@login_required(login_url='login')
def create_view(request):
  player=None
  if(request.method=="POST"):
    print(request.POST)
    j=request.POST.get('jn')
    pn=request.POST.get('pn')
    r=request.POST.get('rn')
    wkt=request.POST.get('wkt')
    t=request.POST.get('tn')
    player=Player(jno=j,pname=pn,runs=r,wickets=wkt,tname=t)
    player.save()
    return redirect("/display/")
  return render(request,"iplapp/create.html")          

@login_required(login_url='login')
def display_view(request):
  db=Player.objects.all()
  context={"db":db}
  return render(request,'iplapp/display.html',context)

@login_required(login_url='login')
def update_view(request,n):
  player=Player.objects.get(jno=n)
  context={"p",player}

  if(request.method=="POST"):
    u_j=request.POST.get('jn')
    u_pn=request.POST.get('pn')
    u_r=request.POST.get('rn')
    u_wkt=request.POST.get('wkt')
    u_t=request.POST.get('tn')

    # player.jno=u_j
    player.pname=u_pn
    player.runs=u_r
    player.wickets=u_wkt
    player.tname=u_t
    player.save()
    return redirect("/display/")

  print("In update view",n)
  db=Player.objects.get(jno=n)
  context={"p":db}
  return render(request,"iplapp/update.html",context)

@login_required(login_url='login')
def delete_view(request,n):

  print("In delete view",n)
  player=Player.objects.get(jno=n)
  player.delete()
  return redirect("/display/")

def signup_view(request):
  if(request.method=='POST'):
    # print(request.POST)
    name=request.POST.get("name")
    email=request.POST.get("email")
    password=request.POST.get("password")
    repassword=request.POST.get("repassword")

    if password != repassword:
      messages.error(request,"passwords do not match!")
      return redirect('/signup/')
    print(name,email,password)

    if(User.objects.filter(username=name).exists()):
            messages.error(request, "Username already taken!")
            return render(request,'iplapp/signup.html/',{'err':"user already exists"})
    else:
      user=User.objects.create_user(username=name,email=email,password=password)
      return redirect('/login/')
  return render(request,"iplapp/signup.html")

def login_view(request):
  if(request.method=='POST'):
    name=request.POST.get('name')
    password=request.POST.get('password')

    user=authenticate(request,username=name,password=password)

    if User is None:
      return render(request,"iplapp/login.html",{'err':'invalid credentials'})
    else:
      login(request,user)
      return redirect('/create/')
  return render(request,"iplapp/login.html")