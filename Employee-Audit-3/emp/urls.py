from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("home/", emp_home),
     path("department-list/", department_list, name='department_list'),
    # path("update-department/", update_department),
    # path("delete-department/", delete_department),
     path("delete-department/<int:department_id>/", delete_department, name='delete_department'),
      path("update-department/<int:department_id>/", update_department, name='update_department'),
    path('delete-emp/<int:emp_id>/', delete_employee, name='delete_employee'),
    path("update-emp/<int:emp_id>", update_emp),
    path("do-update-emp/<int:emp_id>", do_update_emp),
    path('add-department/', add_department, name='add_department'),
    path("add_employee/", add_employee),
    
    # path("delete-emp/<int:emp_id>", delete_employee),
    # path("update-emp/<int:emp_id>", update_emp),
    # path("do-update-emp/<int:emp_id>", do_update_emp),
    # path('add-department/', add_department),

    path('add-skill/', add_skill),
    path('add-office/', add_office),
    path('add-project-assignment/', add_project_assignment),
    path('add_employee_skill/', add_employee_skill, name='add_employee_skill'),

    path('employee-skill-list/', views.employee_skill_list, name='employee_skill_list'),
     path('add-task/', views.add_task, name='add_task'),
    path('task-list/', views.task_list, name='task_list'),
    path('employee_office_assignment_list/', views.employee_office_assignment_list, name='employee_office_assignment_list'),
    path('delete_employee_office_assignment/<int:assignment_id>/', views.delete_employee_office_assignment, name='delete_employee_office_assignment'),
    path('update_employee_office_assignment/<int:assignment_id>/', views.update_employee_office_assignment, name='update_employee_office_assignment'),
    path('update_employee_office_assignment/<int:assignment_id>/', views.update_employee_office_assignment, name='update_employee_office_assignment'),
    path('add_employee_office_assignment/', views.add_employee_office_assignment, name='add_employee_office_assignment'),
    path('add-position/', add_position),
]
