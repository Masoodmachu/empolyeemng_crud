from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from employee.models import Employee,Company,Department,CustomUser
from employee.forms import EmployeeForm
# Create your views here.


def home(request):
    c=Company.objects.all()
    d=Department.objects.all()
    return render(request,"home.html",{'c':c,'d':d})


# def add(request):
#     c = Company.objects.all()
#     d = Department.objects.all()
#
#     if (request.method == 'POST'):
#         name = request.POST['name']
#         age = request.POST['age']
#         company = request.POST['company']
#         department = request.POST['department']
#         address = request.POST['address']
#         image = request.FILES['image']
#         phone_number = request.POST['phone']
#         salary = request.POST['salary']
#
#         d=Department.objects.get(name=department)
#         c=Company.objects.get(name=company)
#
#         e = Employee.objects.create(name=name,age=age,company=c,department=d,address=address,image=image,phone_number=phone_number,salary=salary)
#         e.save()
#
#         return render(request, "addemo.html", {'c': c, 'd': d})
#
@login_required
def add(request):


    if(request.method=='POST'):

        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    form=EmployeeForm()

    return render(request,"addemo.html",{'f':form},)


@login_required()
def viewemp(request):
    e=Employee.objects.all()
    return render(request,"viewemp.html",{'e':e})


@login_required()
def detail(request,pk):

    e=Employee.objects.filter(id=pk)


    return render(request,"detailview.html",{'h':e})

@login_required()
def update(request,pk):
    e=Employee.objects.get(id=pk)

    if(request.method=='POST'):
        form=EmployeeForm(request.POST,request.FILES,instance=e)
        if form.is_valid():
            form.save()
            return viewemp(request)


    form=EmployeeForm(instance=e)

    return (
        render(request,"update.html",{'form':form}))

@login_required()
def delete(request,pk):

    e=Employee.objects.filter(id=pk)
    e.delete()

    return viewemp(request)
@login_required()
def viewdepemp(request,pk):

    c=Company.objects.get(id=pk)
    e=Employee.objects.filter(company=c)
    return render(request,"viewdepemp.html",{'e':e})

def register(request):

    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        phonenumber = request.POST['phone']
        address = request.POST['address']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if (cpassword == password):
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=first_name, last_name=last_name, phone=phonenumber,
                                                  address=address)
            user.save()
            return redirect('employee:login')
        else:
            return HttpResponse("Password does not match")

    return render(request,"register.html")

def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('employee:home')
        else:
            return HttpResponse('Invalid username and Password')

    return render(request,"login.html")
@login_required()
def logout(request):
    auth.logout(request)
    return redirect('employee:login')