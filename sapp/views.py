import datetime

import razorpay
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json
# Create your views here.
from sapp.models import *
from email.mime.text import MIMEText
import smtplib


def login(request):
    return render(request,"loginindex.html")


def logout(request):
    auth.logout(request)
    return render(request,"loginindex.html")


def logincode(request):
    try:
        username=request.POST['textfield']
        pwd=request.POST['password']
        ob=login_table.objects.get(username=username,password=pwd)
        if ob.type=="admin":
            request.session['lid'] = ob.id
            var = auth.authenticate(username='admin', password='admin')
            if var is not None:
                auth.login(request, var)
            return HttpResponse('''<script>alert("Login Successfully");window.location="/admins_home"</script>''')
        elif ob.type=="teacher":
            request.session['lid'] = ob.id
            var = auth.authenticate(username='admin', password='admin')
            if var is not None:
                auth.login(request, var)
            return HttpResponse('''<script>alert("Login Successfully");window.location="/teacher_home"</script>''')
        elif ob.type=="student":
            request.session['lid'] = ob.id
            var = auth.authenticate(username='admin', password='admin')
            if var is not None:
                auth.login(request, var)
            return HttpResponse('''<script>alert("Login Successfully");window.location="/student_home"</script>''')
        else:
         return HttpResponse('''<script>alert("Invalid User Try Again!");window.location="/"</script>''')
    except:
        return HttpResponse('''<script>alert("Invalid User Try Again!");window.location="/"</script>''')






@login_required(login_url='/')
def admins_home(request):
    return render(request,"admin/adminindex.html")


@login_required(login_url='/')
def approve_teacher(request):
    res=teacher_table.objects.all()
    return render(request,"admin/approvetchr.html",{"data":res})

@login_required(login_url='/')
def approve_teacherpost(request):
    s = request.POST['t1']
    res = teacher_table.objects.filter(firstname__istartswith=s)
    return render(request,"admin/approvetchr.html", {"data": res})


AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='email@gmail.com'
EMAIL_HOST_PASSWORD='8086262304'
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
###############>>>>settings
from django.core.mail import send_mail
import random





import smtplib
from email.mime.text import MIMEText
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .models import login_table, teacher_table  # Replace with the correct import path for your models

def acceptteacher(request, id):
    ob = login_table.objects.get(id=id)
    ob.type = 'teacher'
    ob.save()
    q = teacher_table.objects.get(LOGIN__id=id)

    email = q.email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as gmail:
            gmail.ehlo()
            gmail.starttls()
            gmail.login('jishithanarayanan6365@gmail.com', 'sxqo ygdu dccd fbnu')

            msg = MIMEText("Your Are Accepted ")
            msg['Subject'] = 'Online Tutor'
            msg['To'] = email
            msg['From'] = 'jishithanarayanan6365@gmail.com'

            gmail.send_message(msg, from_addr='jishithanarayanan6365@gmail.com', to_addrs=email)

    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert("invalid");window.location="/approve_teacher"</script>''')

    return HttpResponse('''<script>alert("Accepted successfully");window.location="/approve_teacher"</script>''')



# @login_required(login_url='/')
# def acceptteacher(request,id):
#     ob = login_table.objects.get(id=id)
#     ob.type = 'teacher'
#     ob.save()
#     q=teacher_table.objects.get(LOGIN__id=id)
#
#     email = q.email
#     print(email)
#
#     try:
#         gmail = smtplib.SMTP('smtp.gmail.com', 587)
#         gmail.ehlo()
#         gmail.starttls()
#         gmail.login('jishithanarayanan6365@gmail.com', 'sxqo ygdu dccd fbnu')
#         print("login=======")
#     except Exception as e:
#         print("Couldn't setup email!!" + str(e))
#     msg = MIMEText("Your Are Accepted ")
#     print(msg)
#     msg['Subject'] = 'OutPass'
#     msg['To'] = email
#     msg['From'] = 'jishithanarayanan6365@gmail.com'
#
#     print("ok====")
#
#     try:
#         gmail = smtplib.SMTP('smtp.gmail.com', 587)
#         gmail.ehlo()
#         gmail.starttls()
#         gmail.send_message(msg)
#     except Exception as e:
#         print (e)
#         return HttpResponse('''<script>alert("invalid");window.location="/approve_teacher"</script>''')
#
#     return HttpResponse('''<script>alert("Accepted sucsesfully");window.location="/approve_teacher"</script>''')






@login_required(login_url='/')
def rejectteacher(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected sucsesfully");window.location="/approve_teacher"</script>''')


@login_required(login_url='/')
def block_teacher(request):
    res=teacher_table.objects.all()
    return render(request,"admin/Block- tcr.html",{"data":res})

