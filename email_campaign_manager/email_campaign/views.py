from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscriber
from .serializers import SubscriberSerializer
from .utils import send_daily_campaign

class SubscriberList(APIView):
    def get(self, request):
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Unsubscribe(APIView):
    def post(self, request, email):
        try:
            subscriber = Subscriber.objects.get(email=email)
            subscriber.is_active = False
            subscriber.save()
            return Response({'message': 'Unsubscribed successfully'})
        except Subscriber.DoesNotExist:
            return Response({'error': 'Subscriber not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SendDailyCampaign(APIView):
    def get(self, request, format=None):
        try:
            send_daily_campaign()
            return Response({"message": "Daily campaign sent successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)