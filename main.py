import requests
from colorama import Fore, Style

def g_check():   
    print("             \033[0;37m                              \033[0;34m▄▄▄\033[0;34;47m▀▀▀\033[0;34m█\033[0;37m                                        \033[0;34m▄▄▄\033[0;34;47m▀▀▀\033[0;34m█\033[0;37m        \033[0m")
    print("               \033[0;37m                               \033[0;34m█\033[0;34;47m   \033[0;34m█\033[0;37m                                          \033[0;34m█\033[0;34;47m   \033[0;34m█\033[0;37m         \033[0m")
    print("              \033[0;37m  \033[0;30;44m▀\033[0;37;44m▄▄▄▄▄▄▄\033[0;30;44m▀\033[0;37m     \033[0;30;44m▀\033[0;37;44m▄▄▄▀▀▀▄▄▄\033[0;34m▄▄\033[0;37m   \033[0;34m█\033[0;34;47m ░ \033[0;34m█\033[0;37m            \033[0;34m▄\033[0;34;47m▀▀\033[0;37;44m█▀▀█\033[0;34;47m▀\033[0;37;44m▄\033[0;34m▄\033[0;37m     \033[0;30;44m▀\033[0;37;44m▄▄▄▀▀▀▄▄▄\033[0;34m▄▄\033[0;37m   \033[0;34m█\033[0;34;47m ░ \033[0;34m█\033[0;37m    \033[0;34m▄▄\033[0;37;44m▄▄\033[0;34m▄\033[0m")
    print("               \033[0;37m \033[0;34m█\033[0;37;44m█▓█\033[0;34m█▀█\033[0;37;44m█▓█\033[0;34m█\033[0;37m   \033[0;34m█\033[0;37;44m█▓█\033[0;34m█\033[0;37m    \033[0;34m█\033[0;37;44m▀▓▀\033[0;34m▌\033[0;37m  \033[0;34m█\033[0;34;47m░▒░\033[0;34m█\033[0;37m           \033[0;34m█\033[0;34;47m ░\033[0;37;44m▒\033[0;34m█\033[0;37m  \033[0;37;44m▒█▓█\033[0;35;44m░\033[0;37m   \033[0;34m█\033[0;37;44m█▓█\033[0;34m█\033[0;37m    \033[0;34m█\033[0;37;44m▀▓▀\033[0;34m▌\033[0;37m  \033[0;34m█\033[0;34;47m░▒░\033[0;34m█\033[0;37m  \033[0;34m▄\033[0;37;44m▄▓▀\033[0;34m▀▀\033[0;37m \033[0m")
    print("              \033[0;34m█\033[0;37;44m▓▒▓ \033[0;37m   \033[0;37;44m ▓▒▓\033[0;34m█\033[0;37m \033[0;34m█\033[0;37;44m▓▒▓ \033[0;37m      \033[0;34m▀▀▀\033[0;37m   \033[0;34m█\033[0;34;47m▒▓▒\033[0;37m▄▀▀▓\033[0;37;44m▄▄▄\033[0;34m■▄\033[0;37m  \033[0;34m█\033[0;34;47m▒░▒\033[0;37;44m░\033[0;37m   \033[0;37;44m░▓▀▀\033[0;34m▀\033[0;37m  \033[0;34m█\033[0;37;44m▓▒▓ \033[0;37m      \033[0;34m▀▀▀\033[0;37m   \033[0;34m█\033[0;34;47m▒▓▒\033[0;37m▄▀▀▓██\033[0;37;44m▄\033[0;34m■▄\033[0;37m \033[0m")
    print("               \033[0;34m█\033[0;37;44m▒░▒\033[0;34m▓\033[0;37m   \033[0;34m▓\033[0;37;44m▒░▒\033[0;34m█\033[0;37m \033[0;34m█\033[0;37;44m▒░▒\033[0;34m▓\033[0;37m            \033[0;34m█\033[0;34;47m▓█▓\033[0;35;44m░\033[0;37m  \033[0;34m▐\033[0;37;44m▐\033[0;34;47m░\033[0;37;44m▓█▌\033[0;34m▌\033[0;37m \033[0;34m█\033[0;34;47m▒▓▒\033[0;34m█▀■▀▀▀\033[0;37m     \033[0;34m█\033[0;37;44m▒░▒\033[0;34m▓\033[0;37m            \033[0;34m█\033[0;34;47m▓█▓\033[0;35;44m░\033[0;37m  \033[0;34m▐\033[0;37;44m▐\033[0;34;47m░\033[0;37;44m▓█▌\033[0;34m▌\033[0m")
    print("              \033[0;34m█\033[0;37;44m░ ░\033[0;34m▓\033[0;37m   \033[0;34m▓\033[0;37;44m░ ░\033[0;34m█\033[0;37m \033[0;34m█\033[0;37;44m░ ░\033[0;34m▓\033[0;37m    \033[0;34m█\033[0;94;44m░\033[0;34m██▄\033[0;37m   \033[0;34m█\033[0;34;44m \033[0;94;44m░ \033[0;35;44m▒\033[0;37m   \033[0;34m█\033[0;37;44m▓▒▓█\033[0;35;44m░\033[0;37m \033[0;34m█\033[0;34;47m▓█▓\033[0;35;44m░\033[0;37m    \033[0;34m▄▄■▄\033[0;37m  \033[0;34m█\033[0;37;44m░ ░\033[0;34m▓\033[0;37m    \033[0;34m█\033[0;94;44m░\033[0;34m██▄\033[0;37m   \033[0;34m█\033[0;34;44m \033[0;94;44m░ \033[0;35;44m▒\033[0;37m   \033[0;34m█\033[0;37;44m▓▒▓█\033[0;35;44m░\033[0m")
    print("               \033[0;37m \033[0;34m█\033[0;34;44m \033[0;94;44m░▒ \033[0;34m▄\033[0;94;44m ▒░\033[0;34;44m \033[0;34m██\033[0;37m  \033[0;34m█\033[0;34;44m \033[0;94;44m░▒ \033[0;34m▄▄\033[0;94;44m░░▒░\033[0;35;44m▓\033[0;35m■\033[0;37m   \033[0;34m█\033[0;94;44m░▒░\033[0;35;44m▓\033[0;37m   \033[0;34m█\033[0;37;44m▒░░▒\033[0;35;44m▒\033[0;37m  \033[0;34m█\033[0;34;44m \033[0;94;44m░\033[0;35;44m▒\033[0;34m▄\033[0;37m \033[0;34m▄\033[0;94;44m▒░░▒\033[0;35;44m▓\033[0;35m▌\033[0;37m  \033[0;34m█\033[0;34;44m \033[0;94;44m░▒ \033[0;34m▄▄\033[0;94;44m░░▒░\033[0;35;44m▓\033[0;35m■\033[0;37m   \033[0;34m█\033[0;94;44m░▒░\033[0;35;44m▓\033[0;37m   \033[0;34m█\033[0;37;44m▒░░▒\033[0;35;44m▒\033[0m")
    print("              \033[0;37m  \033[0;35m▀\033[0;35;44m▄▄▄\033[0;35m■\033[0;35;44m▄■\033[0;37;44m░\033[0;34m█\033[0;37;44m░\033[0;34m█\033[0;37m    \033[0;34m▀▀▀\033[0;35m■▀▀▀▀▀\033[0;37m     \033[0;34m█\033[0;34;45m▀▀▀ \033[0;37m   \033[0;34m█\033[0;94;44m░\033[0;35;44m▄▄▄▓\033[0;37m    \033[0;35m▀\033[0;35;44m▄▄▄▄\033[0;35m▀▀▀▀\033[0;37m      \033[0;34m▀▀▀\033[0;35m■▀▀▀▀▀\033[0;37m     \033[0;34m█\033[0;34;45m▀▀▀ \033[0;37m   \033[0;34m█\033[0;94;44m░\033[0;35;44m▄▄▄▓\033[0m")
    print("               \033[0;37m    \033[0;34m▄▄\033[0;37m  \033[0;34m█\033[0;37;44m▒\033[0;34m█\033[0;37;44m▒\033[0;34m█\033[0;37m                 \033[0;34m▀▀\033[0;37m     \033[0;34m■▀\033[0;35m▀▀\033[0;37m                                    \033[0;34m▀▀\033[0;37m     \033[0;34m■▀\033[0;35m▀▀\033[0;37m    \033[0m")
    print("              \033[0;37m  \033[0;34m▄\033[0;37;44m▄▀▀▄▄▄▓▄▀\033[0;34m█\033[0;37m                                                                               \033[0m")
    print("               \033[0;37m   \033[0;34m▀\033[0;37m  \033[0;34m▀▀▀▀▀▀\033[0;37m                                                                                \033[0m")
    print("                                                                                                                  aplpha 0.6")


