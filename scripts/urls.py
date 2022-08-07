from django.urls import path  
from .views import *  
  
app_name = 'scripts'  
urlpatterns = [  
    path('upload_script/', enter_script, name = "enter-script"),
    path('', home, name = "home"),
    path('archive/', archive, name = "home"),
    path('thanks/', thanks, name = "thanks"),
    path('filter/', image_filter, name = "image-filter"),
    path('documentation/', documentation, name = "documentation")  
    ]