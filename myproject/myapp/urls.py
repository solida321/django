from django.urls import path
from . import views

urlpatterns = [
  
   #path('',views.home),
    path('product/',views.product),
    path('student/',views.student),
    path('database/login/',views.login_form),
    path('login/show/',views.show),
    path('database/',views.login_database),
    path('base/',views.base),
    path('home/',views.home),
    path('foradmin/',views.admin),
    path('foradmin1/',views.admin1),
    path('create_post/',views.create_post,name='post'),
    path('show_post',views.show_post,),
    path('update_post/<int:id>/',views.update_post,),
    path('delete_post/<int:id>/',views.delete_post,),
    path('Customer/',views.create_byformmodels,name='Modelsform')

    
]

     