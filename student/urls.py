from django.urls import path, include
from . import views
urlpatterns = [
    path("student/", views.StudentView.as_view(), name="student"),
    path("query/", views.StusView.as_view(), name="query")
]
