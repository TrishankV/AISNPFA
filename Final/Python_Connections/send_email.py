#You require to use a less secured email for the cnnection and sending of email or it womnt happen , google stops the requets so keep thaat kn mind 

import smtplib
from email.mime.text import MIMEText

def send_email(name_contact,email,phone_contact,message):

    # Set up the SMTP server
    sender_email="Email"
    sender_password="Password"
    message = "Name : "+ name_contact + "\nEmail of Sender : " + email +"\nPhone : "+ phone_contact + "\n Querey : " + message
    try: 
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the email message
        email_message = MIMEText(message)
        email_message["Subject"] = "Querey from a Sender"
        print("Subject :Querey from a Sender ")
        email_message["From"] = sender_email
        email_message["To"] = email

    # Send the email
        server.send_message(email_message)
        server.quit()
    except:
        print("Mail not send as it was blocked due to security reasons or senders email and password is missing")

# Example usage
if __name__ == "__main__" :
    sender_email = "youremail"
    sender_password = "pass"
    recipient_email = "tvashikar@gmail.com"
    subject = "Task Completed"
    message = "Hello, Your task has been completed successfully!"
    send_email(sender_email, sender_password, recipient_email, subject, message)
