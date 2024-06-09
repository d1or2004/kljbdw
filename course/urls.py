from django.urls import path
from .views import TeacherView, CourseView, AboutView, CourseDetailView, CourseUpdateView, CourseDeleteView, \
    AddNewCourseView

urlpatterns = [
    path('teachers', TeacherView.as_view(), name='teachers'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('about/', AboutView.as_view(), name='about'),
    path('course/<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('update/<int:id>/', CourseUpdateView.as_view(), name='course-update'),
    path('delete/<int:id>/', CourseDeleteView.as_view(), name='course-delete'),
    path('add_cours/', AddNewCourseView.as_view(), name='add-course'),
]
