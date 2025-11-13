from twilio.rest import Client
account_sid = 'ACf406727a206dc4d93a0ce33f9fa7a658'
auth_token = 'c23931ffd9b2e2325426b18eaa4ac292'
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='MGebd0f20ff85f052cfacfd54817e20405',
  body='Ahoy 👋',
  to='+18777804236'
)
print(message.sid)