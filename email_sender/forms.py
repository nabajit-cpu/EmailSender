from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile  # Importing SimpleUploadedFile

class EmailForm(forms.Form):
    recipients = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), label='Recipient Emails')
    subject = forms.CharField(max_length=100, label='Subject', initial='Application for Software Engineer Position')
    company = forms.CharField(max_length=100, label='Company Name')
    hr_name = forms.CharField(max_length=100, label='HR Name')  # New field for HR name
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}), label='Email Body', required=False)
    attachment = forms.FileField(required=True, label='Attachment')

    # Set a default attachment (path to the PDF file)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachment'].initial = SimpleUploadedFile(
            '/home/ubuntu/EmailApp/email_sender/Nabajit_Boro.pdf', 
            b'', 
            content_type='application/pdf'
        )  # Adjust path and content accordingly
    sender_email = forms.EmailField(label='Your Email', initial='nabajitboro796@gmail.com')  # Set default email
