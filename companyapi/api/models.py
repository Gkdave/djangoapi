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

