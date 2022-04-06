from django.urls import path
from .views import *

urlpatterns = [
    path('',Homepage.as_view()),
    path('book',BookList.as_view()),
    path('issue',BookIssueRecords.as_view()),
    path('issueform',BookIssue.as_view()),
    path('student',StudentDetail.as_view()),
    path('add',AddBooks.as_view()),
    path('add-stud',AddStudent.as_view()),
    path('update-student/<str:pk>',UpdateStudent.as_view()),
    path('update-book/<str:pk>',UpdateBooks.as_view()),
    path('delete-student/<str:pk>',DeleteStudent.as_view()),
    path('delete-book/<str:pk>',DeleteBooks.as_view()),
    path('signup',registeradmin),
    path('logpage',loginpage)
]