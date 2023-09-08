# Email Campaign Manager

Email Campaign Manager is a web application that allows you to manage and send email campaigns efficiently. It is built using the Django web framework and is designed to provide a user-friendly interface for creating, scheduling, and tracking email campaigns.

## Features

- **Subscriber Management:** Easily add subscribers to your email list with their email addresses and first names. Includes an endpoint for unsubscribing users.

- **Campaign Creation:** Create and schedule email campaigns with detailed information, including subject, preview text, article URL, HTML content, plain text content, and the published date.

- **Django Admin Integration:** Utilize Django admin to add new records to various tables, ensuring easy management of campaigns and subscribers.

- **SMTP Integration:** Send daily campaigns using SMTP. The application supports SMTP integration, allowing you to use Mailgun or any other SMTP service.

- **Email Template Rendering:** Campaign emails are rendered with information from a base template, ensuring a consistent and professional look.

- **Optimized Sending:** Optimize the sending time by using pub-sub with multiple threads, enabling parallel dispatching of emails for improved efficiency.

## Getting Started

Follow these steps to set up and run the Email Campaign Manager locally for development and testing:

### Prerequisites

- Python (3.x)
- Django (3.x)
- Database system (e.g., PostgreSQL)
- SMTP server or service (e.g., Mailgun)

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:amanjha18/Email-Campaign-Manager.git
   cd email-campaign-manager
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