@login_required(login_url='/')
def blockkktecher(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'block'
    ob.save()
    return HttpResponse('''<script>alert("Blocked sucsesfully");window.location="/block_teacher"</script>''')


@login_required(login_url='/')
def unblockteacher(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'teacher'
    ob.save()
    return HttpResponse('''<script>alert("Unblocked sucsesfully");window.location="/block_teacher"</script>''')


#__________________________search________

@login_required(login_url='/')
def block_student(request):
    res=teacher_table.objects.filter(LOGIN__type='teacher')
    ob=student_table.objects.all()
    return render(request,"admin/Block-stu.html",{"data":res,"val":ob})


@login_required(login_url='/')
def block_studentpost(request):
    test = request.POST['select']
    ob = request_table.objects.filter(TEACHER_ID=test,status="Accept")
    res=teacher_table.objects.all()
    return render(request, "admin/Block-stu.html", {"data": res, 'val': ob,"t":int(test), "a":1})



@login_required(login_url='/')
def blockkkstudent(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'block'
    ob.save()
    return HttpResponse('''<script>alert("Blocked sucsesfully");window.location="/block_student"</script>''')


@login_required(login_url='/')
def unblockstudent(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'student'
    ob.save()
    return HttpResponse('''<script>alert("Unblocked sucsesfully");window.location="/block_student"</script>''')


@login_required(login_url='/')
def chatwith_teacher(request):
    return render(request,"admin/chtwithTeacher.html")


@login_required(login_url='/')
def Snd_complaintreply(request,id):
    request.session['er']=id
    return render(request,"admin/Sndcomplaintreply.html")

@login_required(login_url='/')
def Snd_complaintreplypost(request):
    reply=request.POST['textarea']

    ob=complaint_table.objects.get(id=request.session['er'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>alert("Reply Sended!!");window.location="/View_complaint"</script>''')




@login_required(login_url='/')
def snd_instructionss(request):
    instruction=request.POST['textarea']

    ob=instructions_table()
    ob.instructions_details=instruction
    ob.date=datetime.datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Instruction Added");window.location="/viewinstruction"</script>''')

@login_required(login_url='/')
def snd_instructions(request):
    return render(request,"admin/sndinstuctions.html")

@login_required(login_url='/')
def viewinstruction(request):
    res=instructions_table.objects.all()
    return render(request,"admin/viewinstruction.html",{"data":res})

def delinstruction(request,id):
    res=instructions_table.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location="/viewinstruction"</script>''')




@login_required(login_url='/')
def View_complaint(request):
    res = complaint_table.objects.all()
    return render(request,"admin/Vcomplaint.html",{"data":res})

@login_required(login_url='/')
def View_complaintsearch(request):
    nm=request.POST['search']
    res = complaint_table.objects.filter(date__icontains=nm)
    return render(request,"admin/Vcomplaint.html",{"data":res})


@login_required(login_url='/')
def View_feedback(request):
    res = feedback_table.objects.all()
    return render(request,"admin/Vfeedback.html",{"data":res})


@login_required(login_url='/')
def View_feedbacks(request):
    nm=request.POST['search']
    res = feedback_table.objects.filter(TEACHER_ID__firstname__icontains=nm)
    return render(request,"admin/Vfeedback.html",{"data":res})



@login_required(login_url='/')
def Add_managesalary(request):
    res=salary_table.objects.all()
    return render(request,"admin/addmanagesalary.html",{"data":res})


@login_required(login_url='/')
def Add_managesalarypost(request):
    nm = request.POST['t1']
    res = salary_table.objects.filter(TEACHER_ID__firstname__icontains=nm)
    return render(request, "admin/addmanagesalary.html", {"data": res})



@login_required(login_url='/')
def View_salary(request):
    res=teacher_table.objects.all()
    return render(request,"admin/addsalary.html",{"data":res})

@login_required(login_url='/')
def View_salarypost(request):
    tchr=request.POST['select']
    salary=request.POST['textfield2']

    ob=salary_table()
    ob.salary=salary
    ob.date=datetime.datetime.today()
    ob.TEACHER_ID=teacher_table.objects.get(id=tchr)
    ob.save()
    return HttpResponse('''<script>alert("Salary Added");window.location="/Add_managesalary"</script>''')


@login_required(login_url='/')
def edit_salary(request,id):
    res=teacher_table.objects.all()
    res1=salary_table.objects.get(id=id)
    request.session['es']=id
    return render(request,"admin/editsalary.html",{"val":res,"data":res1})

@login_required(login_url='/')
def edit_salarypost(request):
    tchr=request.POST['select']
    salary=request.POST['textfield2']

    ob=salary_table.objects.get(id=request.session['es'])
    ob.salary=salary
    ob.date=datetime.datetime.today()
    ob.TEACHER_ID=teacher_table.objects.get(id=tchr)
    ob.save()
    return HttpResponse('''<script>alert("Edit Success");window.location="/Add_managesalary"</script>''')

@login_required(login_url='/')
def deletesalary(request,id):
    res=salary_table.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert("Delete Success");window.location="/Add_managesalary"</script>''')


@login_required(login_url='/')
def viewsalary(request):
    res=salary_table.objects.filter(TEACHER_ID__LOGIN__id=request.session['lid'])
    for i in res:
        ob=paymeny_salary.objects.filter(SALARY_ID__id=i.id)
        if len(ob)==0:
            i.status="Pending"
        else:
            i.status=ob[0].status

    return render(request,"Teacher/viewsalary.html",{"data":res})


@login_required(login_url='/')
def add_managequest(request):
    res=question_table.objects.filter(TEST_ID__TEACHERS_ID__LOGIN__id=request.session['lid'])
    ob=test_table.objects.filter(TEACHERS_ID__LOGIN__id=request.session['lid'])
    return render(request,"Teacher/addmanagequest.html",{"data":res,'val':ob})

@login_required(login_url='/')
def add_managequestpost(request):
    test = request.POST['crop']
    print(test,"öooooooooooooooooooo")
    res = question_table.objects.filter(TEST_ID__id=test)
    ob=test_table.objects.filter(TEACHERS_ID__LOGIN__id=request.session['lid'])
    return render(request, "Teacher/addmanagequest.html", {"data": res,'val':ob,"t":int(test)})


@login_required(login_url='/')
def add_Questions(request):
    res=test_table.objects.filter(TEACHERS_ID__LOGIN__id=request.session['lid'])
    return render(request,"Teacher/addQues.html",{"data":res})

@login_required(login_url='/')
def add_Questionspost(request):
    test=request.POST['crop']
    qs=request.POST['textfield']
    op1=request.POST['textfield2']
    op2=request.POST['textfield3']
    op3=request.POST['textfield4']
    op4=request.POST['textfield5']
    ansr=request.POST['textfield6']
    if(ansr == op1 or ansr == op2 or ansr == op3 or ansr == op4):

        ob=question_table()
        ob.questions=qs
        ob.option1=op1
        ob.option2=op2
        ob.option3=op3
        ob.option4=op4
        ob.result=ansr
        ob.TEST_ID=test_table.objects.get(id=test)
        ob.save()
        return HttpResponse('''<script>alert("successfully Added");window.location="/add_managequest#about"</script>''')
    else:
        return HttpResponse('''<script>alert("not match");window.location="/add_Questions#about"</script>''')

@login_required(login_url='/')

def edit_Questions(request,id):
    res=test_table.objects.filter(TEACHERS_ID__LOGIN__id=request.session['lid'])
    res1=question_table.objects.get(id=id)
    request.session['eq']=id
    return render(request,"Teacher/editQues.html",{"val":res,'data':res1})

@login_required(login_url='/')
def edit_Questionspost(request):
    test=request.POST['select']
    qs=request.POST['textfield']
    op1=request.POST['textfield2']
    op2=request.POST['textfield3']
    op3=request.POST['textfield4']
    op4=request.POST['textfield5']
    ansr=request.POST['textfield6']

    ob=question_table.objects.get(id=request.session['eq'])
    ob.questions=qs
    ob.option1=op1
    ob.option2=op2
    ob.option3=op3
    ob.option4=op4
    ob.result=ansr
    ob.TEST_ID=test_table.objects.get(id=test)
    ob.save()
    return HttpResponse('''<script>alert("Edit Success");window.location="/add_managequest"</script>''')

@login_required(login_url='/')
def deleteqs(request,id):
    res=question_table.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert("Delete Success");window.location="/add_managequest"</script>''')


@login_required(login_url='/')
def manage_test(request):
    res=test_table.objects.filter(TEACHERS_ID__LOGIN__id=request.session['lid'])
    return render(request,"Teacher/Mtest.html",{"data":res})

@login_required(login_url='/')
def add_test(request):
    return render(request,"Teacher/AddTest.html")


@login_required(login_url='/')
def add_testpost(request):
    test=request.POST['textarea']
    details=request.POST['textarea2']

    ob=test_table()
    ob.test=test
    ob.details=details
    ob.date=datetime.datetime.today()
    ob.TEACHERS_ID=teacher_table.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("successfully Added");window.location="/manage_test"</script>''')


@login_required(login_url='/')
def edit_test(request,id):
    res=test_table.objects.get(id=id)
    request.session['et']=id
    return render(request,"Teacher/editTest.html",{"data":res})


@login_required(login_url='/')
def edit_testpost(request):
    test=request.POST['textarea']
    details=request.POST['textarea2']

    ob=test_table.objects.get(id=request.session['et'])
    ob.test=test
    ob.details=details
    ob.date=datetime.datetime.today()
    ob.TEACHERS_ID=teacher_table.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Edit Success");window.location="/manage_test"</script>''')



@login_required(login_url='/')
def deletetest(request,id):
    res=test_table.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert("Delete Success");window.location="/manage_test"</script>''')



@login_required(login_url='/')
def chatwith_Admin(request):
    return render(request,"Teacher/chtwithAdmin.html")


@login_required(login_url='/')
def chatwith_Students(request):
    return render(request,"Teacher/chtwithstudents.html")


@login_required(login_url='/')
def manage_studymaterials(request):
    res=studymaterials_table.objects.filter(TEACHER_ID__LOGIN__id=request.session['lid'])
    return render(request,"Teacher/Mstudy materials.html",{"data":res})


@login_required(login_url='/')
def add_materials(request):
    return render(request,"Teacher/Addmaterials.html")


@login_required(login_url='/')
def add_materialspost(request):
    subject=request.POST['select']
    material=request.FILES['file']
    fs = FileSystemStorage()
    fn1 = fs.save(material.name, material)

    ob=studymaterials_table()
    ob.subject=subject
    ob.notes=fn1
    ob.date=datetime.datetime.today()
    ob.TEACHER_ID=teacher_table.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Add Success");window.location="/manage_studymaterials"</script>''')


@login_required(login_url='/')
def deletematerial(request,id):
    res=studymaterials_table.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script>alert("Delete Success");window.location="/manage_studymaterials"</script>''')



@login_required(login_url='/')
def pay_history(request):
    return render(request,"Teacher/payhistory.html")


@login_required(login_url='/')
def teacher_home(request):
    return render(request,"Teacher/teacherindex.html")



def teacher_signup(request):
    return render(request,"Teacher/registerindex.html")

def view_profile(request):
    ob=teacher_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"Teacher/viewprofile.html",{'val':ob})


def update_teacher(request):
    ob=teacher_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"Teacher/edit_teacher.html",{'val':ob})

@login_required(login_url='/')


def upd_staf(request):

    obj = teacher_table.objects.get(LOGIN__id=request.session['lid'])
    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    exp = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    phone = request.POST['textfield7']
    email = request.POST['textfield8']
    quali = request.POST['quali']

    obj.firstname = fname
    obj.lastname = lname
    obj.experience = exp
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.phone = phone
    obj.email = email
    obj.qualification = quali
    try:
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name, photo)
        obj.photo = fn
        obj.save()
    except:
        pass
    try:
        proof = request.FILES['file2']
        fs = FileSystemStorage()
        fn = fs.save(proof.name, proof)
        obj.proof = fn
        obj.save()
    except:
        pass
    obj.save()
    return HttpResponse('''<script>alert("Profile updated successfully");window.location="/view_profile#about"</script>''')
    # else:
    #     obj = staff_table.objects.get(LOGIN__id=request.session['lid'])
    #     fname = request.POST['textfield']
    #     lname = request.POST['textfield2']
    #     age = request.POST['textfield3']
    #     place = request.POST['textfield4']
    #     post = request.POST['textfield5']
    #     pin = request.POST['textfield6']
    #     phone = request.POST['textfield7']
    #     email = request.POST['textfield8']
    #     obj.firstname = fname
    #     obj.lastname = lname
    #     obj.age = age
    #     obj.place = place
    #     obj.post = post
    #     obj.pin = pin
    #     obj.phone = phone
    #     obj.email = email
    #     obj.save()
    #     return HttpResponse('''<script>alert("sucsesfully update staff");window.location="/view_profilestaff#about"</script>''')





@login_required(login_url='/')
def View_instructions(request):
    res=instructions_table.objects.all()
    return render(request,"Teacher/vinstructions.html",{"data":res})


@login_required(login_url='/')
def View_request(request):
    res=request_table.objects.filter(TEACHER_ID__LOGIN__id=request.session['lid'])
    return render(request,"Teacher/Vrequestand approve.html",{"data":res})



@login_required(login_url='/')
def acceptrequest(request,id):
    ob = request_table.objects.get(id=id)
    ob.status = 'Accept'
    ob.save()
    return HttpResponse('''<script>alert("Accepted sucsesfully");window.location="/View_request"</script>''')



@login_required(login_url='/')
def rejectrequest(request,id):
    ob = request_table.objects.get(id=id)
    ob.status = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("Rejected sucsesfully");window.location="/View_request"</script>''')



@login_required(login_url='/')
def View_result(request):
    ob=test_table.objects.filter(TEACHERS_ID__LOGIN__id=request.session['lid'])
    # res=result_table.objects.filter(QUESTION_ID__TEST_ID__TEACHERS_ID__LOGIN__id=request.session['lid'])
    # for i in res:
    #
    #     if len(res)==0:
    #         i.res="Not Attended"
    #     else:
    #         m=0
    #         for j in res:
    #             m=m+int(j.result)
    #         i.res=str(m)+"/"+str(len(res))
    # "data": res,
    return render(request,"Teacher/Vresult.html",{'val':ob})

@login_required(login_url='/')
def viewresult(request):
    print(request.session['lid'],"------------------")
    try:
     ob = request_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'],status='Accept')
     result=[]
     for ii in ob:
         print(ob,request.session['lid'])
         res1=test_table.objects.filter(TEACHERS_ID__id=ii.TEACHER_ID.id)
         print(res1)
         for i in res1:
             ob1=result_table.objects.filter(TEACHER_ID__LOGIN__id=request.session['lid'],QUESTION_ID__TEST_ID__id=i.id)
             if len(ob1)==0:
                 i.res="Not Attended"
             else:
                 m=0
                 for j in ob1:
                     m=m+int(j.result)
                 i.res=str(m)+"/"+str(len(ob1))
             result.append(i)

     return render(request,"student/viewresult.html",{"data":result})
    except Exception as e:
         print(e)
         return render(request, "student/viewresult.html", {"data":[]})


@login_required(login_url='/')
def View_resultpost(request):
    test = request.POST['crop']
    print(test, "öooooooooooooooooooo")

    ob1 = test_table.objects.filter(TEACHERS_ID__LOGIN__id=request.session['lid'])
    ob=request_table.objects.filter(TEACHER_ID__LOGIN__id=request.session['lid'],status='Accept')
    for i in ob:
        obb=result_table.objects.filter(QUESTION_ID__TEST_ID__id=test,TEACHER_ID__id=i.STUDENT_ID.id)
        mark=0
        if len(obb)>0:
            for j in obb:
                mark=mark+int(j.result)
            i.tm=str(mark)+"/"+str(len(obb))
        else:
            i.tm="Not Attended"

    return render(request, "Teacher/Vresult.html", {"data": ob, 'val': ob1, "t": int(test)})




def registercode(request):
    fname=request.POST['fname']
    lname = request.POST['lname']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    pin= request.POST['pin']
    quali= request.POST['qlfn']
    proof= request.FILES['proof']
    fs=FileSystemStorage()
    fn=fs.save(proof.name,proof)
    exp = request.POST['exp']
    email= request.POST['email']
    phno = request.POST['phone']
    photo = request.FILES['photo']
    fs = FileSystemStorage()
    fn1 = fs.save(photo.name, photo)
    Uname= request.POST['uname']
    pwd=request.POST['pswd']
    ob=login_table()
    ob.username=Uname
    ob.password=pwd
    ob.type="pending"
    ob.save()
    ob1=teacher_table()
    ob1.LOGIN=ob
    ob1.firstname=fname
    ob1.lastname =lname
    ob1.gender =gender
    ob1.place =place
    ob1.post =post
    ob1.pin =pin
    ob1.qualification=quali
    ob1.proof =fn
    ob1.experience =exp
    ob1.email=email
    ob1.phonenumber =phno
    ob1.photo = fn1
    ob1.save()
    return HttpResponse('''<script>alert("successfully Registered  ");window.location="/"</script>''')







#_____________________________STUDENT___________________________________________


@login_required(login_url='/')
def student_home(request):
    return render(request,"student/studentindex.html")


def stdregister(request):
    return render(request,"student/registerindex.html")


def stdregisterpost(request):
    fname=request.POST['fname']
    lname = request.POST['lname']
    age = request.POST['age']
    gender = request.POST['gender']
    place = request.POST['place']
    post= request.POST['post']
    pin= request.POST['pin']
    email = request.POST['email']
    phone= request.POST['phone']
    classs = request.POST['class']
    Uname= request.POST['username']
    pwd=request.POST['password']
    photo = request.FILES['photo']
    fs = FileSystemStorage()
    fn1 = fs.save(photo.name, photo)
    ob=login_table()
    ob.username=Uname
    ob.password=pwd
    ob.type="student"
    ob.save()
    ob1=student_table()
    ob1.LOGIN=ob
    ob1.firstname=fname
    ob1.lastname =lname
    ob1.gender =gender
    ob1.place =place
    ob1.post =post
    ob1.pin =pin
    ob1.photo=fn1
    ob1.age=age
    ob1.phonenumber =phone
    ob1.standard =classs
    ob1.email=email
    ob1.save()
    return HttpResponse('''<script>alert("successfully Registered,check email for more details ");window.location="/"</script>''')

def update_student(request):
    ob=student_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"Student/edit_student.html",{'val':ob})

