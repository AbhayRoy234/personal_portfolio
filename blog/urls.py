# from django.contrib import admin
from django.urls import path
from . import views
# from django.conf import
# from django.conf.urls.static import static,include
# from django.conf import settings
app_name="blog"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="all_blog"),
    path('<int:blog_id>/',views.details,name="details"),
    # path('blog/',include('blog.urls')),
]