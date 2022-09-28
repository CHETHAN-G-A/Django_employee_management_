from django.shortcuts import render, redirect
from.models import Employee, Role, Department, Customer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):
    return render(request,'login.html')

def all_emp(request):
    employees = Employee.objects.all()
    return render(request,'all_emplooyees.html', {'emps':employees})

def add_emp(request):
    department = Department.objects.all()
    role = Role.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])

        new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone)
        new_emp.save()
        return redirect('all_emp')

    return render(request,'add_emp.html', {'depts':department , 'roles':role})

def del_emp(request , emp_id=0):
    employees = Employee.objects.all()
    if emp_id:
        emp_to_be_deleted = Employee.objects.get(id=emp_id)
        emp_to_be_deleted.delete()
        return redirect('del_emp')
    return render(request, 'del_emp.html', {'emps':employees})

def filter_emp(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        employees = Employee.objects.all()

        if first_name:
            emps = employees.filter(first_name__icontains = first_name)
        if last_name:
            emps = employees.filter(last_name__icontains = last_name)
        if dept:
            emps = employees.filter(dept__name=dept)
        return render(request, 'filter_emp.html', {'emps': emps})

    return render(request,'filter_emp.html',{'emps':employees})

def signin(request):
    error_message = None
    if request.method == 'POST':
        ## check if the email already exists ##
        e_mail = request.POST.get('e_mail')
        error_message = None
        if Customer.objects.filter(e_mail=e_mail):
            error_message = "e-mail already exists"
            return redirect("signin")

        else:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

           #validation#

            if(not first_name):
                error_message = "First name is required"
            elif(not last_name):
                error_message = "Last name is required"
            elif(not phone):
                error_message ="phone number is rerquired"

            else:
                # hashing password #
                hashed_password = make_password(password)
                # ---------------- #
                customer = Customer(first_name=first_name, last_name=last_name, phone=phone, e_mail=e_mail,password=hashed_password)
                customer.save()
                error_message = "successfully registered"

    return render(request, "signin.html",{'error_message': error_message})

def login(request):
    error_message = None
    if request.method == 'POST':
        e_mail = request.POST.get('e_mail')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(e_mail)

        if not customer:
            error_message = "User not registered"
        elif customer and check_password(password,customer.password):
            request.session['customer_id']= customer.id
            request.session['e_mail']= customer.e_mail
            return redirect("all_emp")
        else:
            error_message = "Invalid password"

    return render(request, "login.html", {'error_message':error_message})

def logout(request):
    return render(request,'login.html')