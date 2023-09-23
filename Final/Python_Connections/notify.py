# IT has some time limitations it worls though 

from twilio.rest import Client

def notify_recevier(r_phone):
    try :
        account_sid = 'ACf34751f83fea0a8b52f08f97d429f7c5'
        auth_token = '574d210e79a3dbe84d99b087e55354f1'
        client = Client(account_sid, auth_token)
        r_phone = "+91"+r_phone
        message = client.messages.create(
        from_='+12563056025',
        to=r_phone ,
        body="Reached the Destination"
        )
        print(message.sid)
    except:
        print("Api not supported so sms not sent to recevier....Reached Destination")

def notify_sender(s_phone) :
    try:
        account_sid = 'ACf34751f83fea0a8b52f08f97d429f7c5'
        auth_token = '574d210e79a3dbe84d99b087e55354f1'
        client = Client(account_sid, auth_token)
        s_phone = "+91"+s_phone
        message = client.messages.create(
        from_='+12563056025',
        to=s_phone ,
        body="Reached the Pickup Point !!!"
        )
        print(message.sid)
    except:
        print("Api not supported so sms not sent to Sender....Reached Pickup point")

def malfunction() :
    try:
        account_sid = 'ACf34751f83fea0a8b52f08f97d429f7c5'
        auth_token = '574d210e79a3dbe84d99b087e55354f1'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='+12563056025',
        to='+919324526912' , #phone number of headquaters
        body="Malfunction occured please retrive me !!!!"
        )
        print(message.sid)
    except:
        print("Api not supported so sms not sent to HeadQuaters....Malfunction !!!")
