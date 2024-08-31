from django.urls import path
from . import views

urlpatterns = [
    path('', views.presentation, name='presentation'),
    path('personal_info/', views.personalinfo,  name='personalinfo'),
    path('education/', views.education,  name='education'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('backtpresentation/', views.backtpresentation, name='backtpresentation'),
    path('backinformacionpersonal/', views.backtinforperonsal, name='backinformacionpersonal'),
    path('backestudios/', views.backtstudies, name='backestudios'),
    path('backSkills/', views.backstskills, name='backSkills')
]