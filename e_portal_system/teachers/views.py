
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from adminsite.models import StudentRegistration, RoleForTeacher, AddSubject
from adminsite.serializers import GetStudentSerializers, FetchSubject,CreateSubjectSerializers
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from teachers.serializers import (
                                AttendanceUploadsModelSerializer,
                                ResultUploadModelSerializer,
                          )
from rest_framework.generics import CreateAPIView
from teachers.models import AttendanceUploads, ResultUpload


# Create your views here.
class AttendanceUploadsView(CreateAPIView):
    serializer_class = AttendanceUploadsModelSerializer
    queryset = AttendanceUploads.objects.all()

class FetchAttendanceByStudent(viewsets.ViewSet):

    def list(self, request,student_id):
        queryset = AttendanceUploads.objects.filter(student_id=student_id)
        serializer = AttendanceUploadsModelSerializer(queryset, many=True)
        return Response(serializer.data)


class ResultUploadUploadView(CreateAPIView):
    serializer_class = ResultUploadModelSerializer
    queryset = ResultUpload.objects.all()


#to get the list of students classWises
class StudentListForAttendance(viewsets.ViewSet):

    def list(self, request, class_number,teacher_id, subject_name):
        queryset = AttendanceUploads.objects.filter(class_number=class_number, teacher_id=teacher_id, subject_name=subject_name)
        serializer = AttendanceUploadsModelSerializer(queryset, many=True)
        return Response(serializer.data)


# For teacher to get subjects based on class_number
class GetSubjectsByTeacher(viewsets.ViewSet):
    
    def list(self, request,teacher_id):
        queryset=RoleForTeacher.objects.filter(teacher_name= teacher_id)
        serializer = FetchSubject(queryset, many=True)
        return Response(serializer.data)
        
class FetchResultByStudent(viewsets.ViewSet):
    def list(self, request,student_id):
        queryset = ResultUpload.objects.filter(student_id=student_id)
        serializer = ResultUploadModelSerializer(queryset, many=True)
        return Response(serializer.data)