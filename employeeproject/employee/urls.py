
from django.urls import path, include
from employee import views
app_name='employee'

urlpatterns = [

    path('',views.home,name="home"),
    path('add/',views.add,name="add"),
    path('view/',views.viewemp,name='viewemp'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('update/<int:pk>',views.update,name="update"),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('viewdepemp/<int:pk>',views.viewdepemp,name="viewdepemp"),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]
