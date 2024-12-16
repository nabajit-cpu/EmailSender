import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace these values with your own
SMTP_SERVER = 'smtp.gmail.com'  # For Gmail
SMTP_PORT = 587  # TLS port
USERNAME = 'nabajitboro796@gmail.com'
PASSWORD = 'umuh eric rndc pscz'  # Use app-specific password if using 2FA

# Email content
from_email = USERNAME
to_email = 'nabajitboro777@gmail.com'  # Replace with recipient's email
subject = 'Test Email'
body = 'This is a test email sent from a Python script.'

# Create a multipart message and set headers
message = MIMEMultipart()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

# Add body to the message
message.attach(MIMEText(body, 'plain'))

try:
    # Set up the server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure the connection
    server.login(USERNAME, PASSWORD)  # Log in to your account

    # Send the email
    server.send_message(message)
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")

finally:
    # Terminate the SMTP session
    server.quit()
