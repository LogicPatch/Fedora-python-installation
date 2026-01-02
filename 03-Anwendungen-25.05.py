

# Inhalt
# firefox                   (war bereits installiert)
# brave                     (Flatpak)
# chromium
# google-chrome             (Flatpak)
# thunderbird
# signal-desktop            Flatpak Installation (Über ein externes Repository auch möglich ; Repo musste hinzugefügt werden)
# telegram
# viber                     Flatpak Installation
# discord
# Microsoft Teams           Flatpak Installation  (2023.03.20 Nur noch die PWA ; Weboberfläche)
# Zoom                      Flatpak Installation
# showtime
# vlc
# celluloid
# parole
# rhythmbox
# musicpod
# soundconverter
# eyedropper
# gpick
# gimp
# krita
# simplescreenrecorder
# handbrake
# kdenlive
# openshot
# wine
# steam                     Flatpak Installation
# lutris
# rustdesk
# anydesk                   Flatpak Installation
# teamviewer                Über Webseite
# ranger
# zsh
# ghostty
# kitty
# tilix
# urxvt
# conky
# zim
# xpad
# keepassxc
# gnome-passwordsafe        (Bei Fedora unter secrets bekannt)
# pycharm Community IDE     (Flatpak Installation)
# Sublime Text IDE
# KVM
# virtualbox
# texlive/latex

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


# transmission  |  gnome-boxes  |  weechat
print()
chromium = input(cyan + 'Soll der Webbrowser chromium installiert werden? (J/n): ' + reset)
brave = input(cyan + 'Soll der Webbrowser brave installiert werden? (J/n): ' + reset)
chrome= input(cyan + 'Soll der Webbrowser Google-Chrome installiert werden? (J/n): ' + reset)
thunderbird = input(cyan + 'Soll der Mail-Client thunderbird installiert werden? (J/n): ' + reset)
signal = input(cyan + 'Soll der Messenger signal installiert werden? (J/n): ' + reset)
telegram = input(cyan + 'Soll der Messenger telegram installiert werden? (J/n): ' + reset)
viber = input(cyan + 'Soll der Messenger viber installiert werden? (J/n): ' + reset)
discord = input(cyan + 'Soll der Messenger discord installiert werden? (J/n): ' + reset)
zoom = input(cyan + 'Soll der Messenger Zoom installiert werden? (J/n): ' + reset)
showtime = input(cyan + 'Soll der Videoplayer showtime installiert werden? (J/n): ' + reset)
mpv = input(cyan + 'Soll der Videoplayer mpv installiert werden? (J/n): ' + reset)
vlc = input(cyan + 'Soll der Videoplayer vlc installiert werden? (J/n): ' + reset)
celluloid = input(cyan + 'Soll der Videoplayer celluloid installiert werden? (J/n): ' + reset)
parole = input(cyan + 'Soll der Videoplayer parole installiert werden? (J/n): ' + reset)
rhythmbox = input(cyan + 'Soll der Audioplayer rhythmbox installiert werden? (J/n): ' + reset)
musicpod = input(cyan + 'Soll der Audioplayer musicpod installiert werden? (J/n): ' + reset)
soundconverter = input(cyan + 'Soll das Programm soundconverter installiert werden? (J/n): ' + reset)
eyedropper = input(cyan + 'Soll das Programm eyedropper installiert werden? (J/n): ' + reset)
gpick = input(cyan + 'Soll das Programm gpick installiert werden? (J/n): ' + reset)
gimp = input(cyan + 'Soll das Bildbearbeitungsprogramm gimp installiert werden? (J/n): ' + reset)
krita = input(cyan + 'Soll das Bildbearbeitungsprogramm krita installiert werden? (J/n): ' + reset)
ssrecorder = input(cyan + 'Soll das Programm simplescreenrecorder installiert werden? (J/n): ' + reset)
handbrake = input(cyan + 'Soll das Videobearbeitungs-Programm HandBrake installiert werden? (J/n): ' + reset)
kdenlive = input(cyan + 'Soll das Videoschnitt-Programm kdenlive installiert werden? (J/n): ' + reset)
openshot = input(cyan + 'Soll das Videoschnitt-Programm openshot installiert werden? (J/n): ' + reset)
wine = input(cyan + 'Sollen die Emulatoren Wine und playonlinux installiert werden? (J/n) ' + reset)
steam = input(cyan + 'Soll die Spieleplattform steam installiert werden? (J/n): ' + reset)
lutris = input(cyan + 'Soll die Spieleplattform lutris installiert werden? (J/n): ' + reset)
rustdesk = input(cyan + 'Soll die Remotesoftware rustdesk installiert werden? (J/n): ' + reset)
anydesk = input(cyan + 'Soll die Remotesoftware anydesk installiert werden? (J/n): ' + reset)
teamviewer = input(cyan + 'Soll die Remotesoftware teamviewer für den privaten Gebrauch installiert werden? (J/n): ' + reset)
ranger = input(cyan + 'Soll der Terminal-Dateimanager ranger installiert werden? (J/n): ' + reset)
zsh = input(cyan + 'Soll die Shell zsh installiert werden? (J/n): ' + reset)
urxvt = input(cyan + 'Soll das Terminal urxvt installiert werden? (J/n): ' + reset)
tilix = input(cyan + 'Soll das Terminal tilix installiert werden? (J/n): ' + reset)
kitty = input(cyan + 'Soll das Terminal kitty installiert werden? (J/n): ' + reset)
ghostty = input(cyan + 'Soll das Terminal ghostty installiert werden? (J/n): ' + reset)
conky = input(cyan + 'Soll der Systemmonitor conky installiert werden? (J/n): ' + reset)
zim = input(cyan + 'Soll das Desktop-Wiki zim installiert werden? (J/n): ' + reset)
xpad = input(cyan + 'Soll die Notizzettel-App xpad installiert werden? (J/n): ' + reset)
keepassxc = input(cyan + 'Soll der Passwortmanager keepassxc installiert werden? (J/n): ' + reset)
gsafe = input(cyan + 'Soll der Passwortmanager gnome-passwortsafe installiert werden? (J/n): ' + reset)
pycharm = input(cyan + 'Soll die Community-Version der Python-IDE pycharm installiert werden? (J/n): ' + reset)
sublime = input(cyan + 'Soll die IDE sublime-text installiert werden? (J/n): ' + reset)
kvm = input(cyan + 'Soll die Virtualisierungsumgebung kvm/qemu/virt-manager installiert werden? (J/n): ' + reset)
vbox = input(cyan + 'Soll die Virtualisierungsumgebung Virtualbox installiert werden? (J/n): ' + reset)
texlive = input(cyan + 'Soll das Textsatzsystem latex/texlive installiert werden? (J/n): ' + reset)
print()




