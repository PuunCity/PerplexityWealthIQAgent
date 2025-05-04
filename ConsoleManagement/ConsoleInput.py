import time as t
import Caching.UserCache as UCache

introAnswer = ""
def Introduce(user):
    while True:
        introAnswer = input(str(">> ").lower())
        
        if introAnswer == "help":
            print("""
        Here is the list of commands: 
                
            help -> list of commands
            query -> start a new query search on selected assets with Perplexity
            fetch -> collect and display recent queries associated with the current account
            quit -> quit program
            
            (more to come!)
                """)
        elif introAnswer == "fetch":
            print("fetching user data!\n")
            print(UCache.Fetching(user))
        elif introAnswer == "query":
            print("let's get started!\n")
            break
        elif introAnswer == "quit":
            print("exiting program...")
            exit()
            break
        else:
            print("command not recognized. (Try \"help\" if you don't know what to type!)")


def Query():
    print("Hello user! This is WealthIQ, your AI-powered investing-related news reporter. \n")
    t.sleep(2)
    try:
        print("To get started, please start by typing in the assets (separated by a comma) you wish to be kept updated on: \n")
        defaultUserPrompt = input(str(">> "))
    except:
        print("Invalid input! Please specify what asset you would like to know about (XRP, Bitcoin, Etherum...)")
    t.sleep(2)
    return defaultUserPrompt

def outputAssets(assets):
    strippedAssets = assets.split(",")
    if len(strippedAssets) > 5:
        print("My apologies, but I would ask you to reduce the number of assets you would like to analyse to 5")
        restart()
    print("I've extracted all valid assets within my capabilities of analysis, do these assets sound right to you? \n")
    print(assets)
    response = input(str("Y/N\n")).lower()
    return response

def restart():
    print("let's try that again!\n")
    t.sleep(2)
    print("Please type in the assets (separated by a comma) you wish to be kept updated on:")
    defaultUserPrompt = input(str("Make sure to respect the following format: Asset#1, Asset#2, Asset#3, etc... \n"))
    return defaultUserPrompt

def separateAssets(assetsList, generatedAssets):
    assetsList = generatedAssets.split(",")
    return assetsList
        