from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone
# Create your models here.

class JobCategory(models.Model):
    job_choices=(
        ('plumber','plumber'),
        ('carpenter','carpenter'),
        ('welder','welder'),
        ('Cooking','Cooking'),
        ('Tile worker','Tile worker'),
        ('painter','painter'),
        ('interior designer','interior designer'),
        ('gardner','gardner'),
        ('Laundry and ironing', 'Laundry and ironing')
    )
    job_name=models.CharField(choices=job_choices,max_length=50) 
    image = models.FileField(upload_to='jobs')  
    job_details = models.CharField(max_length=150)

    def __str__(self):
        return self.job_name


class CustomUser(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    user_type = models.CharField( max_length=100,null=True, blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    pic=models.FileField(upload_to='userprofile')

    def __str__(self):
        return self.username

class Job(models.Model):
    jobcategory_id = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    Price = models.IntegerField()
    date = models.DateField(default=timezone.now,blank=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.jobcategory_id.job_name


    
class JobApplications(models.Model):
    status_choices=(
        ('Approved','Approved'),
        ('Pending','Pending'),
        ('Rejected','Rejected')
    )
    employer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    job_id = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=status_choices, default="Pending", max_length=50)
    booked_date = models.DateField(default=timezone.now,blank=False)
    total_amount = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True)
    review = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.job_id.jobcategory_id.job_name    

# class JobBooking(models.Model):
#     job_id = models.ForeignKey(Job, related_name='worker_booking', on_delete=models.CASCADE,null=True,blank=True)
#     employer_id = models.ForeignKey(CustomUser, related_name='employer_booking', on_delete=models.CASCADE,null=True,blank=True)
    



