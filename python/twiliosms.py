from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException

file = open('ACCSIDAPIKEY.txt', 'r')
ACCOUNT_SID= file.read()
file = open('AuthToken.txt', 'r')
AUTH_TOKEN= file.read()
file = open('TwilioNumber.txt', 'r')
FROM_NUM= file.read()


def send_Twilio( TO_NUM, MSG ):
	print "What up"
        print ACCOUNT_SID, AUTH_TOKEN
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        try:
	    message = client.messages.create(
	        to = '+17177468642', #TO_NUM,
	        from_ = '+18622563399',#FROM_NUM,
                body = 'LOL'
	    )
	    print message
        except TwilioRestException as e:
            print e
