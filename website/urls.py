from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    # path("login/", views.login_user, name = "login"),
    path("logout/", views.logout_user, name = "logout"),
    path("register/", views.register_user, name = "register"),
    path("record/<int:pk>", views.customer_record, name = "record"),
    path("delete_record/<int:pk>", views.delete_record, name = "delete_record"),
    path("add_record/", views.add_record, name = "add_record"),
    path("update_record/<int:pk>", views.update_record, name = "update_record"),
]

# <int:pk> means that we are passing the integer as a primary key so our url will look somehing like this - localhost:8000/record/2
# The "2" in the url stands for the id number of the record that django automatically adds for us depending on the number of previous posts existing when we create a record
# Passing in a primary key is a very easy and normal way to look up specific records from a webpage
