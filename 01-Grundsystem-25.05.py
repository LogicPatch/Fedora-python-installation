import unicodedata
import os
import time


# Farbige print-Ausgaben
reset='\33[0m'          # Keine Farbe. (Farbe zurücksetzen)
lila='\33[35m'          # Lila (Installationsfragen)
flila='\33[1;35m'       # fettes Lila (Installationsfragen)
green='\33[32m'         # Grün (Alles O.K.)
fgreen='\33[1;32m'      # fettes Grün (Alles O.K.)
yellow='\33[1;33m'      # Gelb (Hinweismeldungen)
gray='\33[1;30m'        #
blue='\33[34m'          # Blau (Alternativ: Informationsausgaben)
fblue='\33[1;34m'       # fettes Blau (Informationsausgaben)
cyan='\33[36m'          # Cyan ()
fcyan='\33[1;36m'       # fettes Cyan ()
rot='\33[31m'           # Rot (Alternative: Fehler)
frot='\33[1;31m'        # fettes Rot (Fehler)

#------------------------------------------------------------------------------------------



# Probleme bei den gstreamer-Paketen wenn auch gleichzeitig das multimedia-Repo von negative17.org aktiviert ist: gstreamer1-plugins-bad gstreamer1-plugins-bad-freeworld gstreamer-ffmpeg gstreamer1-plugins-ugly
basic = input(yellow + 'Sollen die Grundlegenden Programme installiert werden (J/n)?: ' + reset)
codecs = input(yellow + 'Sollen Codecs für Spiel-, Bild- und Videoformate (mkv,mp4 usw.) installiert werden (J/n)?: ' + reset)
flatpak = input(yellow + 'Soll über Flatpak Pakete installiert werden können (J/n)?: ' + reset)
vim = input(yellow + 'Soll der Texteditor vim/neovim installiert werden? (J/n): ' + reset)
visualstudio = input(yellow + 'Soll die Entwicklungs-IDE Visual Studio Code installiert werden? (J/n): ' + reset)
emacs = input(yellow + 'Soll der Texteditor emacs installiert werden? (J/n): ' + reset)
if emacs in ('J', 'j', ''):
    doom = input(yellow + 'Soll zusätzlich zu emacs noch doom-emacs installiert werden? (J/n): ' + reset)
cups = input(yellow + 'Sollen Basistools für die Nutzung von Druckern bzw. Scannern installiert werden? (J/n): ' + reset)
wlan = input(yellow + 'Sollen Basistools für das WLAN installiert werden (nötig falls der PC WLAN-fähig sein soll)? (J/n): ' + reset)
tlp = input(yellow + 'Soll Fedora für die Nutzung auf dem Laptop bereit gemacht werden? (Akkulaufzeit, Schnellere Zugriffszeiten/Boot?) (J/n): ' + reset)
print()
print(yellow + '>>>>> Die Unterstützung der Grafikeinheit von NVidia/AMD/Intel wird hier installiert.' + reset)
#                        Grafikkarte herausfinden       'sudo lspci -v | grep VGA'    '''
nvidia = input(cyan + 'Soll die Unterstützung von NVidia-Grafikkarten installiert werden? (J/n): ' + reset)
intel = input(cyan + 'Soll die Unterstützung von Intel-Grafikeinheiten installiert werden? (J/n): ' + reset)
# guestadd = # Guest Additions nicht notwendig. Fedora Gäste haben bereits die notwendigen Erweiterungen installiert und am laufen!!!!




# einige grundlegende Systemspezifische-Pakete
if basic in ('J', 'j', ''):
    print()
    print(green + '>>>>> Grundlegende Programme werden installiert.' + reset)
    time.sleep(3)
    # [ffmpeg, git, gparted, htop, ImageMagick, ncdu, rsync] Schnon vorinstalliert: efibootmgr
    os.system('sudo dnf install -y dkms efibootmgr git gparted htop hunspell-de ImageMagick kernel-devel ncdu perl python3-pip rsync zvbi')
    # Starten von daemons
    os.system('sudo systemctl enable sshd.service')
    # Nur mit aktiviertem negativo17-Repo:  libdvdcss 
    # ausgelassen/unnötig: java-latest-openjdk




# Codecs für Spiel- Bild- und Videoformate installieren             [ffmpeg, gstreamer..., libdvdcss2, libdvdread]
if codecs in ('J', 'j', ''):
    print()
    print(green + 'Codecs für die einzelnen Spiel-, Bild- und Videoformate werden installiert ' + reset)
    os.system('sudo dnf install -y faad2 ffmpeg-free ffmpegthumbnailer flite gstreamer1-devel.x86_64 gstreamer1-plugins-base.x86_64 gstreamer1-plugins-base.i686 gstreamer1-plugins-good.x86_64 gstreamer1-plugins-good.i686 gstreamer1-plugins-good-extras.i686 gstreamer1-plugin-libav.x86_64 lame libaacs libdvdread opencv opus speex')
# gstreamer1-devel.i686