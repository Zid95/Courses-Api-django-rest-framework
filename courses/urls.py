from django.urls import path  
from .api import InstructorView,CoursesListView,CoursesDetailView,InstructorDetail,CategoryDetailView

urlpatterns = [
    path('api/instructor/list',InstructorView.as_view(),name="instructor_list"),
    path('api/courses/list',CoursesListView.as_view(),name="courses_list"),
    path('api/instructor/detail/<int:pk>',InstructorDetail.as_view(),name="instructor_detail"),
    path('api/courses/detail/<int:pk>',CoursesDetailView.as_view(),name="courses_detail"),
    path('api/courses/category_detail/<int:pk>',CategoryDetailView.as_view(),name="category_detail"),
]
