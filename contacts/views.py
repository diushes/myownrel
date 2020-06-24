from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ContactSerializer
from .models import Contact


class ContactAPIView(APIView):

    def get(self, request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)