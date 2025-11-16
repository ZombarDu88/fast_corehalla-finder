# coding:utf-8
import webbrowser, threading, time, sys, subprocess
from libs import colored_terminal

colors = colored_terminal.Colors()

#necessary libs for the good script execution
required_libs = ['keyboard', 'pyperclip', 'pygetwindow', 'pypresence']
missing_libs = []

for lib in required_libs:

    try:
        # try -> import keyboard, pyperclip, pygetwindow
        __import__(lib) 

    except ModuleNotFoundError:
        missing_libs.append(lib)

if missing_libs:
    print("{}Necessary libs are missing: {}{}\n{}Installing missing libraries...{}\n".format(colors.RED, ", ".join(missing_libs), colors.RESET, colors.YELLOW, colors.RESET))

    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_libs)
        print("\n{}Successfully installed missing libs =){}\n".format(colors.GREEN, colors.RESET))

    except subprocess.CalledProcessError:
        print("{}Error: Failed to install libraries. Please install manually: pip install {}{}".format(colors.RED, " ".join(missing_libs), colors.RESET))
        sys.exit(1)
        

# securised import after verification
import keyboard, pyperclip, pygetwindow
from libs import rich_presence

discord = rich_presence.discord_rpc()
discord.connect()

'''
launch via steam in local host =)
291550 = brawl steam id : https://steamdb.info/app/291550/
'''

def start_brawl():
    webbrowser.open("steam://rungameid/291550")

'''
kill the process by name Brawlhalla.exe in that case
'''

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
    webbrowser.open_new_tab(desired_url)

def id_search_event(desired_url_id: str):
    stop_event = threading.Event()

    def id_search():
            
            time.sleep(0.1) # 100 millisecondes
            args_search = pyperclip.paste().strip()

            if args_search:

                if args_search.isdigit():

                    ids_text : str = "ID(s) Tested : {}{}{} is a correct id {}(Double check the copied id at the web page if you find a orther player or clan){}".format(colors.GREEN, args_search, colors.RESET, colors.YELLOW, colors.RESET)
                    
                    webbrowser.open_new_tab(desired_url_id.format(args_search))
                    time.sleep(2)

                else:
                    ids_text : str = "ID(s) Tested : {}{}{} is not a correct id XD".format(colors.RED, args_search, colors.RESET)

                print(ids_text)

    def stop_search():
        print("{}"
              "\n\nExiting ID search..."
              "\n"
              .format("-"*50))
        
        stop_event.set()

    # hotkeys
    keyboard.add_hotkey("ctrl+c", id_search)
    keyboard.add_hotkey("ctrl+q", stop_search)

    print("\n(CTRL+C) to paste and find player by {}Id{}, (CTRL+Q) to {}Quit{} or {}Retry{} :"
          "\n\n{}".format(colors.GREEN, colors.RESET, colors.RED, colors.RESET, colors.YELLOW, colors.RESET, "-"*50))

    stop_event.wait()

    keyboard.remove_hotkey("ctrl+c")
    keyboard.remove_hotkey("ctrl+q")

def memo_search_result():
    print("\n{}Fast memo :"
          "\n\nWarning : Before this comments just try refresh the differents wep pages =)"
          "\n\nNo player found = {}"
          "\n\nPoopy corehalla server = {}"
          "\n\nLong waiting display ? = poopy corehalla server x2 XD"
          "\n\nCheck pretty-print checkbox option for more easier search"
          "{}"
          .format(colors.YELLOW, '{"result":{"data":[]}}', '{"error":{"message":"canceling statement due to statement timeout","code":-x,"data":{"code":"INTERNAL_SERVER_ERROR","httpStatus":500,"path":"searchPlayerAlias or getClansRankings"}}}', colors.RESET))

def update_status_async(status_msg):
    threading.Thread(target=discord.update_status, args=(status_msg,)).start()

def menu():

    while True :

        update_status_async("Status : Main menu...")

        print("Welcome to fast corehalla finder {}v1{}"
              "\n\n------Search options------"
              "\n(1) : Player search"
              "\n(2) : Clan search"
              "\n\n------Other------"
              "\n(3) : Start game"
              "\n(4) : Script instructions"
              "\n(5) : Quit game"
              "\n(6) : Quit"
              "\n".format(colors.GREEN, colors.RESET))
        
        user_choice = input("-> ")

        if user_choice == "1":

            update_status_async("Status : Players searching...")
            memo_search_result()

            desired_name = input("\nBrawl player name : ")

            update_status_async("Status : Search [{}] player info...".format(desired_name))

            s1 = threading.Thread(target=data_search, args = ("https://corehalla.com/api/trpc/searchPlayerAlias?input=%7B%22alias%22%3A%22{}%22%2C%22page%22%3A%221%22%7D".format(desired_name),))
            s2 = threading.Thread(target=id_search_event, args=("https://corehalla.com/stats/player/{}",))

            s1.start()
            s2.start()
            s1.join()
            s2.join()

        elif user_choice == "2":

            update_status_async("Status : Clan searching...")
            memo_search_result()

            desired_clan = input("\nBrawl clan name : ")

            update_status_async("Status : Search [{}] clan info...".format(desired_clan))

            s1 = threading.Thread(target=data_search, args = ("https://corehalla.com/api/trpc/getClansRankings?input=%7B%22name%22%3A%22{}%22%2C%22page%22%3A%221%22%7D".format(desired_clan),))
            s2 = threading.Thread(target=id_search_event, args = ("https://corehalla.com/stats/clan/{}",))

            s1.start()
            s2.start()
            s1.join()
            s2.join()
        
        elif user_choice == "3":
            print("\n")
            start_brawl()

        elif user_choice == "4":
            print("\n1 -- Select your module."
                  "\n2 -- Enter the name of a player or clan."
                  "\n3 -- Check intelligent printing in the web page."
                  "\n4 -- Search the players by mainAlias or otherAliases."
                  "\n5 -- Select the desired player or clan ID with your mouse and press CTRL + C."
                  "\n6 -- Once the player or clan is successfully found (or not), you can quit and restart the module by pressing CTRL + Q.\n")

        elif user_choice == "5":
            print("\n")
            kill_brawl()

        elif user_choice == "6":
            discord.disconnect()
            game_is_executed()

        else:
            print("\nPlease enter a valid choice XD\n")

menu()