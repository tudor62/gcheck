# 🎮 G-Check (v0.6)

**G-Check** is a minimalist Python utility that instantly checks the availability of video games across multiple popular distribution sources and repack platforms, saving you valuable time. 🔍

---

## 🛠️ Supported Sources

The application automatically queries the following platforms:
1. **SteamRip** (`steamrip.com`)
2. **Online-Fix** (`online-fix.me`)
3. **FitGirl Repacks** (`fitgirl-repacks.site`)
4. **DODI Repacks** (`dodi-repacks.site`)
5. **1337X** (`1337x.to`) 🛡️ *(Includes Cloudflare protection detection)*

---

## ⚙️ System Requirements & Dependencies

Make sure you have **Python** installed on your system. The script relies on the following external libraries:
* `requests` – for making HTTP requests to the websites.
* `colorama` – for colored terminal output.

You can install the required dependencies by running the following command in your terminal:
```bash
pip install requests colorama
```

---

## 🚀 How to Use

1. Clone the repository or download the files to your computer:
   ```bash
   git clone https://github.com/your-username/G-Check.git
   cd G-Check
   ```
2. Run the Python script:
   ```bash
   python main.py
   ```
3. Type the name of the game you want to search for when prompted in the terminal.

---

## 📊 Interface Example

```text
            ▄▄▄▀▀▀█                                   ▄▄▄▀▀▀█        
             █   █                                     █   █         
   ▀▄▄▄▄▄▄▄▀ ▀▄▄▄▀▀▀▄▄▄▄▄  █ ░ █            ▄▀▀█▀▀▀▄▄     ▀▄▄▄▀▀▀▄▄▄▄▄  █ ░ █   ▄▄▄▄▄
  ██▓██▀██▓██ █▓█   █▀▓▀▌  █ ░▒█   ▒█▓█░   █▓██ █▓█   █▀▓▀▌  █ ░▒█   █▄▄▀▀
 █▓▒▓   ▓▒▓█ █▓▒▓     ▀▀▀   █▒▓▒▄▀▀▓▄▄▄■▄  █▒░▒░   ░▓▀▀   █▓▓▒▓     ▀▀▀   █▒▓▒▄▀▀▓██▄■▄ 
 █▒░▒▓   ▓▒░▒█ █▒░▒▓         █▓█▓░  ▐▐░▓█▌▌ █▒▓▒█▀■▀▀▀     █▒░▒▓         █▓█▓░  ▐▐░▓█▌▌
 █░ ░▓   ▓░ ░█ █░ ░▓   █░██▄   █ ░ ▒   █▓▒▓█░ █▓█▓░    ▄▄■▄   █░ ░▓   ▄     █░██▄   █ ░ ▒   █▓▒▓█░
  █ █ ░▒ ▄ ▒░ ██ █ █ ░▒ ▄▄░░▒░▓■   █░▒░▓   █▒░░▒▒  █ ░▒▄ ▄▒░░▒░▓▌  █ █ ░▒ ▄▄░░▒░▓■   █░▒░▓   █▒░░▒▒ 
   ▀▄▄▄■▄■░█░█░   ▀▀▀■▀▀▀▀▀   █▀▀▀    █░▄▄▄▓   ▀▄▄▄▄▀▀▀▀     ▀▀▀■▀▀▀▀▀   █▀▀▀    █░▄▄▄▓
     ▄▄ █▒█▒█                 ▀▀   ■▀▀▀                        ▀▀   ■▀▀▀    
  ▄▄▀▀▄▄▄▓▄▀█                                                                      
   ▀ ▀▀▀▀▀▀                                                                       
                                                                             aplpha 0.6

┌──────────────────────────────────────────┐
│          🎮 GAME CHECKER (v0.6)          │
├──────────────────────────────────────────┤
│ Active search sources:                   │
│   1. SteamRip.com                        │
│   2. Online-fix.store                    │
│   3. Fitgirl-repacks                     │
│   4. Dodi-repack                         │
│   5. 1377X [🛡️ Cloudflare]              │
└──────────────────────────────────────────┘
Type your game name:
```

---

## 📄 License

This project is developed for educational and personal purposes.
