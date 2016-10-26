from twilio.rest import TwilioRestClient

account_sid = "AC305cc4ce9d61420f657f5f30b052fb8e" # Your Account SID from www.twilio.com/console
auth_token  = "{{ auth_token }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+12345678901",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)