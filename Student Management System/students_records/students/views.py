from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from.models import student
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
     return render(request,"contact us.html")
def login(request):
    error=""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        admin = auth.authenticate(username=u, password=p)
        try:
            if admin.is_staff:
                auth.login(request, admin)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, "login.html", d)


def admin_home(request):
    return render(request,"admin_dashboard.html")
@login_required(login_url='login')
def add_student(request):
    error=""
    if request.method=="POST":
        n=request.POST['studentName']
        rn=request.POST['rollNumber']
        e=request.POST['email']
        c=request.POST['course']
        dob=request.POST['dob']
        p=request.POST['phone']
        g=request.POST['gender']
        a=request.POST['address']
        t=request.POST['tfee']
        p=request.POST['pfee']
        l=request.POST['lfee']
        img=request.FILES['image']
        try:
            student.objects.create(name=n,rollnumber=rn,email=e,course=c,dob=dob,phone=p,gender=g,address=a,tfee=t,pfee=p,lfee=l,image=img)
            error="no"
        except:
            error="yes"
    d={'error':error}        
    return render(request,"add_student.html",d)
@login_required(login_url='login')
def show_stu(request):
    data=student.objects.all()
    d={'data':data}
    return render(request,'view_stu.html',d)

    
@login_required(login_url='login')
def edit_stu(request,id):
    data=student.objects.get(id=id)
    error=""
    if request.method == "POST":
        n=request.POST['fname']
        r=request.POST['rollnumber']
        e=request.POST['email']
        c=request.POST['course']
        d=request.POST['dob']
        ph=request.POST['phone']
        g=request.POST['gender']
        a=request.POST['address']
        t=request.POST['tfee']
        p=request.POST['pfee']
        l=request.POST['lfee']
        img=request.FILES['image']

        data.name=n
        data.rollnumber=r
        data.email=e
        data.course=c
        data.dob=d
        data.phone=ph
        data.gender=g
        data.address=a
        data.tfee=t
        data.pfee=p
        data.lfee=l
        data.image=img

        try:
            data.save()
            error="no"
        except:
            error="yes"
    d={'data':data,'error':error}
    return render(request,'edit_stu.html',d)


@login_required(login_url='login')
def del_stu(request,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect('view_stu')


@login_required(login_url='login')
def search_data(request):
    return render(request,'search.html')

@login_required(login_url='login')
def search_stu(request):
    n=request.POST['search']
    data=student.objects.filter(name__icontains=n)
    d={'data':data}
    return render(request,'view_stu.html',d)


def Logout(request):
    logout(request)
    return redirect('login')



def change_pass(request):
    if request.method == "POST":
      op=request.POST['current']
      np=request.POST['new']
      user=request.user
      if not user.check_password(op):
        return redirect('account')
      user.set_password(np)
      user.save()
    return redirect('login')

def account(request):
    return render(request,'change_password.html')

   
     