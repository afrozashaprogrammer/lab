from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request):
    friend = {
        "name": "Bithe",
        "address": "Jenidah",
        "phone": "01303456677"
    }
    return Response(friend)