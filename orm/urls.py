from django.urls import path, include
from . import views
urlpatterns = [
   # path('user/', include(user_urls, namespace='user')),
   path('student/',views.Student1.as_view()),
   path('article/', views.ArticleView.as_view()),
   path('teacher/',views.Teacher.as_view()),
   path('area/',views.AreaView.as_view())
   # path('teacher/',include(teacher_urls)),
   # path('lessons/',include(lessons_urls)),
]