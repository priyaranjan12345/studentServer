from rest_framework import permissions
from myuserauth.permission import IsSuperuser
from myuserauth.models import Students
from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .serializer import StudentSerializer
from .models import Students
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class StudentsData(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()

class StudentData(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()
    #permission_classes = [IsSuperuser]
    #authentication_classes = [TokenAuthentication]

    def get(self, request):
        print(request.data)
        return self.list(request)

    def post(self, request):
        return self.create(request)

class StudentDetails(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    lookup_field = 'id'
    serializer_class = StudentSerializer
    queryset = Students.objects.all()

    def get(self, request, id=None):
        return self.retrieve(request, id)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id=None):
        return self.destroy(request, id)
