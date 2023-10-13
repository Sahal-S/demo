from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import employe
from django.contrib import sessions
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@csrf_exempt
def home(request):
    return render(request,"home.html")    # after this it will redirect into check with help of action tag in the form


@csrf_exempt
def check(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        role=request.POST['role']
        if role=='company':
    
            #d=user(username=n1,password=n2)
            #d.save()

            #if user and password  matching
            user= authenticate(username=user_name,password=pass_word)  # at this point authentication occurs
            print("user object ===============",user)
            if  user is not None:
                login(request,user)
                print("successfully logined")
                obj2=User.objects.get(username=user_name)
                return redirect('success_c')
                    
            #if not matching
            else:
                messages.info(request,'invalid credentials')
                # redirect into  signup.html
                return redirect('/')
        else:
            if employe.objects.filter(username=user_name,password=pass_word).exists():
                print('employe successfully authenticated')
                request.session['dc']='aaaa'
                global obje
                obje = employe.objects.get(username=user_name)
                # getting employe object  with specified username
                return redirect('success_e')
                
            else:
                messages.info(request,'invalid credentials')
                return redirect('/')


    else:
        return redirect('/')

@never_cache
def success_e(request):
    if 'dc' in request.session:
        return render(request,'welcome_e.html',{'ls':obje})
    else:
        return redirect('home')



@never_cache # this will help to clear the cache there by prevent the browsing back
@csrf_exempt
def success_c(request):
    print('auth status is.................:',request.user.is_authenticated)
    if request.user.is_authenticated:
        c=request.user.username # here we get the username of the user(company user)
        print(c)
        lst2=employe.objects.filter(company=c)
        return render(request,"welcome_c.html",{'ls':lst2,'name':c})
    else:
        return redirect('/')


@csrf_exempt
def signup_as(request):
    return render(request,'signup_as.html')
@csrf_exempt
def signup_e(request):
    if request.method=='POST':
        user_name=request.POST['username']
        print(user_name)
        pass_word=request.POST['password']
        print(pass_word)
        re=request.POST['re']
        print(re)
        e_mail=request.POST['email']
        print(e_mail)
        com_pany=request.POST['company']
        print(com_pany)
        gen_der=request.POST['gender']
        print(gen_der)
        desig_nation=request.POST['designation']
        print(desig_nation)
        dob=request.POST['dob']
        print(dob)
        if employe.objects.filter(username=user_name).exists():
            messages.info(request,'username exites try something else')
            return redirect("signup_e")
        if pass_word==re:
            d=employe(username=user_name,password=pass_word,company=com_pany,gender=gen_der,designation=desig_nation,DOB=dob,email=e_mail)
            d.save()
            print("object saved successfully")
            return redirect('home')
        else:
            messages.info(request,'both password entries doesnt match try again')
            return render(request,"signup_e.html")
        
    else:
        ls=User.objects.all()
        return render(request,"signup_e.html",{'ls':ls})
@csrf_exempt
def signup_c(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        re=request.POST['re']
        e_mail=request.POST['email']
        c = User.objects.filter(username=user_name).exists()

        if c:
            messages.info(request,'username already exists try new')
            return redirect('signup_c')
        else:
            if pass_word==re:
                d=User.objects.create_user(username=user_name,password=pass_word,email=e_mail)
                d.save()
                return redirect('home')
            else:
                messages.info(request,'both password entries doesnt match try again')
                return render(request,"signup_c.html")
    else:
        return render(request,"signup_c.html")
       
def log_out_c(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def log_out_e(request):
    request.session.flush()
    return redirect('home')


@csrf_exempt   
def dropdown(request):
    return render(request,'dropdown.html')

@csrf_exempt
def droptest(request):
    a=request.POST["sl"]
    return HttpResponse(a)
def test(request):
    return HttpResponse('test is working')

def dlt(request):
    dltval=request.POST['dltval']
    print(dltval)
    obj3=employe.objects.get(username=dltval)
    obj3.delete()
    return redirect('success_c')

def add(request):
    user_name=request.POST['usernme']
    pass_word=request.POST['passwrd']
    comp=request.user.username
    gender=request.POST['gender']
    e_mail=request.POST['email']
    desig_nation=request.POST['designation']
    dob=request.POST['dob']
    print(user_name)
    print(pass_word)
    print(comp)
    d=employe(username=user_name,password=pass_word,company=comp,gender=gender,designation=desig_nation,DOB=dob,email=e_mail)
    d.save()
    return redirect('success_c')

def modify(request):
    return HttpResponse('helooo')

def power(request):
    u=employe.objects.get(username="abil")
    u.delete()
    return redirect('home')

def show1(request):
    y=request.POST['show']
    global lsc
    lsc=employe.objects.get(username=y)
    return redirect('show2')

def show2(request):
    print(lsc.interest,"value at show 2")
    return render(request,"show.html",{'ls':lsc})

@csrf_exempt
def set1(request):
    user_name=request.POST['set1']
    print(user_name)
    u=employe.objects.get(username=user_name)
    u.interest=1
    u.save()
    global lsc
    lsc=employe.objects.get(username=user_name)
    print(u.username)
    print(u.interest)
    return redirect('show2')

@csrf_exempt
def set0(request):
    user_name=request.POST['set0']
    u=employe.objects.get(username=user_name)
    u.interest=0
    u.save()
    print(u.username)
    print(u.interest)
    global lsc
    lsc=employe.objects.get(username=user_name)
    print('successfully set as 0')
    return redirect('show2')









    

    
    

    
    
#if user.objects.filter(username=n1):