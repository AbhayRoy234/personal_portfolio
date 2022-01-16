# from django.contrib import admin
from django.urls import path
from . import views
# from django.conf import
# from django.conf.urls.static import static,include
# from django.conf import settings
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home),
    # path('blog/',include('blog.urls')),
]