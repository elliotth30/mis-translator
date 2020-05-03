# Importing repositries
import time # - Imports the ability to pause the application for specified time.
import random # - Imports the ability to randomly generate numbers.
import csv # - Importing the ability to read & write CSV data files.
import os # - Within MacOS this function clears the terminal.
import googletrans # - Imports the Google Translate API.
from googletrans import Translator # - Imports the translate function from the API.
import sys # - Imports the ability to stop the program.

# Importing routine file
raw_csv_data = open('lang_list.csv') #importing the data raw
read_csv_data = csv.reader(raw_csv_data) #reading the data raw
row = list(read_csv_data) #creating each data row
row_count = len(row) -1 #the total number of rows in the list

# Languages Supported by Google Translate
#https://en.wikipedia.org/wiki/Google_Translate

# Routine To generate random language (imported from CSV file).
random_lang = random.randint(1, row_count)
string_row = str(row[random_lang])[2:-2]
#print(string_row)

#Main Menu  - Sets the program language and constant variables.
time.sleep(1) # - This pauses the program for (number) of seconds. 
os.system('clear') # - Within MacOS this function clears the terminal.
menu_lang = "English"
src_lang = "english"
x = 0
max_number = 100
tts_status = "OFF"
import_stat = "API NOT IMPORTED"
tts_status_check = 0

#Print New Line - prints a new line.
def newline():
    print("")

#Debug Readout - Language data set spotter; prints unreadable language and hold the variable.
def Debug_error():
    translation = "Error Debug"
    print("######################")
    print("Debug Error Language -", current_lang)
    print("######################")
    breakpoint

