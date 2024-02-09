from django.db import models

class Record(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True, max_length=100)
    phone=models.CharField(unique=True, max_length=10)
    Address=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    zipcode=models.CharField(max_length=6)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return(f"{self.first_name} {self.last_name} {self.phone} {self.email} {self.Address} {self.city} {self.state} {self.zipcode} {self.created_at}")
