import subprocess
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
import mysql.connector
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def homepage(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        paswd1=request.POST.get('passwd1')
        paswd2=request.POST.get('passwd2')#databse

        if paswd1!=paswd2:#exception 2
            messages.success(request,'passwords does not match')
            return render(request,'signup.html')
        
        if User.objects.filter(username=uname).first():#exception 1
            messages.success(request,'username aleday exsists please use another username')
            return render(request,'signup.html')
        else:
            try:
                mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="root",
                database="lquick"
                )
                cursor=mydb.cursor()
                print("success")
            
                query ="insert into logiInfo(name,email,password)values(%s,%s,%s)"
                data =(uname,email,paswd1)
                cursor.execute(query,data)
                mydb.commit()
                cursor.close()

                mydb.close()

            except :
                print("no")
            
            # if User.objects.filter(username=uname).first():#exception 1
            #     messages.MessageFailure(request,'username aleday exsists please use another username')
            #     return render(request,'signup.html')

            my_user=User.objects.create_user(uname,email,paswd1)
            my_user.save()
            
            return redirect('logn')


    return render(request,'signup.html')

def loginp(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        paswd1=request.POST.get('passwd1')
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="root",
                database="lquick"
                )
            cursor=mydb.cursor()
            print("success")
        except mysql.connector.errors as e:
            print("no",e)
        # message = "hello ayush"
        # send_mail('contact form',message,'settings.EMAIL_HOST_USER',['ayush.solanki@somaiya.edu'],fail_silently=False)
    #     userid =str(User.objects.get(username=uname))
    #     pas=User.objects.get(password = paswd1)
    #     query = 'select from logiInfo where name=%s && password=%s'
    #     data=(userid,pas)
    #     cursor.execute(query,data)
    #     mydb.commit()
    #     cursor.close()
    #     mydb.close()
    #     if query is not None:
    #         login(request,userid)
    #         return redirect('home')
    #     else:
    #         return HttpResponse("username or password not found")
        
        
    # return render(request,'login.html')






        user =authenticate(request,username=uname,password=paswd1)
        if user is not None:
            login(request,user)
            return redirect('lq2')
        else:
            messages.success(request,'username or passowrd is incorrect')
            return render(request,'login.html')
        
    return render(request,'login.html')

def lgout(request):
    logout(request)
    return redirect('logn')

def forgotp(request):
    if request.method=='POST':
        email=request.POST.get('email')
        
        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)
            # print("email yes")
            send_mail('reset your password: ',
                    f"hey user : {user} to reset your paswords click on the the given link \n http://127.0.0.1:8000/reset_password/{user}/",
                    'EMAIL_HOST_USER',
                    [email],
                    fail_silently=True)
            
            messages.success(request,'email has been sent to your email')
            return render(request,'forgot_password.html')
            
        else:
            messages.error(request,'email does not exsist')
            return render(request,'forgot_password.html')
    return render(request,'forgot_password.html')

def resetpas(request,user):
    userid=User.objects.get(username=user)
    if request.method=='POST':
        paswd1=request.POST.get('passwd1')
        paswd2=request.POST.get('passwd2')
        if paswd1==paswd2:
            userid.set_password(paswd1)
            userid.save()
        else:
            messages.success(request,' password is incorrect')
            return render(request,'reset_password.html')
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="root",
                database="lquick"
                )
            
            cursor=mydb.cursor()
            query ="update logiInfo set password = %s where name = %s"
            data = (paswd1,str(userid))
            cursor.execute(query,data)
            mydb.commit()
            cursor.close()

            mydb.close()
            

            print("success")
            return redirect('logn')

        except mysql.connector.Error as e:
            print("no",e)

        
    return render(request,'reset_password.html')

def lq(request):
    return render(request,'lq.html')

def about(request):
    return render(request,'about.html')

def newexp(request):
    return render(request,'newexp.html')

def lq2(request):
    return render(request,'lq2.html')

def sum(request):
    subprocess.Popen(["streamlit","run","inference.py"])
    JsonResponse("running")
    return render(request,'inference.py')

def summary(request):
    return render(request,'streamlit_summary.html')

def quiz(request):
    subprocess.Popen(["streamlit","run","quizapp.py"])
    JsonResponse("running")
    return render(request,'quizapp.py')

def flow(request):
    return render(request,'s_flowchart.html')

def flashc(request):
    subprocess.Popen(["streamlit","run","try.py"])
    JsonResponse("running")
    return render(request,'try.py')




def mcq(request):
    return render(request,'s_mcq.html')

def chartt(request):
    subprocess.Popen(["streamlit","run","chart.py"])
    JsonResponse("running")
    return render(request,'chart.py')

def flash(request):
    return render(request,'s_flash.html')