def upd_stu(request):

    obj = student_table.objects.get(LOGIN__id=request.session['lid'])
    fname = request.POST['fname']
    lname = request.POST['lname']
    age = request.POST['age']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    phone = request.POST['phone']
    classs = request.POST['class']

    obj.firstname = fname
    obj.lastname = lname
    obj.age =age
    obj.gender = gender
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.email = email
    obj.phone = phone
    obj.classs =classs


@login_required(login_url='/')
def sendcomplaint(request):
    return render(request,"student/sendcomplaint.html")


@login_required(login_url='/')
def sendcomplaintpost(request):
    complaint=request.POST['textfield2']

    ob=complaint_table()
    ob.complaint=complaint
    ob.date=datetime.datetime.today()
    ob.STUDENT_ID=student_table.objects.get(LOGIN_id=request.session['lid'])
    ob.reply='pending'
    ob.save()
    return HttpResponse('''<script>alert("Complaint Send!!");window.location="/viewreply"</script>''')



@login_required(login_url='/')
def viewreply(request):
    res=complaint_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'])
    return render(request,"student/viewreply.html",{"data":res})


@login_required(login_url='/')
def sendfeedback(request):
    try:
      ob=request_table.objects.get(STUDENT_ID__LOGIN__id=request.session['lid'])
      res=teacher_table.objects.filter(id=ob.TEACHER_ID.id)
      return render(request,"student/sendfeedback.html",{"data":res})
    except:
        return render(request, "student/sendfeedback.html", {"data":[]})




