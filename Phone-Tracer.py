import requests
import platform
import time
import os
import json


from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H%m")







def timeout(secs):
    time.sleep(secs)

def clear():
    if platform.system()=='Windows':
        os.system('cls')
    else:
        os.system('clear')





#intro
print("Phone Tracer 1.1")
print("Developed by Mutiny27")
timeout(1.5)
clear()

#API START
try:
    f = open('PTracerAPI', 'r')
    access_key = f.read()
except FileNotFoundError:
    TracerApi_Key = input('Enter your API key for Numverify: ')
    with open('PTracerAPI', "w") as f:
        f.write(TracerApi_Key);
        f.close()

#main menu
clear()
print('Phone Tracer')
print('[1] Trace Phone Number')
print('[0] Quit')
main_menu_choice=input('Enter one of the options: ')
clear()


if main_menu_choice=='1':


    phone_number=input('Enter the Phone Number you wish to trace: ')
    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_number
    response = requests.get(url)
#    print(response.content)
#    valid_check = response.content[9:13]
#    print(valid_check)

    #check number
    valid_check=response.text[9:13]
    if valid_check=='true':
        valid_confirm_loop='valid'
    elif valid_check!='true':
        print("Number is Invalid")
        input("Press Enter to Continue...")


response_json = json.loads(response.content)
country_prefix = response_json.get('country_prefix', "")
country_code = response_json.get('country_code', "")
country_name = response_json.get('country_name', "")
city = response_json.get('location', "")
carrier = response_json.get('carrier', "")
cell_type = response_json.get('line_type', "")



if valid_confirm_loop=='valid':
    clear()
    print(phone_number)
    print('Number is Valid')
    print('Country Prefix: ' + country_prefix)
    print('Country code: ' + country_code)
    print('Country Name: ' + country_name)
    print("City: " + city)
    print("Carrier: " + carrier)
    print("Landlane or Mobile: " + cell_type)
    save = input("Would you like this saved to a file? (Y/N): ")

    if save == "y":
        try:
            f = open("PhoneTrace"+city+country_code+".txt", "w+")
            f.write(phone_number)
            f.write("\nNumber is Valid")
            f.write("\nCountry Prefix: " + country_prefix)
            f.write("\nCountry Code:" + country_code)
            f.write("\nCountry Name: " + country_name)
            f.write("\nCity: " + city)
            f.write("\nCarrier: " + carrier)
            f.write("\nLandlane or Mobile: " + cell_type)
            timeout(1.5)
            f.close()
        except FileExistsError:
            print("You've already scanned this number, no need to save it")





if main_menu_choice=='0':
    quit()