def lista():
  print(f"\n{Fore.CYAN}┌──────────────────────────────────────────┐{Style.RESET_ALL}")
  print(
      f"{Fore.CYAN}│{Style.RESET_ALL}          🎮"
      f"  {Style.BRIGHT}GAME CHECKER{Style.RESET_ALL} (v0.6)        "
      f" {Fore.CYAN}│{Style.RESET_ALL}"
  )
  print(f"{Fore.CYAN}├──────────────────────────────────────────┤{Style.RESET_ALL}")
  print(
      f"{Fore.CYAN}│{Style.RESET_ALL} Surse active de căutare:                 "
      f"{Fore.CYAN}│{Style.RESET_ALL}"
  )
  print(
      f"{Fore.CYAN}│{Style.RESET_ALL}   1. SteamRip.com                        "
      f"{Fore.CYAN}│{Style.RESET_ALL}"
  )
  print(
      f"{Fore.CYAN}│{Style.RESET_ALL}   2. Online-fix.store                    "
      f"{Fore.CYAN}│{Style.RESET_ALL}"
  )
  print(
      f"{Fore.CYAN}│{Style.RESET_ALL}   3. Fitgirl-repacks                     "
      f"{Fore.CYAN}│{Style.RESET_ALL}"
  )
  print(
      f"{Fore.CYAN}│{Style.RESET_ALL}   4. Dodi-repack                         "
      f"{Fore.CYAN}│{Style.RESET_ALL}"
  )
  print(
      f"{Fore.CYAN}│{Style.RESET_ALL}   5. 1377X {Fore.YELLOW}[🛡️"
          f" Cloudflare]{Style.RESET_ALL}              {Fore.CYAN}  │{Style.RESET_ALL}"
  )
  print(f"{Fore.CYAN}└──────────────────────────────────────────┘{Style.RESET_ALL}")
  print("Type your game name:")

