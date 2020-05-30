import requests
import platform
import time
import os
import json
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def timeout(secs):
    time.sleep(secs)

def clear():
    if platform.system()=='Windows':
        os.system('cls')
    else:
        os.system('clear')



low_risk_check = False
medium_risk_check = False
high_risk_check = False
unknow_risk_level = True

validStatus = 0 # 0 = null, 1 = Valid in-state, 2 = international unconfirmed.



chrome_options = Options()
chrome_options.add_argument("--headless")






def checkInternational ():
    if country_code != "+1":
        print("International code detected")
        validStatus = 2
    if country_code == "+1":
        print("Invalid Number")
        input("Press Enter to Exit...")
        quit("Invalid Number")


def getRiskLevel():
    if low_risk_check == True:
        print("[+] This number has a low Risk")

    #if medium_risk_check == True:
    #    print("[+] This number has a medium risk (Use caution)")

    if high_risk_check == True:
        print("[X] This number is High Risk")

    if unknow_risk_level == True:
        print("[Error] Unable to get risk level")






def write(validStatus):
    try:
        if validStatus == 1:
            f = open("PhoneTrace.txt", "a+")
            if country_code == "+1":
                f.write("\n\n\n\nName: " + name)
            else:
                f.write("\n\n\n")
            f.write("\n" + country_code +" "+ phone_number)
            f.write("\nNumber is Valid")
            f.write("\nCountry Prefix: " + country_prefix)
            f.write("\nCountry Code:" + country_code_out)
            f.write("\nCountry Name: " + country_name)
            f.write("\nCity: " + city)
            f.write("\nCarrier: " + carrier)
            f.write("\nLandlane or Mobile: " + cell_type)
        if validStatus != 0:
            if low_risk_check == True:
                f.write("\n[+]This number is low risk")

            if medium_risk_check == True:
                f.write("\n[]This number is medium risk")

            if high_risk_check == True:
                f.write("\n[X] This number is high risk")

            if unknow_risk_level == True:
                f.write("\n[Error] Unable to get risk level")
        timeout(1.5)
        f.close()
    except FileExistsError:
        print("FileExistsError occured - if you get this error please report it on my github")
        #fileOverwrite = input("File already exists, do you wish to overwrite? (Y/N): ")
        #if fileOverwrite == "y":
        #    os.remove("PhoneTrace.txt")
        #if fileOverwrite == "n":
        #    input("Press Enter to close...")








#intro
version = "1.4.1"
updateLoop = False
updateCounter = 0
clear()
print("Checking for updates...")

clear()
try:
    url = 'https://github.com/rshelver/Phone-Tracer/blob/master/Phone-Tracer.py'

    response = requests.get(url)
#print(response.content)
#print(response.text)

    if not(version in response.text):
        updateLoop = True
        while updateLoop == True:
            if updateCounter == 0:
                print("update reccomended")
                print("https://github.com/rshelver/Phone-Tracer")
                print("Update menu will close in 10 seconds")
                for i in range(10,0,-1):
                    print(i)
                    time.sleep(1)
                updateLoop = False
            else:
                pass

except:
    print("Requires internet to run...")
    print("Goodbye")
    timeout(2.2)
    quit()

clear()
print("Phone Tracer " + version)
print("Developed by Mutiny27")
print("Note: The name finder feature is in beta and may not provide fully accurate information")
# print("Note: The name finder feature may not be 100% accurate, In testing it's been found to be mostly accurate")
input("Press Enter to continue...")
clear()


#API START
try:
    f = open('PTracerAPI', 'r')
    for line in f:
        if "API: " in line:
            access_key = line[5:-1]
            break
    print("key: " + access_key)
except FileNotFoundError:
    TracerApi_Key = input('Enter your API key for Numverify: ')
    ChromeDriver74 = input("Enter the directory to ChromeDriver 74 or lower: ")
    with open('PTracerAPI', "w") as f:
        f.write("API: " + TracerApi_Key);
        f.write("\nchrome dir: " + ChromeDriver74)
        f.close()
        os.system("python3 Phone-Tracer.py")
        quit()

#ChromeDriver INIT
try:
    f = open("PTracerAPI", "r")
    for line in f:
        if "chrome dir:" in line:
            chromeDir = line[12:]
            print("ChromeDriver: " + chromeDir)
    driver = webdriver.Chrome(chromeDir,   options=chrome_options)
except FileNotFoundError:
    quit(8888)
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

    if "+1" == country_code:

        driver.get("https://www.spydialer.com/")
        number = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_SearchInputTextBox"]')

        submit = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_SearchImageButton"]')

        number.send_keys(phone_number)
        time.sleep(1)
        submit.click()
        time.sleep(5)
        secondSubmit = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_SearchCellImageButton"]')
        secondSubmit.click()

        nameSRC = driver.page_source
        name = "N/A"
        if "ctl00_ContentPlaceHolder1_NameLinkButton" in nameSRC:
            nameLoc = nameSRC.find('''href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$NameLinkButton','')">''')
            name = nameSRC[nameLoc:nameLoc + 140]
            name = name.replace('''href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$NameLinkButton','')">''',
                                "")
            name = name.replace("</a>", "")
            name = name.replace(" ", "-", 1)
            name = name.replace(" ", "", -1)
            name = name.replace("-", " ")


        # print("name:", name)
#    print(response.content)
#    valid_check = response.content[9:13]
#    print(valid_check)

    #check number

    valid_check=response.text[9:13]
    if valid_check=='true':
        valid_confirm_loop='valid'
        validStatus = 1
    elif valid_check!='true':
        checkInternational()


    #check scammer
    scamCheckURL = 'https://spamcalls.net/us-en/number/' + country_code + phone_number
    scamresponse = requests.get(scamCheckURL)
    if "spam risk is low<" in scamresponse.text:
        low_risk_check = True
        unknow_risk_level = False


    if "&rating=Probably+Spam" in scamresponse.text and low_risk_check == False:
        medium_risk_check = True
        low_risk_check = False
        unknow_risk_level = False


    if  "&rating=Spam" in scamresponse.text and low_risk_check == False:
        high_risk_check = True
        low_risk_check = False
        medium_risk_check = False
        unknow_risk_level = False


if main_menu_choice=='0':
    quit()

response_json = requests.get(url).json()
# response_json = json.loads(response.content)
country_prefix = response_json.get('country_prefix', "")
country_code_out = response_json.get('country_code', "")
country_name = response_json.get('country_name', "")
city = response_json.get('location', "")
carrier = response_json.get('carrier', "")
cell_type = response_json.get('line_type', "")





if "Sprint" in carrier:
    carrier = "Tmobile"



if valid_confirm_loop=='valid':
    clear()
    if country_code == "+1":
        print("Name:", name)
    else:
        print("Name: not yet supported for international numbers")
    print(country_code+ " " + phone_number)
    print('Number is Valid')
    print('Country Prefix: ' + country_prefix)
    print('Country code: ' + country_code_out)
    print('Country Name: ' + country_name)
    print("City: " + city)
    print("Carrier: " + carrier)
    print("Landlane or Mobile: " + cell_type)
    getRiskLevel()



    save = input("Would you like this saved to a file? (Y/N): ")

    if save == "y":
        write(validStatus)