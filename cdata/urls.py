from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.MyFormView.as_view()),
    # path('', views.View_data.as_view()),
    path('delete/<int:id>',views.delete_data,name='delete'),
    path('update/<int:id>',views.updatedata,name='update_data'),
    
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)