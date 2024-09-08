from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationsSerializerClass

class RegistrationsApiView(generics.GenericAPIView):
    serializer_class = RegistrationsSerializerClass

    def post(self, request, *args, **kwargs):
        serializer = RegistrationsSerializerClass(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message': 'user created successfully',
                'detail': f" you registered with email: {serializer.validated_data['email']} ",
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