@login_required(login_url='/')
def sendfeedbackpost(request):
    teacher=request.POST['select']
    feedback=request.POST['textfield']
    rating=request.POST['rating']

    ob=feedback_table()
    ob.feedback=feedback
    ob.rating=rating
    ob.date=datetime.datetime.today()
    ob.TEACHER_ID=teacher_table.objects.get(id=teacher)
    ob.STUDENT_ID=student_table.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Feedback Send!!");window.location="/student_home"</script>''')




@login_required(login_url='/')
def viewmaterial(request):
    try:
        ob=request_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'],status='Accept')
        ls=[]
        for i in ob:
            ls.append(i.TEACHER_ID.id)
        res=studymaterials_table.objects.filter(TEACHER_ID__id__in=ls)
        return render(request,"student/viewmaterial.html",{"data":res})
    except Exception as e:
        print(e)

        return render(request,"student/viewmaterial.html",{"data":[]})


@login_required(login_url='/')
def viewmaterialpost(request):
    ob=request_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'],status='Accept')
    ls = []
    nm = request.POST['textfield']
    for i in ob:
        ls.append(i.TEACHER_ID.id)
    res = studymaterials_table.objects.filter(date=nm,TEACHER_ID__id__in=ls)

    # for i in ob:
    #     res = studymaterials_table.objects.filter(date=nm,TEACHER_ID_id=i.TEACHER_ID.id)
    return render(request, "student/viewmaterial.html", {"data": res,"d":nm})