def help():
    print("######################")
    print("help Menu")
    print("######################")
    newline()
    os.system('clear') # - Within MacOS this function clears the terminal.
    print("This translator allows you to write an input; example (What's for dinner?)")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("It will then take your message, and translate it again and again,")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("through multiple languages back to back.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    newline()
    print("[ English ] how much is it for a beer, please?")
    time.sleep(2) # - This pauses the program for (number) of seconds.
    newline()
    print("[ Urdu ]   ->  کتنا براہ مہربانی ایک بیر کے لئے یہ ہے؟")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("[ Malayalam ]   ->  എത്ര ഒരു ബിയർ, ദയവായി?")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("[ Maltese ]   ->  Kemm għal birra, jekk jogħġbok?")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    newline()
    print("Then returning it back to the orginal language.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    newline()
    print("[ English ]  Whether for beer, please?")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    newline()
    newline()
    input("Press 1 at the main menu to try! Have fun.")

def credit():
    os.system('clear') # - Within MacOS this function clears the terminal.
    print("The Sh*t Traslator Bot!")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("Designed & Programmed By Elliott C Hall")
    newline()
    time.sleep(2) # - This pauses the program for (number) of seconds.
    print("[Website] - www.elliotthall.co.uk")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("[Social] - @elliotth30")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("[Email] - hello@elliotthall.co.uk")
    time.sleep(3) # - This pauses the program for (number) of seconds.
    newline()
    newline()
    print("Further thank you for the following repositories and API's:")
    newline()
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("import time # - Imports the ability to pause the application for specified time.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("import random # - Imports the ability to randomly generate numbers.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("import csv # - Importing the ability to read & write CSV data files.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("import os # - Within MacOS this function clears the terminal.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("import googletrans # - Imports the Google Translate API.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("from googletrans import Translator # - Imports the translate function from the API.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("import sys # - Imports the ability to stop the program.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("import google_speech # - Allows text to be read by Google Cloud Services")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    print("from google_speech import Speech # - Imports the Speech function from the API.")
    time.sleep(1) # - This pauses the program for (number) of seconds.
    newline()
    input("Press Enter to return to menu.")

def menu():
    global import_stat
    while True:
        menu_select = 0
        os.system('clear') # - Within MacOS this function clears the terminal.
        print("Welcome to the Sh*t Traslator Bot!")
        print("")
        print("1. New translation")
        print("2. Help")
        print("3. Credits")
        print("")
        print("4. Exit")
        print("")
        menu_select = input("Please select a menu item: ")
        if menu_select == "1":
            os.system('clear') # - Within MacOS this function clears the terminal.
            break
        elif menu_select == "2":
            help()
            menu()
            break
        elif menu_select == "3":
            credit()
            menu()
            break
        elif menu_select == "4":
            os.system('clear') # - Within MacOS this function clears the terminal.
            print("User closed application")
            sys.exit("")
            print("DEBUG - SYS.EXIT should have initiated.")
            menu()
            break
        elif menu_select == "debug":
            os.system('clear') # - Within MacOS this function clears the terminal.
            debug_menu()
            menu()
            break
        else:
            os.system('clear') # - Within MacOS this function clears the terminal.
            print("Please enter a valid menu item. Use the numbers!")
            time.sleep(3) # - This pauses the program for (number) of seconds. 
            menu()
        break

def debug_menu():
    menu_select = 0
    global tts_status
    os.system('clear') # - Within MacOS this function clears the terminal.
    print("######################")
    print("Debug Menu")
    print("######################")
    print("")
    print("1. Text-to-speach (", tts_status, ")")
    print("")
    menu_select = input("Please select a menu item: ")
    if menu_select == "1":
        os.system('clear') # - Within MacOS this function clears the terminal.
        tts_status = input("Please set the new state to ON or OFF: ")
        if tts_status == "ON":
            os.system('clear') # - Within MacOS this function clears the terminal.
            print("This change has successfully been updated!")
            newline()
            print("New staus (", tts_status, ")")
            time.sleep(3) # - This pauses the program for (number) of seconds.
            pass
        elif tts_status == "OFF":
            os.system('clear') # - Within MacOS this function clears the terminal.
            print("This change has successfully been updated!")
            newline()
            print("New staus (", tts_status, ")")
            time.sleep(3) # - This pauses the program for (number) of seconds.
        else:
            try:
                os.system('clear') # - Within MacOS this function clears the terminal.
                print("Change not saved!")
                print("")
                print("error - please set the state to either OFF or ON.")
                tts_status = "OFF"
                time.sleep(3) # - This pauses the program for (number) of seconds.
                debug_menu()
            except ValueError: # - Debug: commonly caused by unreadable/supported language.
                os.system('clear') # - Within MacOS this function clears the terminal.
                print("Change not saved!")
                print("")
                print("error - please set the state to either OFF or ON.")
                tts_status = "OFF"
                time.sleep(3) # - This pauses the program for (number) of seconds.
    else:
        pass

while True: # - Main Menu
    menu()
    if tts_status == "ON":
        if tts_status_check == 0:
            tts_status_check = 1
            import_stat = "SPEECH API - IMPORT COMPLETE"
            print(import_stat)
            import google_speech
            from google_speech import Speech
            time.sleep(3) # - This pauses the program for (number) of seconds. 
            os.system('clear') # - Within MacOS this function clears the terminal.
        else:
            pass
    else:
        pass
    #Input Menu - Allows the user to input text for translation and the number of times it's cycled.
    translator = Translator()
    text_input = input("What is your text to be translated: ")
    if text_input == "debug": # - Checks for debug command to close program
        sys.exit("Debug Error - Closing Program")
    else:
        pass
    while True: # - checks the user has entered an intiger and below the max set limit.
        try:
            os.system('clear') # - Within MacOS this function clears the terminal.
            no_lang = int(input("How many languages do you want it to pass through?: "))
        except ValueError:
            os.system('clear') # - Within MacOS this function clears the terminal.
            print("Please enter a valid numerical number. (i.e 1,2,3..)")
        else:
            if no_lang > max_number:
                os.system('clear') # - Within MacOS this function clears the terminal.
                print("Please enter a number less than", max_number)
                breakpoint
            else:
                break

    print("")
    print("[", menu_lang, "]", text_input,)
    print("")

    while x != int(no_lang): # - Loops untill number of pass-throughs are completed.
        random_lang = random.randint(1, row_count) # - Pick a random language from the dataset.
        current_lang = str(row[random_lang])[2:-2] # - Removes CSV formatting.
        try: # - This checks that the previous language isn't the same as the next.
            translation = translator.translate(text_input, src = str(src_lang), dest=current_lang)
            if src_lang == current_lang:
                breakpoint
            else: 
                #print("[", current_lang, "] ", translation.origin, ' -> ', translation.text,)
                print("[", current_lang, "] ", ' -> ', translation.text,)
                src_lang = current_lang
                text_input = translation.text
                x = x + 1
        except ValueError: # - Debug: commonly caused by unreadable/supported language.
            Debug_error()
    # Return to Host Language
    try:
        translation = translator.translate(text_input, src = str(src_lang), dest=menu_lang)
        print("")
        print("[", menu_lang, "] ", translation.text,)
        src_lang = current_lang
        text_input = translation.text
        if tts_status == "ON":
            try:
                translation_speech = Speech(str(text_input), "en")
                translation_speech.play()
            except ValueError: # - Debug: commonly caused by unreadable/supported language.
                menu_lang = "Audio Import Error - Check SOX directory import"
                Debug_error()
        else:
            pass
    except ValueError: # - Debug: commonly caused by unreadable/supported language.
        Debug_error()

    print("")
    input("Press Enter to return to menu.")
    x = 0
# text_morn = (good_morning + final_total_time)
