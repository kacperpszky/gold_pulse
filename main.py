from connect import make_request, getData, internet_on
import os, time

CYELL = '\033[33m'
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\033[92m'

date = input("Data from a specific day (enter date *[....-..-..]* (y-m-d)) / skip the question (click Enter) \n")
if len(str(date)) > 2:
    date = str(date).replace('-','')
if internet_on():
    make_request("/" + date)
    for x in range(3):
        for z in range (1, 4):
            match z:
                case 1:
                    print(CYELL + "Requesting information of XAU price." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
                case 2:
                    print(CYELL + "Requesting information of XAU price.." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
                case 3:
                    print(CYELL + "Requesting information of XAU price..." + CEND)
                    time.sleep(0.5)
                    os.system('cls')
                    
    print(CYELL + "Requesting information of XAU price..." + CEND)
    if getData("error") == 0:
        print(CGREEN + "Request successful" + CEND)
    else:
        print(CRED + "No data available for this date or pair." + CEND)
    
    time.sleep(3)
    os.system('cls')

else:
    print(CRED + "Something's wrong with the internet!" + CEND)









