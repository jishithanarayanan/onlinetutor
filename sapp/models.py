
from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    type=models.CharField(max_length=90)

class teacher_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=90)
    lastname=models.CharField(max_length=90)
    gender=models.CharField(max_length=90)
    place=models.CharField(max_length=90)
    post=models.CharField(max_length=90)
    pin=models.BigIntegerField()
    qualification=models.CharField(max_length=90)
    proof=models.FileField()
    experience=models.CharField(max_length=90)
    phonenumber=models.BigIntegerField()
    email=models.CharField(max_length=90)
    photo=models.FileField()


class student_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=90)
    lastname = models.CharField(max_length=90)
    age = models.IntegerField()
    gender = models.CharField(max_length=90)
    place = models.CharField(max_length=90)
    post = models.CharField(max_length=90)
    pin = models.BigIntegerField()
    email = models.CharField(max_length=90)
    photo=models.FileField()
    phonenumber = models.BigIntegerField()
    standard = models.CharField(max_length=90)


class instructions_table(models.Model):
    instructions_details=models.CharField(max_length=90)
    date=models.DateField()

class feedback_table(models.Model):
    STUDENT_ID=models.ForeignKey(student_table,on_delete=models.CASCADE)
    TEACHER_ID=models.ForeignKey(teacher_table,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=90)
    rating=models.CharField(max_length=90)
    date=models.DateField()



class complaint_table(models.Model):
    STUDENT_ID=models.ForeignKey(student_table,on_delete=models.CASCADE)
    date=models.DateField()
    complaint=models.CharField(max_length=90)
    reply=models.CharField(max_length=90)


class chat_table(models.Model):
    FROM_ID=models.ForeignKey(login_table,on_delete=models.CASCADE,related_name="a")
    TO_ID=models.ForeignKey(login_table,on_delete=models.CASCADE,related_name="b")
    date=models.DateField()
    chatbox=models.CharField(max_length=90)

class request_table(models.Model):
    STUDENT_ID=models.ForeignKey(student_table,on_delete=models.CASCADE)
    TEACHER_ID=models.ForeignKey(teacher_table,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=90)

class studymaterials_table(models.Model):
    date=models.DateField()
    TEACHER_ID=models.ForeignKey(teacher_table,on_delete=models.CASCADE)
    subject=models.CharField(max_length=90)
    notes=models.FileField()


class test_table(models.Model):
    date=models.DateField()
    TEACHERS_ID=models.ForeignKey(teacher_table,on_delete=models.CASCADE)
    test=models.CharField(max_length=90)
    details=models.CharField(max_length=90)

class question_table(models.Model):
    TEST_ID=models.ForeignKey(test_table,on_delete=models.CASCADE)
    questions=models.CharField(max_length=90)
    option1=models.CharField(max_length=90)
    option2=models.CharField(max_length=90)
    option3=models.CharField(max_length=90)
    option4=models.CharField(max_length=90)
    result=models.CharField(max_length=90)



class payment_table(models.Model):
    date=models.DateField()
    REQUEST_ID=models.ForeignKey(request_table,on_delete=models.CASCADE)
    fee=models.CharField(max_length=90)
    status=models.CharField(max_length=90)

class result_table(models.Model):
    date=models.DateField()
    TEACHER_ID=models.ForeignKey(student_table,on_delete=models.CASCADE)
    QUESTION_ID=models.ForeignKey(question_table,on_delete=models.CASCADE)
    result=models.CharField(max_length=90)



class salary_table(models.Model):
    TEACHER_ID=models.ForeignKey(teacher_table,on_delete=models.CASCADE)
    date=models.DateField()
    salary=models.CharField(max_length=90)


class paymeny_salary(models.Model):
    SALARY_ID = models.ForeignKey(salary_table, on_delete=models.CASCADE)
    date = models.DateField()
    month = models.CharField(max_length=90)
    status = models.CharField(max_length=90)