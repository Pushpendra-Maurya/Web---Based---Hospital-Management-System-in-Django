from django.urls import path 

from  .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name = 'about'),
    path('admin_login/',views.login,name='login'),
    path('logout/',views.logout_admin,name='logout'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('view_doctor/', views.view_doctor, name= 'view_doctor'), 
    path('add_doctor/', views.add_doctor, name= 'add_doctor'),
    path('delete_doctor(?P<int:pid>)', views.delete_doctor, name= 'delete_doctor'),
    
]