@login_required(login_url='/')
def viewteacher(request):
    print(request.session['lid'])
    res=teacher_table.objects.all()
    return render(request,"student/viewteacher.html",{"data":res})


@login_required(login_url='/')
def sendrequest(request,id):
    z=request_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'],TEACHER_ID__id=id)
    if len(z) == 0:
        ob=request_table()
        ob.date=datetime.datetime.today()
        ob.status='requested'
        ob.STUDENT_ID=student_table.objects.get(LOGIN_id=request.session['lid'])
        ob.TEACHER_ID=teacher_table.objects.get(id=id)
        ob.save()
        return HttpResponse('''<script>alert("Send Request");window.location="/viewteacher"</script>''')
    else:
        return HttpResponse('''<script>alert("Already Requested");window.location="/viewteacher"</script>''')




@login_required(login_url='/')
def requeststatus(request):
    res=request_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'])
    return render(request,"student/viewrequeststatus.html",{"data":res})





@login_required(login_url='/')
def viewresultpost(request):
    test = request.POST['select']
    # res = result_table.objects.filter(QUESTION_ID__TEST_ID__id=test)
    ob = request_table.objects.get(STUDENT_ID__LOGIN__id=request.session['lid'])

    # res1=result_table.objects.filter(QUESTION_ID__TEST_ID__test=test)
    res1 = test_table.objects.filter(TEACHERS_ID__id=ob.TEACHER_ID.id)

    # for i in res1:
    #     obb = result_table.objects.filter(QUESTION_ID__TEST_ID__id=i.id,
    #                                     QUESTION_ID__TEST_ID__test=test,
    #                                       TEACHER_ID__LOGIN__id=request.session['lid']).aggregate(sum=Sum('result'))
    #     i.mark = obb['sum']
    #     print(i.mark,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    # print(res1,"kkkkkkkkkkkkkkkkkkkkkkk")
    return render(request, "student/viewresult.html", {'data':res1,'t':int(test)})


