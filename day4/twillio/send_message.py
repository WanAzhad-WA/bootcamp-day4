import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/desecure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                      body="Hi boss, this is Azhad trying out Twilio",
                      from_='+12532378250',
                      to='+60124290640'
                  )

#call = client.calls.create(
#                        url='http://demo.twilio.com/docs/voice.xml',
#                        from_='+12532378250',
#                        to='+60182560300'
#                    )

#print(call.sid)
print(account_sid)
