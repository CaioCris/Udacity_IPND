from twilio.rest import TwilioRestClient

account_sid = "AC85b3477e0d839e4df5a3d35d4f47795d" # Your Account SID from www.twilio.com/console
auth_token  = "b7fca03798987aafd5a4042a320b20d7"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Seu Otario, me manda uma msg no whats se você recebeu isso! #mimacher #descubra",
    to="+12489741982",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)