@login_required(login_url='/')
def attendexam(request,id):
    res=test_table.objects.get(id=id)
    return  render(request,"student/attendexam.html",{"data":res})
#
# def attendexampost(request):
#     question=request.POST['radiobutton']
#
#     ob=





#________________________________CHAT_________________________________

@login_required(login_url='/')
def chatwithteacher(request):
    ob = teacher_table.objects.all()
    print(ob,"HHHHHHHHHHHHHHHHHHHHHHHHH")
    return render(request,"admin/fur_chat.html",{'val':ob})



@login_required(login_url='/')
def chatview1(request):
    ob = teacher_table.objects.all()
    d=[]
    for i in ob:
        r={"name": i.firstname,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_msg1(request,id):

    ob1=chat_table.objects.filter(FROM_ID__id=id,TO_ID__id=request.session['lid'])
    ob2=chat_table.objects.filter(FROM_ID__id=request.session['lid'],TO_ID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROM_ID.id,"msg":i.chatbox,"date":i.date,"chat_id":i.id})

    obu=teacher_table.objects.get(LOGIN__id=id)

    print(obu.firstname,obu.LOGIN.id,obu.photo.url,"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return JsonResponse({"data":res,"name":obu.firstname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})



@login_required(login_url='/')
def coun_insert_chat(request,msg,id):
    try:
        print("===++++++++++++++++++++++++++===========",msg,id)
        ob=chat_table()
        ob.FROM_ID=login_table.objects.get(id=request.session['lid'])
        ob.TO_ID=login_table.objects.get(id=id)
        ob.chatbox=msg
        ob.date= datetime.date.today().strftime("%Y-%m-%d")
        ob.save()

        return JsonResponse({"task":"ok"})
    except Exception as e:
        print(e)

    # refresh messages chatlist



#_________________________________________________________________________




#___________________________CHATWITH STUDENT__________________________________


@login_required(login_url='/')
def chatwithteacherfromstudent(request):
    try:
     ob = request_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'],status="Accept")
     res = teacher_table.objects.filter(id=ob.TEACHER_ID.id)
     print(ob,"HHHHHHHHHHHHHHHHHHHHHHHHH")
     return render(request,"student/fur_chat.html",{'val':res})
    except Exception as e:
        print(e)
    return render(request, "student/fur_chat.html", {'val':[]})




@login_required(login_url='/')
def chatview2(request):
    ob = request_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'])
    # ob = teacher_table.objects.filter(id=obj.TEACHER_ID.id)
    d=[]
    for i in ob:
        r={"name": i.TEACHER_ID.firstname,'photo':i.TEACHER_ID.photo.url,'email':i.TEACHER_ID.email,'loginid':i.TEACHER_ID.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)

@login_required(login_url='/')
def coun_msg2(request,id):

    ob1=chat_table.objects.filter(FROM_ID__id=id,TO_ID__id=request.session['lid'])
    ob2=chat_table.objects.filter(FROM_ID__id=request.session['lid'],TO_ID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROM_ID.id,"msg":i.chatbox,"date":i.date,"chat_id":i.id})

    obu=teacher_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.firstname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})



@login_required(login_url='/')
def coun_insert_chat(request,msg,id):
    try:
        print("===++++++++++++++++++++++++++===========",msg,id)
        ob=chat_table()
        ob.FROM_ID=login_table.objects.get(id=request.session['lid'])
        ob.TO_ID=login_table.objects.get(id=id)
        ob.chatbox=msg
        ob.date= datetime.date.today().strftime("%Y-%m-%d")
        ob.save()

        return JsonResponse({"task":"ok"})
    except Exception as e:
        print(e)

    # refresh messages chatlist


#________________________________CHATWITHTEACHER____________________________

@login_required(login_url='/')
def chatwithstudent(request):
    try:
        ob = request_table.objects.filter(TEACHER_ID__LOGIN__id=request.session['lid'],status="Accept")
        for i in ob:
            res=student_table.objects.filter(id=i.STUDENT_ID.id)
            print (res)
        return render(request,"Teacher/fur_chat.html",{'val':res})
    except:
        return render(request,"Teacher/fur_chat.html",{'val':[]})





@login_required(login_url='/')
def chatview(request):
    obj = request_table.objects.filter(TEACHER_ID__LOGIN__id=request.session['lid'])
    # ob = student_table.objects.filter(id=obj.STUDENT_ID.id)
    d=[]
    for i in obj:
        r={"name": i.STUDENT_ID.firstname,'photo':i.STUDENT_ID.photo.url,'email':i.STUDENT_ID.email,'loginid':i.STUDENT_ID.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)

@login_required(login_url='/')
def coun_msg(request,id):

    ob1=chat_table.objects.filter(FROM_ID__id=id,TO_ID__id=request.session['lid'])
    ob2=chat_table.objects.filter(FROM_ID__id=request.session['lid'],TO_ID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROM_ID.id,"msg":i.chatbox,"date":i.date,"chat_id":i.id})

    obu=student_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.firstname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})



@login_required(login_url='/')
def coun_insert_chat(request,msg,id):
    try:
        print("===++++++++++++++++++++++++++===========",msg,id)
        ob=chat_table()
        ob.FROM_ID=login_table.objects.get(id=request.session['lid'])
        ob.TO_ID=login_table.objects.get(id=id)
        ob.chatbox=msg
        ob.date= datetime.date.today().strftime("%Y-%m-%d")
        ob.save()

        return JsonResponse({"task":"ok"})
    except Exception as e:
        print(e)

    # refresh messages chatlist




#______________________________CHAT WITH ADMIN_____________________________



@login_required(login_url='/')
def chatwithadmin(request):

    return render(request,"student/fur_chat1.html")


