from rest_framework.views import APIVIEW
from rest_framework.response import Response


class HelloApiView(APIVIEW):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Is mapped maually to URLs',

        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview })
