from twilio.rest import Client
#pip install karna mat bhulna
account_sid = 'ACa0909188bdfb531dc9c6b91cb3f89d25'# apne account ka sid
auth_token = '3b0e42da86266d97fbc8542acdf55aa1' #apne account ke tokens
client = Client(account_sid, auth_token)
mssg = input("Enter the message you want to send: ")
try:
    message = client.messages.create(
    from_='+15188643786', #apne account mai yeh sender number milega
    body= mssg ,
    to='+919324526912' #khud ka registered number
    )
    print(message.sid)
except Exception as err :
        print(err)