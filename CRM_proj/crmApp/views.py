from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def dashboard(request):
    data=Record.objects.all()
    # checked to see if logged in
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        #authenticate
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been sucessfully loged in.")
            return redirect('dashboard')
        else:
            messages.error(request,"Authentication Error!")
            return redirect('dashboard')
    
    return render(request,'dashboard.html',{'data':data})

# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request,"You have been Loged Out!")
    return redirect('dashboard')

def register_user(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"You are Successfully Register Welcome!")
            return redirect('dashboard')
    else:
        form= SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})
    
def customer_record(request, pk):
    if request.user.is_authenticated:
        cust_data=Record.objects.get(id=pk)
        context={'cust_data':cust_data}
        return render(request, 'customer.html',{'cust_data':cust_data})
    
    else:
        messages.info(request, "You Must be Logged in to View the detail...")
        return redirect('dashboard')
    

def update_cutomer(request, pk):
    if request.user.is_authenticated:
        current_data=Record.objects.get(id=pk)
        form= AddRecordForm(request.POST or None,instance=current_data)
        if form.is_valid():
            form.save()
            messages.success(request,'Record has been updated successfully..')
            return redirect('dashboard')
        return render(request,'update_cutomer.html',{'form':form})


    else:
        messages.info(request, "You Must be Logged in to View the detail...")
        return redirect('dashboard')


def delete_cutomer(request, pk):
    if request.user.is_authenticated:
        del_customer=Record.objects.get(id=pk)
        del_customer.delete()
        messages.info(request,'Customer Deleted successfully!')
        return redirect('dashboard')

    else:
        messages.info(request, "You Must be Logged in to View the detail...")
        return redirect('dashboard')    

def add_record(request):
    form= AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid:
                print("abc")
                add_record=form.save()
                # print(add_record)
                messages.success(request,'Record added successfully..')
                return redirect('dashboard')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.error(request,'Must be logged in!')
        return redirect('dashboard')
