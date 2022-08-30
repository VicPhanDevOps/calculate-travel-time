#!/bin/python

# calculate profit

# you can run this script with: python3 calculateTotalProfitInPython.py < total sale > < profit margin > 

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32":
        print(Fore.GREEN + "Operating System: ")
        print(os.system('ver'))
        print(Style.RESET_ALL)
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('sw_vers'))
        print(Style.RESET_ALL)
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('uname -r'))
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem


def getTotalSale(operatingSystem): 
    if operatingSystem == "Windows": 
        totalSale = float(input("Please type the total sale amount and press \"Enter\" key (Example: 100): "))

        print("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        totalSale = float(input("Please type the total sale amount and press \"return\" key (Example: 100): "))

        print("")

    return totalSale


def getProfitMargin(operatingSystem): 
    if operatingSystem == "Windows": 
        profitMargin = float(input("Please type the profit margin and press \"Enter\" key (Example: 20): "))

        print("")

    if operatingSystem == "macOS" or operatingSystem == "Linux": 
        profitMargin = float(input("Please type the profit margin and press \"Enter\" key (Example: 20): "))

        print("")

    return profitMargin

        
def checkParameters(totalSale, profitMargin): 
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    valid = "true"

    print("Parameters:")
    print("--------------------------------------")
    print("totalSale   : {0}".format(totalSale))
    print("profitMargin: {0}".format(profitMargin))
    print("--------------------------------------")

    if totalSale == None: 
        print(Fore.RED + "totalSale is not set." + Style.RESET_ALL)
        valid = "false"

    if profitMargin == None: 
        print(Fore.RED + "profitMargin is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "One or more parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")


def calculateTotalProfit(): 
    print("\nCalcuate total profit in Python.\n\n")
    operatingSystem = checkOs()

    if len(sys.argv) > 2: 
        totalSale    = float(sys.argv[1])
        profitMargin = float(sys.argv[2])

    else: 
        totalSale    = getTotalSale(operatingSystem)
        profitMargin = getProfitMargin(operatingSystem)

    checkParameters(totalSale, profitMargin)

    try: 
        startDateTime = datetime.now()
        
        print("Started calculating total profit at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))
        
        totalProfit = totalSale * (profitMargin/100)
        
        print(Fore.BLUE + "Total profit from total sale of ${0} with {1}% profit margin is ${2}".format(totalSale, profitMargin, totalProfit) + Style.RESET_ALL)

        print(Fore.GREEN + "Successfully calculated total profit." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished calculated total profit at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} seconds".format(duration.seconds))
        print("")
        
    except Exception as e:
        print(Fore.RED + "Failed to calculate total profit in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


calculateTotalProfit()
