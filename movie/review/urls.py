from django.contrib import admin
from django.urls import path
from django .conf import settings
from django.conf.urls.static import static
from review import views
app_name="review"
urlpatterns = [
    
      path("addmovie",views.addmovie,name='addmovie'),
      path("",views.viewmovie,name='viewmovie'),
      path("updel/<int:p>",views.update_delete,name='updel'),
      path("delete/<int:p>",views.delete,name='delete'),
      path("update/<int:p>",views.update,name='update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
