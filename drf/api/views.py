from rest_framework.views import APIView
from rest_framework.response import Response
from .models import School
from .serializers import SchoolSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

#Commening out below view

class SchoolList(APIView):

    def get(self, request, format=None):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            permission_classes = (IsAdminOrReadOnly,)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)