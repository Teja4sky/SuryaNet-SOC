from pyfiglet import Figlet
from colorama import Fore, Style, init
import time
import os

init()

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def show_banner():

    clear()

    fig = Figlet(font='slant')

    text = fig.renderText("SuryaNet SOC")

    print(Fore.CYAN + text)

    print(Fore.GREEN + "="*60)

    print(Fore.YELLOW + "  Advanced Network Intrusion Detection System")

    print(Fore.RED + "  Real-time Threat Monitoring Active")

    print(Fore.GREEN + "="*60)

    time.sleep(1)
