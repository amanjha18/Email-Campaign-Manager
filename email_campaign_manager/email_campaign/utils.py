# campaign_manager/utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils import timezone
from multiprocessing import Pool
from .models import Campaign, Subscriber
from email_campaign_manager.task_celery import app
from email_campaign_manager.settings import EMAIL_HOST_USER

def send_campaign_email(campaign, recipient_list):
    subject = campaign.subject
    message = campaign.plain_text_content

    # Load the base email template
    base_template = get_template('base_campaign_template.html')

    # Render the campaign email content
    context = {
        'subject': campaign.subject,
        'preview_text': campaign.preview_text,
        'article_url': campaign.article_url,
        'html_content': campaign.html_content,
        'plain_text_content': campaign.plain_text_content,
    }
    email_content = base_template.render(context)

    # Create and send the email to all recipients
    msg = EmailMultiAlternatives(subject, message, EMAIL_HOST_USER, recipient_list)
    msg.attach_alternative(email_content, "text/html")
    msg.send()

@app.task
def send_daily_campaign(): 
    # Get the campaign you want to send daily (assuming there's only one)
    campaign = Campaign.objects.first()

    if campaign:
        # Get all active subscribers associated with the campaign
        subscriber_list = Subscriber.objects.filter(is_active=True)

        if subscriber_list:
            recipient_list = [subscriber.email for subscriber in subscriber_list]

            # Send the same campaign to all subscribers in parallel
            with Pool(processes=4) as pool:
                pool.starmap(send_campaign_email, [(campaign, recipient_list)])
