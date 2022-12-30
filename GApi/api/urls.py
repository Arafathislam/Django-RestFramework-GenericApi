from django.urls import path
from .import views


urlpatterns = [
    #  path('studentapi/',views.StudentList.as_view()),
    #  path('showall/',views.StudentCreate.as_view()),
    #  path('find/<int:pk>/',views.StudentRetrieve.as_view()),
    #  path('update/<int:pk>/',views.StudentUpdate.as_view()),
    #   path('delete/<int:pk>/',views.StudentDestroy.as_view()),
      path('studentapi/',views.StudentLC.as_view()),
      path('studentapi/<int:pk>/',views.StudentFUD.as_view()),
    
]