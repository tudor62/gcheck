#functie pentru onlinefix.StopIteration
def cautare_onlinefix(joc_formatat):
    nume_joc = joc_formatat.lower()
    url = f"https://online-fix.me/index.php?do=search&subaction=search&story={nume_joc}"

    headers = {'User-Agen': 'Mozilla/5.0'}
    raspuns = requests.get(url, headers = headers)

    if raspuns.status_code == 200:
        if nume_joc in raspuns.text.lower():
            print("The game is available on SteamRip✔️")
        else:
            print("The game can't be found on OnlineFix")
    else:
        print("Erroare de la site.  Check later!")        
        