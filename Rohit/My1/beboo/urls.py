from django.urls import path
from .import views

urlpatterns = [
    path('',views.home1,name='home'),
    path('about/',views.About1,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dash/', views.dashboard, name='dashboard'),
    path('logout/', views.logout1, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login1, name='login'),

]