# @login_required(login_url='/')
# def chatview3(request):
#     ob = login_table.objects.get(type="admin")
#     d=[]
#     for i in ob:
#         r={"name": i.firstname,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
#         d.append(r)
#     return JsonResponse(d, safe=False)

@login_required(login_url='/')
# def coun_msg3(request,id):
#
#     ob1=chat_table.objects.filter(FROM_ID__id=id,TO_ID__id=request.session['lid'])
#     ob2=chat_table.objects.filter(FROM_ID__id=request.session['lid'],TO_ID__id=id)
#     combined_chat = ob1.union(ob2)
#     combined_chat=combined_chat.order_by('id')
#     res=[]
#     for i in combined_chat:
#         res.append({"from_id":i.FROM_ID.id,"msg":i.chatbox,"date":i.date,"chat_id":i.id})
#
#     obu=student_table.objects.get(LOGIN__id=id)
#
#
#     return JsonResponse({"data":res,"name":obu.firstname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})


@login_required(login_url='/')
def coun_msg4(request,id):

    ob1=chat_table.objects.filter(FROM_ID__id=id,TO_ID__id=request.session['lid'])
    ob2=chat_table.objects.filter(FROM_ID__id=request.session['lid'],TO_ID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROM_ID.id,"msg":i.chatbox,"date":i.date,"chat_id":i.id})




    return JsonResponse({"data":res,"name":"ADMIN","photo":"","user_lid":'1'})



@login_required(login_url='/')
def coun_insert_chat(request,msg,id):
    try:
        print("===++++++++++++++++++++++++++===========",msg,id)
        ob=chat_table()
        ob.FROM_ID=login_table.objects.get(id=request.session['lid'])
        ob.TO_ID=login_table.objects.get(id=id)
        ob.chatbox=msg
        ob.date= datetime.date.today().strftime("%Y-%m-%d")
        ob.save()

        return JsonResponse({"task":"ok"})
    except Exception as e:
        print(e)

    # refresh messages chatlist
"======================attent test================================="


@login_required(login_url='/')
def viewtest(request):
    try:
        ob = request_table.objects.filter(STUDENT_ID__LOGIN__id=request.session['lid'],status='Accept')
        print(ob)
        data=[]
        for i in ob:
            res = test_table.objects.filter(TEACHERS_ID__id=i.TEACHER_ID.id)
            print(res,"===============================================================")
            for j in res:
                data.append(j)
            # r = json.dumps(data)
        return render(request,"student/attendtest.html",{"data":data})
    except Exception as e:
        print(e)
        return render(request, "student/attendtest.html", {"data":[]})



@login_required(login_url='/')
def attendtestsearch(request):
    test = request.POST['select']
    res = test_table.objects.filter(test=test)
    ob = test_table.objects.filter(TEACHERS_ID__LOGIN__id=request.session['lid'])
    return render(request, "student/attendtest.html", {"data": res, 'val': ob})



@login_required(login_url='/')
def attendtest(request,id):

    z = result_table.objects.filter(QUESTION_ID__TEST_ID_id=id,TEACHER_ID__LOGIN__id=request.session['lid'])
    print(z,"zzzzzzzzzzzzzzzzz")
    if len(z) == 0:
        ob = question_table.objects.filter(TEST_ID=id)
        cnt = 0
        request.session['tid'] = id
        request.session['cnt'] = 0
        q = []
        for i in ob:
            q.append(i.id)
        res1 = question_table.objects.get(TEST_ID=id, id=q[cnt])
        return render(request, 'student/attendexam.html',
                      {'data': res1, 'ln': len(ob), 'ss': int(len(ob) - 1), 'cnt': int(cnt)})

    else:
        return HttpResponse('''<script>alert("Already Attended");window.location="/viewtest";</script>;''')



@login_required(login_url='/')
def attendtest1(request):
    ob = question_table.objects.filter(TEST_ID=request.session['tid'])
    cnt=request.session['cnt']
    q = []
    print(q,"jjjjjjjjjj")
    for i in ob:
        q.append(i.id)
    res1 = question_table.objects.get(TEST_ID=request.session['tid'], id=q[cnt])
    return render(request, 'student/attendexam.html', {'data': res1, 'ln': len(ob),'ss':int(len(ob)-1),'cnt':int(cnt)})


@login_required(login_url='/')
def atexam(request):
    q = request.POST['q']
    btn = request.POST['button']
    print(btn,"kkkkkkkkkkkkkkkkkk")
    ans = request.POST['radiobutton']
    print(q)
    print(ans)
    if btn == "FINISH":
        request.session['cnt'] = 0
        obb = question_table.objects.get(id=q)
        if obb.result == ans:
            print("hiiiiiiiiiiiiii")
            ob = result_table()

            ob.date = datetime.date.today()
            ob.TEACHER_ID = student_table.objects.get(LOGIN__id=request.session['lid'])
            ob.QUESTION_ID = question_table.objects.get(id=q)
            ob.result = 1
            ob.save()
            return HttpResponse('''<script>alert("succesfully attended");window.location="/viewtest"</script>''')
        else:
            ob = result_table()

            ob.date = datetime.date.today()
            ob.TEACHER_ID = student_table.objects.get(LOGIN__id=request.session['lid'])
            ob.QUESTION_ID = question_table.objects.get(id=q)
            ob.result = 0
            ob.save()
            return HttpResponse('''<script>alert("succesfully attended");window.location="/viewtest"</script>''')
    else:

        if btn == "NEXT":
            request.session['cnt'] = request.session['cnt'] + 1
            obb = question_table.objects.get(id=q)
            if obb.result == ans:
                ob = result_table()

                ob.date = datetime.datetime.today()
                ob.TEACHER_ID = student_table.objects.get(LOGIN=request.session['lid'])
                ob.QUESTION_ID = question_table.objects.get(id=q)
                ob.result = 1
                ob.save()
                return redirect('attendtest1')
            else:
                ob = result_table()

                ob.date = datetime.datetime.today()
                ob.TEACHER_ID = student_table.objects.get(LOGIN=request.session['lid'])
                ob.QUESTION_ID = question_table.objects.get(id=q)
                ob.result = 0
                ob.save()
                return redirect('attendtest1')









