from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home (request):
    records = Record.objects.all() # This is going to grab all the records in the table and assign it to this recors variable
    # check to see if user is logging in...now we want to pass the records into our webpade so that once a user is logged in, the user can see all the records but no one logged out will be abe to see the records. Note that befor you can use the records in your views.py file...you'll have to import it above from the models .py file where it was created.
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["Password"]
        
        # Authenticate
        user = authenticate(request, username =username, password=password)
        
        # Run some logic on on the authenticated user
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In!")
            return redirect("home")
        else:
            messages.success(request, "There was an Error Logging In. Please Try again...")
            return redirect("home")

    else:
        return render (request, "home.html", {"records":records})
    # Inside the curly braces of the code above is where the records variable was passed in so it can be visible on the webpage when a user is logged in

def logout_user(request):
    logout(request)
    messages.success(request, "You have Been Logged Out!!!")
    return redirect("home")

def register_user(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        # The condition below checks whether the form is being posted (filling the form and submitting)
        
        if form.is_valid():
            form.save()
            # Now that the user has filled the registration form, checked if it is a valid form and the form has been saved...
            # We want to authenticate the user and log them in so that they can use the website
            
            # Authenticate and Login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            
            # Now you can log them in by passing the login request and the user that is requesting to login as a parameter
            login(request, user)
            messages.success(request, "You have successfully Registered. Welcome!!!")
            return redirect("home")
        
        # The next condition (the else) checks if...since they did not post the form, then they are just going to visit the website
        # We are not going to pass in a request because we have not filled out the form yet, the user is just going to the site. They want to fill out the form but they haven't done it yet.
        # You don't need to pass in the post yet but you do need to pass in the form that will be filled by the user (The form hasn't been posted yet).
    else:
        form = SignUpForm()
        return render(request,"register.html", {"form":form})
 
        # The code above will pass the form into the webpage so that we can do something with it
    return render(request,"register.html", {"form":form})        

def customer_record(request, pk):
    # When the integer of the particular post is passed in as a primary key...django knows to return the exact record/post with the padded integer.
    # Everybody's record has a unique primary key
    
    # Before passing in any particular record to the web page...you want to check and make sure that the user is actually logged in
        if request.user.is_authenticated:
            # Look up record
            customer_record = Record.objects.get(id=pk)
            return render(request,"record.html", {"customer_record":customer_record})   
        else:
            messages.success(request, "You must be logged in to view that page...")
            return redirect("home")
        
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect("home")
    else:
        messages.success(request, "You must be logged in to perform that action...")
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
          if request.method == "POST":
              if form.is_valid():
                  add_record = form.save()
                  messages.success(request, "Record Added successfully...")
                  return redirect("home")
          return render(request, "add_record.html", {"form":form})
    else:
         messages.success(request, "You must be logged in to perform that action...")   
         return redirect("home")
     
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance= current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully...")
            return redirect("home")
        return render(request, "update_record.html", {"form":form})
    else:
        messages.success(request, "You must be logged in to perform that action...")
        return redirect("home")
 