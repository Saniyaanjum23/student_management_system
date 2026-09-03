# student_management_system

class Student(models.Model):
    ID=models.CharField(max_length=100, unique=True)
    Name=models.CharField(max_length=100, unique=True)
    mail=models.CharField(max_length=100, unique=True)