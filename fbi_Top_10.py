import requests
import json
import time

# This program is used to show the top ten wanted list from the Federal Bureau of Investigation
# The API provided was from the FBI. API is a mess and not properly formatted, but is possible to get through
# Not sure if regularlly updated but this V1 testing
# Programmed by Tristan Prater of TrisC0. 
response = requests.get('https://api.fbi.gov/wanted/v1/list')
data = json.loads(response.content)




def Intro(): 
    print("Welcome to the FBI Wanted Data Base.")
    time.sleep(2.4)
    print("We are here to provide you with knowledgeable information from the FBI")
    time.sleep(8)
    print("Please enjoy, and use this info wisely.")
    time.sleep(5)
    _main_()







# The FBI Tops Tens listed with name, details, and description. 

# Number 10
wanted10 = data['items'][0]
wanted10Name = wanted10['title']
wanted10Desc = wanted10['description']
wanted10Reasion = wanted10['caution']
wanted10Detail = wanted10['details']
if wanted10Detail == None:
    wanted10Detail = " "
# Number 9 
wanted9 = data['items'][1]
wanted9Name = wanted9['title']
wanted9Desc = wanted9['description']
wanted9Detail = wanted9['details']
if wanted9Detail == None:
    wanted9Detail = " "
# Number 8

wanted8 = data['items'][2]
wanted8Name = wanted8['title']
wanted8Detail =  wanted8['details']
wanted8Desc = wanted8['description']
if wanted8Detail == None:
    wanted8Detail = " "
# Number 7
wanted7 = data['items'][3]
wanted7Name = wanted7['title']
wanted7Detail = wanted7['details']
wanted7Desc = wanted7['description']
if wanted7Detail == None:
    wanted7Detail = " "
# Number 6
wanted6 = data['items'][4]
wanted6Name = wanted6['title']
wanted6Detail = wanted6['details']
wanted6Desc = wanted6['description']
if wanted6Detail == None:
    wanted6Detail = " "
# Number 5
wanted5 = data['items'][5]
wanted5Name = wanted5['title']
wanted5Detail = wanted5['details']
wanted5Desc = wanted5['description']
if wanted5Detail == None:
    wanted5Detail = " "
# Number 4
wanted4 = data['items'][6]
wanted4Name = wanted4['title']
wanted4Detail = wanted4['details']
wanted4Desc = wanted4['description']
if wanted4Detail == None:
    wanted4Detail = " "
# Number 3
wanted3 = data['items'][7]
wanted3Name = wanted3['title']
wanted3Detail = wanted3['details']
wanted3Desc = wanted3['description']
if wanted3Detail == None:
    wanted3Detail = " "
# Number 2
wanted2 = data['items'][8]
wanted2Name = wanted2['title']
wanted2Detail = wanted2['details']
wanted2Desc = wanted2['description']
if wanted2Detail == None:
    wanted2Detail = " "
# Number 1
wanted1 = data['items'][9]
wanted1Name = wanted1['title']
wanted1Detail = wanted1['details']
wanted1Desc = wanted1['description']
if wanted1Detail == None:
    wanted1Detail = " "

def _main_():

    choice = input(
    "[1]\n[2]\n[3]\n[4]\n[5]\n[6]\n[7]\n[8]\n[9]\n[10] \n  Please choose which case you would like to inspect. ")

    userChose = str(choice)
 

    if userChose == "1": 
        print("The name of this case file " + wanted1Name)
        print("The details of the wanted case is " + wanted1Detail)
        print("The Description of the case is " + wanted1Desc)
    if userChose == "2": 
        print("The name of this case file " + wanted2Name)
        print("The details of the wanted case is " + wanted2Detail)
        print("The Description of the case is " + wanted2Desc)
    if userChose == "3": 
        print("The name of this case file " + wanted3Name)
        print("The details of the wanted case is " + wanted3Detail)
        print("The Description of the case is " + wanted3Desc)
    if userChose == "4": 
        print("The name of this case file " + wanted4Name)
        print("The details of the wanted case is " + wanted4Detail)
        print("The Description of the case is " + wanted4Desc)
    if userChose == "5": 
        print("The name of this case file " + wanted5Name)
        print("The details of the wanted case is " + wanted5Detail)
        print("The Description of the case is " + wanted5Desc)
    if userChose == "6": 
        print("The name of this case file " + wanted6Name)
        print("The details of the wanted case is " + wanted6Detail)
        print("The Description of the case is " + wanted6Desc)
    if userChose == "7": 
        print("The name of this case file " + wanted7Name)
        print("The details of the wanted case is " + wanted7Detail)
        print("The Description of the case is " + wanted7Desc)
    if userChose == "8": 
        print("The name of this case file " + wanted8Name)
        print("The details of the wanted case is " + wanted8Detail)
        print("The Description of the case is " + wanted8Desc)
    if userChose == "9": 
        print("The name of this case file " + wanted9Name)
        print("The details of the wanted case is " + wanted9Detail)
        print("The Description of the case is " + wanted9Desc)
    if userChose == "10": 
        print("The name of this case file is " + wanted10Name)
        print("The details of the wanted case is " + wanted10Detail)
        print("The Description of the case is " + wanted10Desc)
    time.sleep(4.0)
    again = input("Want to continute to look? (y/n) ")

    if again == "y":
        _main_()
    else: 
        print("Thank you. ")
Intro()


