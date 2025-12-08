

# Inhalt
# firefox                   (war bereits installiert)
# chromium
# google-chrome             Über Webseite
# Opera                     (spyware???)
# thunderbird
# signal-desktop            Flatpak Installation (Über ein externes Repository auch möglich ; Repo musste hinzugefügt werden)
# telegram
# viber                     Flatpak Installation
# discord
# Microsoft Teams           Flatpak Installation  (2023.03.20 Nur noch die PWA ; Weboberfläche)
# Zoom                      Flatpak Installation
# totem
# vlc
# celluloid
# parole
# rhythmbox
# soundconverter
# gpick
# gcolor3
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
#opera= input(cyan + 'Soll der Webbrowser Opera installiert werden? (J/n): ' + reset)
thunderbird = input(cyan + 'Soll der Mail-Client thunderbird installiert werden? (J/n): ' + reset)
signal = input(cyan + 'Soll der Messenger signal installiert werden? (J/n): ' + reset)
telegram = input(cyan + 'Soll der Messenger telegram installiert werden? (J/n): ' + reset)
viber = input(cyan + 'Soll der Messenger viber installiert werden? (J/n): ' + reset)
discord = input(cyan + 'Soll der Messenger discord installiert werden? (J/n): ' + reset)
#teams = input(cyan + 'Soll der Messenger Microsoft Teams installiert werden? (J/n): ' + reset)
zoom = input(cyan + 'Soll der Messenger Zoom installiert werden? (J/n): ' + reset)
totem = input(cyan + 'Soll der Videoplayer totem installiert werden? (J/n): ' + reset)
mpv = input(cyan + 'Soll der Videoplayer mpv installiert werden? (J/n): ' + reset)
vlc = input(cyan + 'Soll der Videoplayer vlc installiert werden? (J/n): ' + reset)
celluloid = input(cyan + 'Soll der Videoplayer celluloid installiert werden? (J/n): ' + reset)
parole = input(cyan + 'Soll der Videoplayer parole installiert werden? (J/n): ' + reset)
rhythmbox = input(cyan + 'Soll der Audioplayer rhythmbox installiert werden? (J/n): ' + reset)
soundconverter = input(cyan + 'Soll das Programm soundconverter installiert werden? (J/n): ' + reset)
gpick = input(cyan + 'Soll das Programm gpick installiert werden? (J/n): ' + reset)
gcolor3 = input(cyan + 'Soll das Programm gcolor3 installiert werden? (J/n): ' + reset)
gimp = input(cyan + 'Soll das Bildbearbeitungsprogramm gimp installiert werden? (J/n): ' + reset)
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