def stuview_profile(request):
    ob=student_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"student/viewprofile.html",{'val':ob})


def update_students(request):
    ob=student_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"student/edit_student.html",{'val':ob})

@login_required(login_url='/')


def upd_stu(request):

    obj = student_table.objects.get(LOGIN__id=request.session['lid'])
    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    age = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    phone = request.POST['textfield7']
    email = request.POST['textfield8']
    gender = request.POST['gender']

    obj.firstname = fname
    obj.lastname = lname
    obj.age = age
    obj.gender = gender
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.phone = phone
    obj.email = email
    try:
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name, photo)
        obj.photo = fn
        obj.save()
    except:
        pass
    try:
        proof = request.FILES['file2']
        fs = FileSystemStorage()
        fn = fs.save(proof.name, proof)
        obj.proof = fn
        obj.save()
    except:
        pass
    obj.save()
    return HttpResponse('''<script>alert("sucsesfully updated");window.location="/update_student#about"</script>''')
    # else:
    #     obj = staff_table.objects.get(LOGIN__id=request.session['lid'])
    #     fname = request.POST['textfield']
    #     lname = request.POST['textfield2']
    #     age = request.POST['textfield3']
    #     place = request.POST['textfield4']
    #     post = request.POST['textfield5']
    #     pin = request.POST['textfield6']
    #     phone = request.POST['textfield7']
    #     email = request.POST['textfield8']
    #     obj.firstname = fname
    #     obj.lastname = lname
    #     obj.age = age
    #     obj.place = place
    #     obj.post = post
    #     obj.pin = pin
    #     obj.phone = phone
    #     obj.email = email
    #     obj.save()
    #     return HttpResponse('''<script>alert("sucsesfully update staff");window.location="/view_profilestaff#about"</script>''')














"==========payment ADMIN====================="

@login_required(login_url='/')
def viewsalarytopay(request):
    res=salary_table.objects.all()
    import datetime

    # Get the current date and time
    current_date = datetime.datetime.now()
    # Extract the current month from the date
    current_month = current_date.month
    for i in res:
        obb=paymeny_salary.objects.filter(SALARY_ID__id=i.id)
        if(len(obb))>0:
            i.s="1"
        else:
            i.s="0"

    return render(request,"admin/pay salaery.html",{"data":res})


@login_required(login_url='/')
def viewsalarytopaycode(request):
    nm = request.POST['textfield']
    res = salary_table.objects.filter(TEACHER_ID__firstname__icontains=nm)
    return render(request, "admin/pay salaery.html", {"data": res})


@login_required(login_url='/')
def user_pay_proceed(request,id,sla):
    print(request.session,"kkkkkkkkkkkkkkkkkk")
    request.session['ssid']=id
    request.session['pay_amount']= sla

    # request.session['pay_amount'] = amount
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': str(sla)+"00", 'currency': "INR", 'payment_capture': '1'})
    res=login_table.objects.get(id=request.session['lid'])
    return render(request,'admin/UserPayProceed.html', {'p':payment,'val':res,"lid":request.session['lid'],"id":request.session['ssid']})



def on_payment_success(request):
    request.session['ssid']=request.GET['id']
    request.session['lid']=request.GET['lid']
    var = auth.authenticate(username='admin', password='admin')
    if var is not None:
        auth.login(request, var)
    # print(sid,"=========================")
    ob=paymeny_salary()
    ob.date=datetime.datetime.today()
    today = datetime.date.today()
    month = today.month
    ob.month=month
    ob.SALARY_ID=salary_table.objects.get(id=request.session['ssid'])
    ob.status='paid'
    ob.save()
    return HttpResponse('''<script>alert("Success! Thank you ");window.location="viewsalarytopay"</script>''')


"==========paymentSTUDENT====================="

# @login_required(login_url='/')
# def viewsalarytopaycode1(request):
#     nm = request.POST['textfield']
#     res = salary_table.objects.filter(TEACHER_ID__firstname__icontains=nm)
#     return render(request, "student/checkpayment.html", {"data": res})


@login_required(login_url='/')
def user_pay_proceed1(request,id):
    request.session['rid'] = id


    # request.session['pay_amount'] = amount
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': 250, 'currency': "INR", 'payment_capture': '1'})
    res=student_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'student/UserPayProceed.html',{'p':payment,'val':res,"lid":request.session['lid'],"id":request.session['rid']})



def on_payment_success1(request):
    request.session['rid'] = request.GET['id']
    request.session['lid'] = request.GET['lid']
    var = auth.authenticate(username='admin', password='admin')
    if var is not None:
        auth.login(request, var)
    # amt = request.session['pay_amount']
    ob=payment_table()
    ob.date=datetime.datetime.today()
    today = datetime.date.today()
    month = today.month
    ob.month=month
    ob.fee=1000
    ob.REQUEST_ID=request_table.objects.get(id=request.session['rid'])
    ob.status='paid'
    ob.details='juhgfds'
    ob.save()

    # qry = "UPDATE `charity_information` SET `amount`=`amount`-%s WHERE `id`=%s"
    # iud(qry, (amt,charity))

    return HttpResponse('''<script>alert("Success! Thank you for your Contribution");window.location="requeststatus"</script>''')

"============================="




















