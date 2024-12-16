import smtplib
from django.core.files.uploadedfile import SimpleUploadedFile  # Make sure to import this
from django.shortcuts import render
from .forms import EmailForm
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            sender_email = form.cleaned_data['sender_email']  # Get sender email
            company = form.cleaned_data['company']
            hr_name = form.cleaned_data['hr_name']
            
            # Replace placeholders with company and HR name if provided
            if company:
                body = body.replace('{{ company }}', company)
            if hr_name:
                body = body.replace('{{ hr_name }}', hr_name)

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipients
            message['Subject'] = subject
            
            # Add body to the message
            message.attach(MIMEText(body, 'plain'))

            # Check if the user uploaded a new attachment
            attachment = request.FILES.get('attachment')
            if not attachment:
                # If no new attachment is provided, use the default PDF
                try:
                    with open('/home/ubuntu/EmailApp/email_sender/Nabajit_Boro.pdf', 'rb') as f:  # Specify the path to your default PDF
                        attachment = SimpleUploadedFile(f.name, f.read(), content_type='application/pdf')
                except FileNotFoundError:
                    print("Default PDF file not found.")
                    return render(request, 'email_sender/error.html')  # Handle missing default file

            # Attach the file to the message if available
            if attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)  # Encode the payload
                part.add_header('Content-Disposition', f'attachment; filename={attachment.name}')
                message.attach(part)  # Attach the MIMEBase object to the message

            try:
                # Set up the server
                SMTP_SERVER = 'smtp.gmail.com'
                SMTP_PORT = 587
                PASSWORD = 'umuh eric rndc pscz'  # Use your app-specific password

                # Connect to the SMTP server and send the email
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()  # Secure the connection
                    server.login(sender_email, PASSWORD)  # Log in to your account
                    server.send_message(message)  # Send the email

                return render(request, 'email_sender/success.html')  # Redirect to a success page

            except Exception as e:
                # Log the error (optional) and render the error template
                print(f"Error: {e}")  # You can also log this error using Django logging
                return render(request, 'email_sender/error.html')  # Render the error page

    else:
        form = EmailForm()

    return render(request, 'email_sender/email_form.html', {'form': form})
