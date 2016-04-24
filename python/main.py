from Naked.toolshed.shell import execute_js
from temp_check import get_temp
from uv_check import get_uv
from twiliosms import send_Twilio
from air_check import get_quality

def main():
    phone_number = '+17177468642' 
    #phone_number = raw_input("Enter phone number: ")
    #gps_success = execute_js('main.js')

    #while True:
        uv_index = get_uv()
        temp = get_temp()
        airq = get_quality()
        print airq

        # if gps_success:
        #     print "GPS Success"
        file = open('lat', 'r')
        lat = file.read()
        file = open('long', 'r')
        lon = file.read()
        msg = "({0}, {1})".format(lat, lon)
        msg += 'Temp: {0}  UV: {1} Air Quality: {2}'.format(temp, uv_index, airq)

            send_Twilio(phone_number, msg)
        #else:
        #    break # nothing?

main()
