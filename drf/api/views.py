from .models import School
from .serializers import SchoolSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class SchoolList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes(IsAdminUser,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SchoolSerializer(queryset, many=True)
        return Response(serializer.data)

    @permission_classes((IsAdminUser, ))
    def post(self, request, format=None):
        user = request.user
        serializer = SchoolSerializer(data=request.data, context={'user':user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SchoolDetail(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer