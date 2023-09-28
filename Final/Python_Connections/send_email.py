#You require to use a less secured email for the cnnection and sending of email or it womnt happen , google stops the requets so keep thaat kn mind 

import smtplib
from email.mime.text import MIMEText

def send_email(name_contact,sender_email,phone_contact,message):

    # Set up the SMTP server
    print(name_contact)
    print(sender_email)
    print(phone_contact)
    print(message)
    message = "Name : "+ name_contact + "\nEmail of Sender : " + sender_email +"\nPhone : "+ phone_contact + "\n Querey : " + message
    try: 
        sender = "query_from_user_simulation@outlook.com"
        recipient = "query_from_user_simulation@outlook.com"
        email_message = MIMEText(message)
        email_message["Subject"] = name_contact + " trying to Contact"
        email_message["From"] = sender
        email_message["To"] = recipient
        print("email drafted.....")

        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, "Argentavious")
        smtp.sendmail(sender, recipient, email_message.as_string())
        print("email sent.....")
        smtp.quit()

    except:
        print("Mail not send as it was blocked due to security reasons or senders email and password is missing")

# Example usage
if __name__ == "__main__" :
    sender_email = "vedanranade2612@gmail.com"
    # sender_password = "pass"
    name = "Vedant Ranade"
    Phone = "9324526912"
    message = "I have a query is this mail working in the miniproject presentation???"
    send_email(name,sender_email,Phone,message)
