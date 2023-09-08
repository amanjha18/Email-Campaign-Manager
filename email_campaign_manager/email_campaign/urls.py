from django.urls import path
from .views import SubscriberList, Unsubscribe, SendDailyCampaign

urlpatterns = [
    path('subscribers/', SubscriberList.as_view(), name='subscriber-list'),
    path('unsubscribe/<str:email>/', Unsubscribe.as_view(), name='unsubscribe'),
    path('send_daily_campaign/', SendDailyCampaign.as_view(), name='send_daily_campaign'),
    # Add more URLs for campaigns and other views as needed
]
