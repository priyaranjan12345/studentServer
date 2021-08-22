from django.urls import path
from django.urls.conf import include
from .views import StudentsData, StudentData
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('students',StudentsData, basename='students')


urlpatterns = [
    path('student/', include(router.urls)),
    path('student/v2/', StudentData.as_view()),
]