# chromium installieren
if chromium in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/chromium-browser'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Webbrowser chromium wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Webbrowser chromium wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y chromium fedora-chromium-config')




# brave installieren
if brave in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.brave.Browser'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Webbrowser brave wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Webbrowser brave wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y com.brave.Browser')




# Google-Chrome
if chrome in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.google.Chrome'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Webbrowser google-chrome wurde bereits installiert, mache nichts..' + reset)
    else:
        print(green + '>>>>> Der Webbrowser google-chrome wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y flathub com.google.Chrome')




# telegram installieren
if telegram in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/org.telegram.desktop'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Messenger telegram wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Messenger telegram wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y org.telegram.desktop')




# signal-desktop
if signal in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/org.signal.Signal'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Messenger signal wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Messenger signal wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y org.signal.Signal')




# viber installieren (Flatpak Installation)
if viber in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.viber.Viber'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Messenger viber wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Messenger viber wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y com.viber.Viber')




# discord installieren (Flatpak Installation)
if discord in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.discordapp.Discord'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Messenger discord wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Messenger discord wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y com.discordapp.Discord')




# Zoom installieren (Flatpak Installation)
if zoom in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/us.zoom.Zoom'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Messenger Zoom wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Messenger Zoom wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y us.zoom.Zoom')




# showtime-Videoplayer installieren
if showtime in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/showtime'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Videoplayer showtime wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Videoplayer showtime wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y showtime')




# mpv-Videoplayer installieren
if mpv in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/mpv'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Videoplayer mpv wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Videoplayer mpv wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y mpv')




# vlc-Videoplayer installieren
if vlc in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/vlc'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Videoplayer vlc wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Videoplayer vlc wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y vlc vlc-extras')
# vlc-core



# celluloid-Videoplayer installieren
if celluloid in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/celluloid'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Videoplayer celluloid wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Videoplayer celluloid wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y celluloid')




# Parole-Videoplayer installieren
if parole in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/parole'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Videoplayer parole wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Videoplayer parole wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y parole libxfce4util libxfce4ui')




# rhythmbox installieren
if rhythmbox in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/rhythmbox'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Audioplayer rhythmbox wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Audioplayer rhythmbox wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y rhythmbox')




# musicpod installieren
if musicpod in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/org.feichtmeier.Musicpod'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Audioplayer musicpod wurde bereits installiert, mache nichts..' + reset)
    else:
        print(green + '>>>>> Der Audioplayer musicpod wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y flathub org.feichtmeier.Musicpod')




# soundconverter installieren
if soundconverter in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/soundconverter'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Programm soundconverter wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Programm soundconverter wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y soundconverter')




# eyedropper installieren
if eyedropper in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.github.finefindus.eyedropper'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Programm eyedropper wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Programm eyedropper wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y com.github.finefindus.eyedropper')




# gpick installieren
if gpick in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/gpick'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Programm gpick wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Programm gpick wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y gpick')




# gimp installieren
if gimp in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/gimp'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Bildbearbeitungsprogramm gimp wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Bildbearbeitungsprogramm gimp wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y gimp gimp-help-de')




# krita installieren
if krita in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/krita'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Bildbearbeitungsprogramm krita wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Bildbearbeitungsprogramm krita wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y krita')