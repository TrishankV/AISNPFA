# #You require to use a less secured email for the cnnection and sending of email or it womnt happen , google stops the requets so keep thaat kn mind 

# import smtplib
# from email.mime.text import MIMEText

# def send_email(name_contact,sender_email,phone_contact,message):

#     # Set up the SMTP server
#     print(name_contact)
#     print(sender_email)
#     print(phone_contact)
#     print(message)
#     message = "Name : "+ name_contact + "\nEmail of Sender : " + sender_email +"\nPhone : "+ phone_contact + "\n Querey : " + message
#     try: 
#         # sender = "query_from_user_simulation@outlook.com"
#         # recipient = "query_from_user_simulation@outlook.com"
#         sender = "ai.39.vedant.ranade@gmail.com"
#         recipient = "ai.39.vedant.ranade@gmail.com"
#         email_message = MIMEText(message)
#         email_message["Subject"] = name_contact + " trying to Contact"
#         email_message["From"] = sender
#         email_message["To"] = recipient
#         print("email drafted.....")

#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()
#             server.login(sender,)  # Use the App Password here
#             server.sendmail(sender,recipient, msg.as_string())
#             server.quit()

#     except smtplib.SMTPAuthenticationError:
#         print("Email not sent. Authentication failed. Please check the sender's email and password.")
#     except smtplib.SMTPException as e:
#         print("Email not sent due to an SMTP error:", str(e))
#     except Exception as e:
#         print("Email not sent due to an unexpected error:", str(e))

# # Example usage
# if __name__ == "__main__" :
#     sender_email = "vedanranade2612@gmail.com"
#     # sender_password = "pass"
#     name = "Vedant Ranade"
#     Phone = "9324526912"
#     message = "I have a query is this mail working in the miniproject presentation???"
#     send_email(name,sender_email,Phone,message)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
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

def send_email_notify(sender_email,message):

    # Set up the SMTP server
    message = "Email Registered: {}\n Notification: {}".format(sender_email,message)

    try:
        sender = "ai.39.vedant.ranade@gmail.com"
        recipient = sender_email
        email_message = MIMEText(message)
        email_message["Subject"] = "Alert"
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

def billing(sender_email,message,document_path=None):

    # Set up the SMTP server

    try:
        sender = "ai.39.vedant.ranade@gmail.com"
        recipient = sender_email
        email_message = MIMEMultipart()
        email_message["Subject"] = "Check Your Bill"
        email_message["From"] = sender
        email_message["To"] = recipient
        print("Email drafted...")
        
        message = "Email Registered: {}\n Notification: {}".format(sender_email,message)
        text_message = MIMEText(message)
        email_message.attach(text_message)
        # if document_name:
        #     script_directory = os.path.dirname(__file__)  # Get the directory of the current script
        #     document_path = os.path.join(script_directory, document_name)

        with open(document_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename="+document_path)  # You can specify the filename

            email_message.attach(part)


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
    # send_email(name, sender_email, Phone, message)
    # send_email_notify('ai.58.vedant.ranade@gmail.com','Reached Destination')
    billing('ai.58.vedant.ranade@gmail.com','Reached Destination','Vedant.pdf')
