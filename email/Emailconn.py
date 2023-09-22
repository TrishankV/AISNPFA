#You require to use a less secured email for the cnnection and sending of email or it womnt happen , google stops the requets so keep thaat kn mind 

import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create the email message
    email_message = MIMEText(message)
    email_message["Subject"] = subject
    email_message["From"] = sender_email
    email_message["To"] = recipient_email

    # Send the email
    server.send_message(email_message)
    server.quit()

# Example usage
sender_email = "youremail"
sender_password = "pass"
recipient_email = "tvashikar@gmail.com"
subject = "Task Completed"
message = "Hello, Your task has been completed successfully!"

send_email(sender_email, sender_password, recipient_email, subject, message)
