from django.urls import path
from user import views as user_views
app_name = 'user'
urlpatterns = [
    path('getlist', user_views.getlist),
    path('create',user_views.create),
    path('upload',user_views.upload),
    path('returnhtml',user_views.returnhtml,name='returnhtml'),
    path('returnjson',user_views.returnjson),
    path('retunfile',user_views.retunfile),
    path('setresponseheaders',user_views.setresponseheaders),
    path("redirecturl",user_views.redirecturl),
    path("redirectin",user_views.redirectin),
]