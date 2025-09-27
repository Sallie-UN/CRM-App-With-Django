from django.db import models

# Create your models here.
class Record(models.Model):
    # In the bracket...we are inheriting model
    created_at = models.DateTimeField(auto_now_add=True)
    # The code above is so that django will know to add the date and time automatically when a record is created
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    
    # Now we want to define what we want to happen when we call any of these records (what we want to show on the screen when we access any one of the records)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # So if you just call one of these records in the sdmin area or the webpage, it will return the first name and the last name