from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Gender choices

GENDER = (
   ("male","MALE"),
   ("female", "FEMALE"),
)

#creating parents model
class Parent(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   photo = models.ImageField(upload_to="images",blank=False)
   date_of_birth = models.DateField(blank=False)
   phone_number = models.IntegerField(blank=False)
   adress = models.CharField(max_length=100,blank=False)
   gender = models.CharField(choices=GENDER,blank=False,max_length=20)

#creating a staff model
class Staff(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   photo = models.ImageField(upload_to="images",blank=False)
   date_of_birth = models.DateField(blank=False)
   phone_number = models.IntegerField(blank=False)
   adress = models.CharField(max_length=100,blank=False)
   gender = models.CharField(choices=GENDER,blank=False,max_length=20)
   salary = models.IntegerField(default=00)
   isNoneTeaching = models.BooleanField(default=True)
   isPrincipal = models.BooleanField(default=False)
   isDeputy = models.BooleanField(default=False)
   isTeacher = models.BooleanField(default=False)
   isDriver = models.BooleanField(default=False)


#create a subject
class Subject(models.Model):
   name = models.CharField(max_length=30)

#labs
class Labs(models.Model):
   name = models.CharField(max_length=30)
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   technitian = models.ForeignKey(Staff,on_delete=models.CASCADE)

#creating a book model
class Book(models.Model):
   name = models.CharField(max_length=30,blank=False)
   author =  models.CharField(max_length=40,blank=False)
   #one book can belong to categories
   category = models.ForeignKey(Subject,on_delete=models.CASCADE)

class Club(models.Model):
   name = models.CharField(max_length=50,blank=False)
   #one club can have many patrons
   patron = models.ForeignKey(Staff,on_delete=models.CASCADE)

# classroom model
class ClassRoom(models.Model):
   class_name = models.CharField(max_length=20,blank=False)
   class_teacher = models.OneToOneField(Staff,on_delete=models.CASCADE)

class Fee(models.Model):
   amount_paid =models.IntegerField(default=0)
   slip_id = models.CharField(max_length=30,blank=False)
   student_name = models.ForeignKey('Student',on_delete=models.CASCADE)
   term = models.CharField(max_length=20,blank=False)
   expected_amount = models.IntegerField(blank=False,default=20000)
   due_date = models.DateField(blank=False)
   date_paid = models.DateField(auto_now_add=True)
# creating a student profile extending from the User model
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images",blank=False)
    date_of_birth = models.DateField(blank=False)
    phone_number = models.IntegerField(blank=False)
    adress = models.CharField(max_length=100,blank=False)
    condition = models.CharField(max_length=200,blank= True,null=True)
    # this is better  to avoid anyone putting fake genders
    gender = models.CharField(choices=GENDER,blank=False,max_length=20)
    #a student can have many subjects and a subject can be done by many studentd
    subjects = models.ManyToManyField(Subject)
    #many students can belong to one parent
    parents_name = models.ForeignKey(Parent,on_delete=models.CASCADE,blank=False)
    grade = models.CharField(blank=False,max_length=5)
    #many students can belong to many classes
    class_room = models.ManyToManyField(ClassRoom)
    #one student can have may fees payed 
    school_fee = models.ForeignKey(Fee,on_delete=models.CASCADE)
    attedance = models.BooleanField(default=False)
    is_class_rep = models.BooleanField(default=False)
    #one student can have many  books
    book_issued = models.ForeignKey(Book,on_delete=models.CASCADE)
    #many students can belong to many clubs
    club = models.ManyToManyField(Club)

    
# creating a fee model


#creating a notice
class Notice(models.Model):
   title = models.CharField(max_length=30,blank=False)
   description = models.TextField()
   exp_date = models.DateField(blank=False)

#create a new application
class NewApplication(models.Model):
   students_name = models.CharField(max_length=30,blank=False)
   parents_name = models.CharField(max_length=30,blank=False)
   email =models.EmailField(blank=False)
   phone_number = models.IntegerField(blank=False)
   adm_class = models.CharField(max_length=5,blank=False)
   transfer_reason = models.TextField(blank=False)
   previous_school = models.CharField(max_length=30,blank=False)
   previous_grade = models.CharField(max_length=3,blank=False)

#test model
class Test(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   score = models.IntegerField(default=0)
   student = models.ForeignKey(Student,on_delete=models.CASCADE)

## results
class Results(models.Model):
   test = models.ForeignKey(Test,on_delete=models.CASCADE)