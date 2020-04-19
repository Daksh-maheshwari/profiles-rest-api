from rest_framework.views import APIVIEW
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIVIEW):
    """Test API View"""
    serializer_class=serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Is mapped maually to URLs',

        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview })
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializeer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """DELETE an OBject """
        return Response({'method': 'DELETE'})
