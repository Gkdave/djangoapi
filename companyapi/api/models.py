from django.db import models




class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
            (('It','It'),
            ('Non-IT','Non-It'),
            ('Mobile phone','MOBILE phone')))
    added_date = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name +'--' +self.location 

#Employee Model 

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    about=models.CharField(max_length=200)
    position=models.CharField(max_length=60,choices=(
        ('Manager','manager'),
        ('Software Developer','SD'),
        ('Project Leader','pl')
    ))

    company=models.ForeignKey(Company,on_delete=models.CASCADE)

