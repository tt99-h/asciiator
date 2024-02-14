from pyfiglet import Figlet
from colorama import init, Fore
import os

# Initialiser Colorama
init(autoreset=True)

def effacer_console():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def afficher_menu():
    ascii_text = Figlet(font='slant')
    ascii_menu_title = ascii_text.renderText("Asciiator")

    print(f"{Fore.BLUE}{ascii_menu_title.strip()}{Fore.RESET}")
    print(f"{Fore.GREEN}CRÉE PAR MINESGAMES{Fore.RESET}")
    print(f"1. {Fore.GREEN}Convertir en ASCII{Fore.RESET}")
    print(f"2. {Fore.RED}Quitter{Fore.RESET}")

def choix_utilisateur():
    return input(f"{Fore.CYAN}Sélectionnez une option : {Fore.RESET}")

def convertir_en_ascii(texte):
    ascii_art = Figlet(font='slant')
    resultat = ascii_art.renderText(texte)
    return resultat

while True:
    afficher_menu()
    choix = choix_utilisateur()

    if choix == "1":
        texte_a_convertir = input(f"{Fore.CYAN}Entrez le texte à convertir en ASCII : {Fore.RESET}")
        ascii_resultat = convertir_en_ascii(texte_a_convertir)
        effacer_console()
        print(f"{Fore.GREEN}RÉSULTAT DE LA CONVERSION{Fore.RESET}")
        print(ascii_resultat)
        input(f"\n{Fore.CYAN}Appuyez sur Entrée pour continuer...{Fore.RESET}")
        effacer_console()
    elif choix == "2":
        print(f"\n{Fore.RED}Au revoir!{Fore.RESET}")
        break
    else:
        print(f"\n{Fore.YELLOW}Option invalide. Veuillez choisir une option valide.{Fore.RESET}")
