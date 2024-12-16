# EmailApp/settings.py
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
INSTALLED_APPS = [
    # Other apps
    'email_sender',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP for sending emails
