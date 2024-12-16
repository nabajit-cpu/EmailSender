import smtplib

# Test SMTP settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = 'nabajitboro796@gmail.com'
PASSWORD = 'umuh eric rndc pscz'

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(USERNAME, PASSWORD)  # Log in to your account
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")
