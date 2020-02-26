import requests
import platform
import time
import os
import json
import webbrowser


from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H%m")

low_risk_check = False
medium_risk_check = False
high_risk_check = False
unknow_risk_level = True






def timeout(secs):
    time.sleep(secs)

def clear():
    if platform.system()=='Windows':
        os.system('cls')
    else:
        os.system('clear')





#intro
print("Phone Tracer 1.2")
print("Developed by Mutiny27")
print("Note: The spam caller feature is in beta and may not provide fully accurate information")
print("Press Enter to continue...")
input()
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

    country_code=input('Please enter the country code the number you want to track (Include "+"): ')
    phone_number=input('Enter the Phone Number you wish to trace: ')
    url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + country_code + phone_number
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


    #check scammer
    scamCheckURL = 'https://spamcalls.net/us-en/search?q=%2B' + country_code + phone_number
    scamresponse = requests.get(scamCheckURL)
    if "spam risk is low<" in scamresponse.text:
        low_risk_check = True
        unknow_risk_level = False


    #if "Neutral" in scamresponse.text and low_risk_check == False:
    #    medium_risk_check = True
    #    low_risk_check = False
    #    unknow_risk_level = False


    if  "Scam Call:" in scamresponse.text and low_risk_check == False:
        high_risk_check = True
        low_risk_check = False
        medium_risk_check = False
        unknow_risk_level = False




response_json = json.loads(response.content)
country_prefix = response_json.get('country_prefix', "")
country_code_out = response_json.get('country_code', "")
country_name = response_json.get('country_name', "")
city = response_json.get('location', "")
carrier = response_json.get('carrier', "")
cell_type = response_json.get('line_type', "")





if valid_confirm_loop=='valid':
    clear()
    print(country_code+ " " + phone_number)
    print('Number is Valid')
    print('Country Prefix: ' + country_prefix)
    print('Country code: ' + country_code_out)
    print('Country Name: ' + country_name)
    print("City: " + city)
    print("Carrier: " + carrier)
    print("Landlane or Mobile: " + cell_type)
    if low_risk_check == True:
        print("[+] This number has a low Risk")

    if medium_risk_check == True:
        print("[+] This number has a medium risk (Use caution)")

    if high_risk_check == True:
        print("[+] This number is Risky")

    if unknow_risk_level == True:
        print("[X] Unable to get risk level")



    save = input("Would you like this saved to a file? (Y/N): ")

    if save == "y":
        try:
            f = open("PhoneTrace"+city+country_code+".txt", "w+")
            f.write(country_code+phone_number)
            f.write("\nNumber is Valid")
            f.write("\nCountry Prefix: " + country_prefix)
            f.write("\nCountry Code:" + country_code_out)
            f.write("\nCountry Name: " + country_name)
            f.write("\nCity: " + city)
            f.write("\nCarrier: " + carrier)
            f.write("\nLandlane or Mobile: " + cell_type)
            if low_risk_check == True:
                f.write("\n[+]This number is low risk")

            if medium_risk_check == True:
                f.write("\n[]This number is medium risk")

            if high_risk_check == True:
                f.write("\nThis number is high risk")

            if unknow_risk_level == True:
                f.write("\n[X] Unable to get risk level")
            timeout(1.5)
            f.close()
        except FileExistsError:
            print("You've already scanned this number, no need to save it")





if main_menu_choice=='0':
    quit()