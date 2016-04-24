from twilio.rest import TwilioRestClient

file = open('ACCSIDAPIKEY.txt', 'r')
ACCOUNT_SID= file.read()
file = open('AuthToken.txt', 'r')
AUTH_TOKEN= file.read()
file = open('TwilioNumber.txt', 'r')
FROM_NUM= file.read()


def send_Twilio( TO_NUM, MSG ):

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

	message = client.messages.create(
	    body = MSG,
	    to = FROM_NUM,
	    from_ = TO_NUM
	)
	print message
