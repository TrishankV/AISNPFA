# #You require to use a less secured email for the cnnection and sending of email or it womnt happen , google stops the requets so keep thaat kn mind 

# import smtplib
# from email.mime.text import MIMEText

# def send_email(sender_email, sender_password, recipient_email, subject, message):
#     # Set up the SMTP server
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
#     server.login(sender_email, sender_password)

#     # Create the email message
#     email_message = MIMEText(message)
#     email_message["Subject"] = subject
#     email_message["From"] = sender_email
#     email_message["To"] = recipient_email

#     # Send the email
#     server.send_message(email_message)
#     server.quit()

# # Example usage
# sender_email = "youremail"
# sender_password = "pass"
# recipient_email = "tvashikar@gmail.com"
# subject = "Task Completed"
# message = "Hello, Your task has been completed successfully!"

# send_email(sender_email, sender_password, recipient_email, subject, message)
import smtplib
from email.mime.text import MIMEText

def send_email(name_contact, sender_email, phone_contact, message):

    # Set up the SMTP server
    message = "Name: {}\nEmail of Sender: {}\nPhone: {}\nQuery: {}".format(name_contact, sender_email, phone_contact, message)

    try:
        sender = "ai.39.vedant.ranade@gmail.com"
        recipient = "ai.39.vedant.ranade@gmail.com"
        email_message = MIMEText(message)
        email_message["Subject"] = "{} Trying to Contact".format(name_contact)
        email_message["From"] = sender
        email_message["To"] = recipient
        print("Email drafted...")

        # Use your Gmail account and App Password for secure connection
        gmail_user = "your@gmail.com"
        app_password = "your_app_password"

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender,"hosy zgdh uoti hvel")
            server.sendmail(sender, recipient, email_message.as_string())
            print("Email sent...")

    except smtplib.SMTPAuthenticationError:
        print("Email not sent. Authentication failed. Please check the sender's email and App Password.")
    except smtplib.SMTPException as e:
        print("Email not sent due to an SMTP error:", str(e))
    except Exception as e:
        print("Email not sent due to an unexpected error:", str(e))

# Example usage
if __name__ == "__main__":
    sender_email = "Test@gmail.com"
    # Replace "your_app_password" with your actual App Password
    app_password = "your_app_password"
    name = "Vedant Ranade"
    Phone = "9324526912"
    message = "I have a query: Is this mail working in the miniproject presentation?"
    send_email(name, sender_email, Phone, message)