def nume_introdus():
    nume = input()
    return nume


def cautare_fitgirl(joc_formatat):
    nume_joc = joc_formatat.lower()
    url = f"https://fitgirl-repacks.site/?s={nume_joc}"

    headers = {'User-Agent': 'Mozilla/5.0'}
    raspuns = requests.get(url, headers=headers)

    if raspuns.status_code == 200:
        #daca il gaseste
        if joc_formatat.lower() in raspuns.text.lower():
            print("The game is available on FitGirl✅ ")
        else:
            print("The game can't be found on Firgirl!❌")    
    else:
        print("Error from the site!⚠️")      


def cautare_steam_rip(joc_formatat):
    nume_joc = joc_formatat.lower()       
    url = f"https://steamrip.com/?s={nume_joc}" 

    headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/122.0.0.0 Safari/537.36"
      ),
      "Accept-Language": "en-US,en;q=0.9",
      "Accept": (
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
      ),
      "Connection": "keep-alive",
        }

    raspuns = requests.get(url, headers = headers)

    if raspuns.status_code == 200:
        if nume_joc in raspuns.text.lower():
            print("The game is available on SteamRip✅")
        else:
            print("The game can't be found on SteamRip❌")
    else:
        print("Error from the site⚠️")            

#functie pentru onlinefix, pt unele jocuri inca nu le gaseste
def cautare_onlinefix(joc_formatat):
    nume_joc = joc_formatat.lower()
    url = f"https://online-fix.me/index.php?do=search&subaction=search&story={nume_joc}"

    headers = {'User-Agent': 'Mozilla/5.0'}
    raspuns = requests.get(url, headers = headers)

    if raspuns.status_code == 200:
        if nume_joc in raspuns.text.lower():
            print("The game is available on OnlineFix✅")
        else:
            print("The game can't be found on OnlineFix❌")
    else:
        print("Error from the site⚠️  Check later!")        
        

def cautare_dodi(joc_formatat):
    nume_joc = joc_formatat.lower()
    url = f"https://dodi-repacks.site/?s={nume_joc}"

    headers = { #dodi foloseste protectie bazata pe cloudflare si trebuie un header complet
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/122.0.0.0 Safari/537.36"
      ),
      "Accept-Language": "en-US,en;q=0.9",
      "Accept": (
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
      ),
      "Connection": "keep-alive",
  }

    raspuns = requests.get(url, headers = headers)

    if raspuns.status_code == 200:
        if nume_joc in raspuns.text.lower():
            print("The game is available on DodiRepacks☑️")
        else:
            print("The game can't be found on DodiRepacks❌")
    else:
        print("Error from the site⚠️")      


def cautare_1377x(joc_formatat):
    nume_joc = joc_formatat.lower()
    url = f"https://1337x.to/search/{nume_joc}/1" #caut doar pe prima pagina,restu nu are rost 

    headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/122.0.0.0 Safari/537.36"
      ),
      "Accept-Language": "en-US,en;q=0.9",
      "Accept": (
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
      ),
      "Connection": "keep-alive",
  }

    raspuns = requests.get(url, headers=headers)

    if raspuns.status_code == 200:
        if nume_joc in raspuns.text.lower():
            print("The game is available on 1337X ☑️")
        else:
            print("The game can't be found on 1337X ❌")
    elif raspuns.status_code == 403:
            print("1337X a blocat accesul automat (Cloudflare 403) 🛡️")
    else:
            print(f"Eroare de la site (Cod {raspuns.status_code}).⚠️")
#-------------------------------------------------------------------------------------------------------    

def main(): #echivalentu la int main(), pentru o organizarea mai placuta ;)
    g_check()
    lista()

    joc_dorit = nume_introdus()

    joc_formatat = joc_dorit.replace(" ", "+") #pentru jocurile cu spatiu nu il va putea gasit pe site-uri = majoritatea site-urilor folosesc + ca delimitator

    cautare_fitgirl(joc_formatat)
    cautare_steam_rip(joc_formatat)
    cautare_onlinefix(joc_formatat)
    cautare_dodi(joc_formatat)
    cautare_1377x(joc_formatat)

main()    