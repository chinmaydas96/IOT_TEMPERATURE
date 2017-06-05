from twilio.rest import TwilioRestClient

account_sid = "AC8fafcce72877db5b3fd75c7a8823a234"
auth_token = "b53ef0f09772118c67e9be369b599ace"

client = TwilioRestClient(account_sid, auth_token)


def send(to_no):
    message = client.sms.messages.create(
        body="who are you",
        to=to_no,
        # to="+919778428629",
        from_="+12512201581")
    print message.sid


send("+919778428629")
