from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    code=models.CharField(max_length=10,unique=True)
    Hod_name=models.CharField(max_length=100, blank=True)

    class Meta:
        ordering=['name']


class Course(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100,unique=True)
    department=models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='Courses',
    )
    semester=models.SmallIntegerField(default=1)
    credits=models.SmallIntegerField(default=1)

class Student(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]
    roll_no=models.CharField(max_length=20, unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100, unique=True)

    #blank=True -> the FORM allow it to be empty
    #null=True -> the DATABASE allow itto be empty
    phone=models.CharField(max_length=15, blank=True)
    date_of_birth=models.DateField(null=True, blank=True)

    gender= models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    #PROJECT = you cannot delete a department that still has students.
    department=models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='students',
    )
    year_of_study=models.PositiveSmallIntegerField(default=1)
    address=models.TextField(blank=True)
    photo=models.ImageField(upload_to='student_photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    admitted_on=models.DateField(default=timezone.now)
    #Django fills this in automatically when the row iscreated.
    created_at= models.DateTimeField(auto_now_add=True) 
    class Meta:
        ordering= ['roll_no']