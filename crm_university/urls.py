from django.urls import path
from . import views

app_name = 'crm_university'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('faculty/list/', views.faculty, name='faculty_list'),
    path('group/list/', views.group, name='group_list'),
    path('department/list/', views.department, name='department_list'),
    path('student/list/', views.student, name='student_list'),
    path('subject/list/', views.subject, name='subject_list'),
    path('teacher/list/', views.teacher, name='teacher_list'),
    path('faculty/create/', views.faculty_form, name='faculty_create'),
    path('group/create/', views.group_form, name='group_create'),
    path('department/create/', views.department_form, name='department_create'),
    path('student/create/', views.student_form, name='student_create'),
    path('subject/create/', views.subject_form, name='subject_create'),
    path('teacher/create/', views.teacher_form, name='teacher_create'),
    path('update/faculty/<int:pk>/', views.update_faculty, name='faculty_update'),
    path('update/group/<int:pk>/', views.update_group, name='group_update'),
    path('update/department/<int:pk>/', views.update_department, name='department_update'),
    path('update/student/<int:pk>/', views.update_student, name='student_update'),
    path('update/subject/<int:pk>/', views.update_subject, name='subject_update'),
    path('update/teacher/<int:pk>/', views.update_teacher, name='teacher_update'),
    path('delete/faculty/<int:pk>/', views.delete_faculty, name='faculty_delete'),
    path('delete/group/<int:pk>/', views.delete_group, name='group_delete'),
    path('delete/department/<int:pk>/', views.delete_department, name='department_delete'),
    path('delete/student/<int:pk>/', views.delete_student, name='student_delete'),
    path('delete/subject/<int:pk>/', views.delete_subject, name='subject_delete'),
    path('delete/teacher/<int:pk>/', views.delete_teacher, name='teacher_delete'),
]