from django.urls import path


from sapp import views

urlpatterns=[
    path('',views.login),
    path('admins_home',views.admins_home,name="admins_home"),
    path('logout',views.logout,name="logout"),
    path('approve_teacher',views.approve_teacher,name="approve_teacher"),
    path('approve_teacherpost',views.approve_teacherpost,name="approve_teacherpost"),
    path('acceptteacher/<int:id>',views.acceptteacher,name="acceptteacher"),
    path('rejectteacher/<int:id>',views.rejectteacher,name="rejectteacher"),
    path('block_teacher',views.block_teacher,name="block_teacher"),
    path('blockkktecher/<int:id>',views.blockkktecher,name="blockkktecher"),
    path('unblockteacher/<int:id>',views.unblockteacher,name="unblockteacher"),
    path('blockkkstudent/<int:id>',views.blockkkstudent,name="blockkkstudent"),
    path('unblockstudent/<int:id>',views.unblockstudent,name="unblockstudent"),
    path('block_student',views.block_student,name="block_student"),
    path('block_studentpost',views.block_studentpost,name="block_studentpost"),
    path('chatwith_teacher',views.chatwith_teacher,name="chatwith_teacher"),
    path('Snd_complaintreply/<int:id>',views.Snd_complaintreply,name="Snd_complaintreply"),
    path('Snd_complaintreplypost',views.Snd_complaintreplypost,name="Snd_complaintreplypost"),
    path('snd_instructionss',views.snd_instructionss,name="snd_instructionss"),
    path('snd_instructions',views.snd_instructions,name="snd_instructions"),
    path('viewinstruction',views.viewinstruction,name="viewinstruction"),
    path('delinstruction/<int:id>',views.delinstruction,name="delinstruction"),
    path('View_complaint',views.View_complaint,name="View_complaint"),
    path('View_complaintsearch',views.View_complaintsearch,name="View_complaintsearch"),
    path('View_feedback',views.View_feedback,name="View_feedback"),
    path('View_feedbacks',views.View_feedbacks,name="View_feedbacks"),

    path('add_managequest', views. add_managequest, name=" add_managequest"),
    path('add_managequestpost', views. add_managequestpost, name=" add_managequestpost"),
    path('Add_managesalary', views. Add_managesalary, name=" Add_managesalary"),
    path('Add_managesalarypost', views. Add_managesalarypost, name=" Add_managesalarypost"),
    path('View_salary', views. View_salary, name=" View_salary"),
    path('View_salarypost', views. View_salarypost, name=" View_salarypost"),
    path('edit_salary/<int:id>', views. edit_salary, name=" edit_salary"),
    path('deletesalary/<int:id>', views. deletesalary, name=" deletesalary"),
    path('viewsalary', views. viewsalary, name=" viewsalary"),
    path('edit_salarypost', views. edit_salarypost, name=" edit_salarypost"),
    path('add_materials', views.add_materials, name="add_materials"),
    path('add_materialspost', views.add_materialspost, name="add_materialspost"),
    path('deletematerial/<int:id>', views.deletematerial, name="deletematerial"),
    path('add_Questions', views.add_Questions, name="add_Questions"),
    path('add_Questionspost', views.add_Questionspost, name="add_Questionspost"),
    path('edit_Questions/<int:id>', views.edit_Questions, name="edit_Questions"),
    path('edit_Questionspost', views.edit_Questionspost, name="edit_Questionspost"),
    path('upd_stu', views.upd_stu, name="upd_stu"),
    path('deleteqs/<int:id>', views.deleteqs, name="deleteqs"),
    path('add_test', views.add_test, name="add_test"),
    path('add_testpost', views.add_testpost, name="add_testpost"),
    path('edit_test/<int:id>', views.edit_test, name="edit_test"),
    path('deletetest/<int:id>', views.deletetest, name="deletetest"),
    path('edit_testpost', views.edit_testpost, name="edit_testpost"),
    path('chatwith_Admin', views.chatwith_Admin, name="chatwith_Admin"),
    path('chatwith_Students', views.chatwith_Students, name="chatwith_Students"),
    path('manage_studymaterials', views.manage_studymaterials, name="manage_studymaterials"),
    path('manage_test', views.manage_test, name="manage_test"),
    path('pay_history', views.pay_history, name="pay_history"),
    path('teacher_home', views. teacher_home, name=" teacher_home"),
    path('teacher_signup', views.teacher_signup, name="teacher_signup"),
    path('View_instructions', views.View_instructions, name="View_instructions"),
    path('View_request', views.View_request, name="View_request"),
    path('acceptrequest/<int:id>', views.acceptrequest, name="acceptrequest"),
    path('rejectrequest/<int:id>', views.rejectrequest, name="rejectrequest"),
    path('View_result', views.View_result, name="View_result"),
    path('View_resultpost', views.View_resultpost, name="View_resultpost"),

    path('login', views.login, name="login"),
    path('logincode', views.logincode, name="logincode"),
    path('logout', views.logout, name="logout"),
    path('registercode', views.registercode, name="registercode"),



    path('chatwithteacher', views.chatwithteacher, name='chatwithteacher'),
    path('chatview1', views.chatview1, name='chatview1'),
    path('coun_msg1/<int:id>', views.coun_msg1, name='coun_msg1'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),



    #____________________STUDENT___________________________



    path('student_home', views.student_home, name="student_home"),
    path('stdregister', views.stdregister, name="stdregister"),
    path('stdregisterpost', views.stdregisterpost, name="stdregisterpost"),
    path('sendcomplaint', views.sendcomplaint, name="sendcomplaint"),
    path('sendcomplaintpost', views.sendcomplaintpost, name="sendcomplaintpost"),
    path('viewreply', views.viewreply, name="viewreply"),
    path('sendfeedback', views.sendfeedback, name="sendfeedback"),
    path('sendfeedbackpost', views.sendfeedbackpost, name="sendfeedbackpost"),
    path('viewmaterial', views.viewmaterial, name="viewmaterial"),
    path('viewmaterialpost', views.viewmaterialpost, name="viewmaterialpost"),
    path('viewteacher', views.viewteacher, name="viewteacher"),
    path('sendrequest/<int:id>', views.sendrequest, name="sendrequest"),
    path('attendtest/<int:id>', views.attendtest, name="attendtest"),
    path('viewtest', views.viewtest, name="viewtest"),
    path('requeststatus', views.requeststatus, name="requeststatus"),
    path('attendtestsearch', views.attendtestsearch, name="attendtestsearch"),
    path('viewresult', views.viewresult, name="viewresult"),
    path('viewresultpost', views.viewresultpost, name="viewresultpost"),
    path('attendexam', views.attendexam, name="attendexam"),
    path('stuview_profile', views.stuview_profile, name="stuview_profile"),
    path('upd_staf', views.upd_staf, name="upd_staf"),
    path('update_students', views.update_students, name="update_students"),
    path('update_teacher', views.update_teacher, name="update_teacher"),
     path('update_student', views.update_student, name="update_student"),
    path('attendtest1', views.attendtest1, name="attendtest1"),
    path('atexam', views.atexam, name="atexam"),
    path('viewsalarytopay', views.viewsalarytopay, name="viewsalarytopay"),
    path('viewsalarytopaycode', views.viewsalarytopaycode, name="viewsalarytopaycode"),
    path('on_payment_success', views.on_payment_success, name="on_payment_success"),
    path('user_pay_proceed/<int:id>/<int:sla>', views.user_pay_proceed, name="user_pay_proceed"),
    path('view_profile', views.view_profile, name="view_profile"),


    #_________________________CHAT WITH STUDENT________________________
    #
    path('chatwithteacherfromstudent', views.chatwithteacherfromstudent, name='chatwithteacherfromstudent'),
    path('chatview2', views.chatview2, name='chatview2'),
    path('coun_msg2/<int:id>', views.coun_msg2, name='coun_msg2'),
    # path('coun_insert_chat1/<str:msg>/<int:id>', views.coun_insert_chat1, name='coun_insert_chat1'),



    #_________________________CHAT WITH TEACHER_______________________


path('chatwithstudent', views.chatwithstudent, name='chatwithteacher'),
path('chatview', views.chatview, name='chatview'),
path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
# path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),


    #_________________________________CHAT WITH ADMIN_________________________


    path('chatwithadmin', views.chatwithadmin, name='chatwithadmin'),
    # path('chatview3', views.chatview3, name='chatview3'),
    # path('coun_msg3/<int:id>', views.coun_msg3, name='coun_msg3'),
    path('coun_msg4/<int:id>', views.coun_msg4, name='coun_msg4'),
    # path('coun_insert_chat3/<str:msg>/<int:id>', views.coun_insert_chat3, name='coun_insert_chat3'),



    #______________________PAYMENT______________________________



    # path('viewsalarytopaycode1', views.viewsalarytopaycode1, name="viewsalarytopaycode1"),
    path('on_payment_success1', views.on_payment_success1, name="on_payment_success1"),
    path('user_pay_proceed1/<int:id>', views.user_pay_proceed1, name="user_pay_proceed1"),



]