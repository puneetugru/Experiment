from rest_framework.views import APIView
from rest_framework.response import Response
from .models import School
from .serializers import SchoolSerializer


class SchoolList(APIView):
    def get(self, request, format=None):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)