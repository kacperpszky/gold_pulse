from connect import make_request, getData, internet_on, connectDB
from database_save import createTable, addValues, getSimpleData, getPenultimate
from menu import print_menu
import os, time
import datetime

CYELL = '\033[33m'
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\033[92m'
CBLUE = '\033[34m'

REQUEST = False

print_menu()

date = input(" " + "Data from a specific day (enter date *[....-..-..]* (y-m-d)) / skip the question (click Enter) \n")
time.sleep(1)
os.system('cls')
if len(str(date)) > 2:
    date = str(date).replace('-','')
if internet_on():
    make_request("/" + date)
    
    for x in range(3):
        for z in range (1, 4):
            match z:
                case 1:
                    print_menu()
                    print(CBLUE + " " + "Connecting do Database." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
                case 2:
                    print_menu()
                    print(CBLUE + " " + "Connecting do Database.." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
                case 3:
                    print_menu()
                    print(CBLUE + " " + "Connecting do Database..." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
    print_menu()                
    print(CBLUE + " " + "Connecting do Database..." + CEND)
    if connectDB():
        print(CGREEN + " " + "Connected do Database." + CEND)
        createTable()
        time.sleep(2)
    else:
        print(CRED + " " + "No connection to the database has been established, data will not be saved." + CEND)
    
    for x in range(3):
        for z in range (1, 4):
            match z:
                case 1:
                    print(CYELL + " " + "Requesting information of XAU price." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
                    print_menu()
                case 2:
                    print(CYELL + " " + "Requesting information of XAU price.." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
                    print_menu()
                case 3:
                    print(CYELL + " " + "Requesting information of XAU price..." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
                    print_menu()
                    
    print(CYELL + " " + "Requesting information of XAU price..." + CEND)
    if getData("error") == 0:
        print(CGREEN + " " + "Request successful" + CEND)
        REQUEST = True
    else:
        print(CRED + " " + "No data available for this date or pair." + CEND)
    
    time.sleep(3)
    os.system('cls')
    print_menu()
else:
    print(CRED + " " + "Something's wrong with the internet!" + CEND)
    REQUEST = False
    
if REQUEST:
    addValues(str(getData('metal')), float(getData('price')), float(getData('low_price')), float(getData('high_price')), float(getData('chp')), str(getData('date')))
    print(CGREEN + " " + "Data saved to Database." + CEND)
    time.sleep(2)
    os.system('cls')
    print_menu()



if len(date) > 2:
    print(" " + CYELL + "Current gold price status and key information at " + date + CEND)
else:
    print(" " + CYELL + "Current gold price status and key information at " + str(datetime.datetime.now().strftime("%x")) + CEND)
print(" " + getSimpleData("name") + " Price: \t \t" + getSimpleData("price"))

#high_price
if float(getPenultimate("high_price")) > float(getSimpleData("high_price")):
    print(" " + getSimpleData("name") + " High price: \t" + CRED + getSimpleData("high_price") + CEND + " <-- " + CGREEN + getPenultimate("high_price") + CEND + " [last saved data]")
else:
    print(" " + getSimpleData("name") + " High price: \t" + CGREEN + getSimpleData("high_price") + CEND + " <-- " + CRED + getPenultimate("high_price") + CEND + " [last saved data]")

# low_price
if float(getPenultimate("low_price")) > float(getSimpleData("low_price")):
    print(" " + getSimpleData("name") + " Low price: \t" + CRED + getSimpleData("low_price") + CEND + " <-- " + CGREEN + getPenultimate("low_price") + CEND + " [last saved data]")
else:
    print(" " + getSimpleData("name") + " Low price: \t" + CGREEN + getSimpleData("low_price") + CEND + " <-- " + CRED + getPenultimate("low_price") + CEND + " [last saved data]")    
    
#chp
if float(getPenultimate("chp")) > float(getSimpleData("chp")):
    print(" " + getSimpleData("name") + " CHP: \t \t" + CRED + getSimpleData("chp") + CEND + " <-- " + CGREEN + getPenultimate("chp") + CEND + " [last saved data]")
else:
    print(" " + getSimpleData("name") + " CHP: \t \t" + CGREEN + getSimpleData("chp") + CEND + " \t <-- " + CRED + getPenultimate("chp") + CEND + " [last saved data]")    
    
    

    
    
    











