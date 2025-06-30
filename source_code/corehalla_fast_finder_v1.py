# coding:utf-8
import webbrowser, threading, time, sys, subprocess
from libs import keyboard, pyperclip, pygetwindow, colored_terminal

colors = colored_terminal.Colors()

def start_brawl():
    webbrowser.open("steam://rungameid/291550")

def kill_brawl():
    subprocess.call(["taskkill", "/f", "/im", "Brawlhalla.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def game_is_executed():

    try:
        brawl = pygetwindow.getWindowsWithTitle("Brawlhalla")[0]

        if brawl:
            brawl.activate()

        sys.exit("\nExiting script...")

    except Exception:
        sys.exit("\nExiting script...")

def data_search(desired_url : str):

    print("\n")
    webbrowser.open_new_tab(desired_url)

def id_search(desired_url_id : str):

    while True:

        time.sleep(0.01)

        if keyboard.is_pressed("ctrl+c"):
            args_search = pyperclip.paste().strip()

            if args_search:

                if args_search.isdigit():

                    ids_text : str = "ID(s) Tested : {}{}{}".format(colors.GREEN, args_search, colors.RESET)

                    webbrowser.open_new_tab(desired_url_id.format(args_search))
                    time.sleep(2)
                
                else:
                    ids_text : str = "ID(s) Tested : {}{}{}".format(colors.RED, args_search, colors.RESET)
                    time.sleep(1)

                print(ids_text)
                    
        if keyboard.is_pressed("ctrl+q"):
            print("Exiting ID search...\n")
            break

def menu():

    while True :
        print("Welcome to fast corehalla finder {}v1{} \n\n------search options------\n\n(1) : Player search\n(2) : Clan search\n\n------Orther------\n\n(3) : Start game\n(4) : Script instructions\n(5) : Quit game\n(6) : Quit\n".format(colors.GREEN, colors.RESET))
        user_choice = input("-> ")

        if user_choice == "1":

            desired_name = input("\nBrawl player name : ")

            s1 = threading.Thread(target=data_search, args = ("https://corehalla.com/api/trpc/searchPlayerAlias?input=%7B%22alias%22%3A%22{}%22%2C%22page%22%3A%221%22%7D".format(desired_name),))
            s2 = threading.Thread(target=id_search, args=("https://corehalla.com/stats/player/{}",))

            s1.start()
            s2.start()

            s1.join()
            s2.join()

        elif user_choice == "2":

            desired_clan = input("\nBrawl clan name : ")

            s1 = threading.Thread(target=data_search, args = ("https://corehalla.com/api/trpc/getClansRankings?input=%7B%22name%22%3A%22{}%22%2C%22page%22%3A%221%22%7D".format(desired_clan),))
            s2 = threading.Thread(target=id_search, args = ("https://corehalla.com/stats/clan/{}",))

            s1.start()
            s2.start()

            s1.join()
            s2.join()
        
        elif user_choice == "3":
            print("\n")
            start_brawl()

        elif user_choice == "4":
            print("\n1 -- Select your module.\n2 -- Enter the name of a player or clan.\n3 -- Check intelligent printing in the web page.\n4 -- Search the players by mainAlias or otherAliases.\n5 -- Select the desired player or clan ID with your mouse and press CTRL + C.\n6 -- Once the player or clan is successfully found (or not), you can quit and restart the module by pressing CTRL + Q.\n")

        elif user_choice == "5":
            print("\n")
            kill_brawl()

        elif user_choice == "6":
            game_is_executed()

        else:
            print("\nPlease enter a valid choice XD\n")

menu()
