# coding: utf-8

from api import models
from api import serializers

from rest_framework import generics
from rest_framework import filters

from rest_framework.response import Response

from rest_framework.authtoken.models import Token


"""
TOKEN
"""


class ObtainAuthToken(generics.CreateAPIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = serializers.AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': unicode(token.key),
        }

        return Response(content)


"""
PROJECTS
"""


class ProjectListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.ProjectSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id', 'name']

    def get_queryset(self):
        return models.Project.objects.filter(access__user=self.request.user)


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        return models.Project.objects.all()


"""
ACCESS
"""


class AccessListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.AccessSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']

    def get_queryset(self):
        return models.Access.objects.filter(user=self.request.user)


class AccessRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AccessSerializer

    def get_queryset(self):
        return models.Access.objects.all()


"""
TASKS
"""


class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.TaskSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id', 'name', 'creation_date']

    def get_queryset(self):
        return models.Task.objects.filter(project__access__user=self.request.user)


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return models.Task.objects.all()


"""
LABELS
"""


class LabelListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.LabelSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id', 'name']

    def get_queryset(self):
        return models.Label.objects.all()


class LabelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LabelSerializer

    def get_queryset(self):
        return models.Label.objects.all()


"""
Files
"""


class FileListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.FileSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id', 'name']

    def get_queryset(self):
        return models.File.objects.all()


class FileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FileSerializer

    def get_queryset(self):
        return models.File.objects.all()


"""
COMMENTS
"""


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']

    def get_queryset(self):
        return models.Comment.objects.all()


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return models.Comment.objects.all()


"""
Kanboards
"""


class KanboardListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.KanboardSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id', 'name']

    def get_queryset(self):
        return models.Kanboard.objects.all()


class KanboardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.KanboardSerializer

    def get_queryset(self):
        return models.Kanboard.objects.all()


"""
Columns of kanboard
"""


class ColumnListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.ColumnSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id', 'name']

    def get_queryset(self):
        return models.Column.objects.all()


class ColumnRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ColumnSerializer

    def get_queryset(self):
        return models.Column.objects.all()