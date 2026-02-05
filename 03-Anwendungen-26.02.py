

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
# mpv
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
# yazi                      (Flatpak)
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
# weechat
# KVM
# virtualbox
# texlive/latex

import unicodedata
import os
import time
import getpass


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
wine = input(cyan + 'Sollen die Emulatoren Wine und gamehub installiert werden? (J/n) ' + reset)
steam = input(cyan + 'Soll die Spieleplattform steam installiert werden? (J/n): ' + reset)
lutris = input(cyan + 'Soll die Spieleplattform lutris installiert werden? (J/n): ' + reset)
rustdesk = input(cyan + 'Soll die Remotesoftware rustdesk installiert werden? (J/n): ' + reset)
anydesk = input(cyan + 'Soll die Remotesoftware anydesk installiert werden? (J/n): ' + reset)
teamviewer = input(cyan + 'Soll die Remotesoftware teamviewer für den privaten Gebrauch installiert werden? (J/n): ' + reset)
ranger = input(cyan + 'Soll der Terminal-Dateimanager ranger installiert werden? (J/n): ' + reset)
yazi = input(cyan + 'Soll der Terminal-Dateimanager yazi installiert werden? (J/n): ' + reset)
zsh = input(cyan + 'Soll die Shell zsh installiert werden? (J/n): ' + reset)
ghostty = input(cyan + 'Soll das Terminal ghostty installiert werden? (J/n): ' + reset)
kitty = input(cyan + 'Soll das Terminal kitty installiert werden? (J/n): ' + reset)
tilix = input(cyan + 'Soll das Terminal tilix installiert werden? (J/n): ' + reset)
urxvt = input(cyan + 'Soll das Terminal urxvt installiert werden? (J/n): ' + reset)
conky = input(cyan + 'Soll der Systemmonitor conky installiert werden? (J/n): ' + reset)
zim = input(cyan + 'Soll das Desktop-Wiki zim installiert werden? (J/n): ' + reset)
xpad = input(cyan + 'Soll die Notizzettel-App xpad installiert werden? (J/n): ' + reset)
keepassxc = input(cyan + 'Soll der Passwortmanager keepassxc installiert werden? (J/n): ' + reset)
gsafe = input(cyan + 'Soll der Passwortmanager gnome-passwortsafe installiert werden? (J/n): ' + reset)
pycharm = input(cyan + 'Soll die Community-Version der Python-IDE pycharm installiert werden? (J/n): ' + reset)
sublime = input(cyan + 'Soll die IDE sublime-text installiert werden? (J/n): ' + reset)
weechat = input(cyan + 'Soll der IRC-Chatclient weechat installiert werden? (J/n): ' + reset)
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




# thunderbird installieren
if thunderbird in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/thunderbird'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Mail-Client thunderbird wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Mail-Client thunderbird wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y thunderbird')




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
        os.system('sudo dnf install -y vlc vlc-plugins-all')
# vlc-extras



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




# simplescreenrecorder installieren
if ssrecorder in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/simplescreenrecorder'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Programm simplescreenrecorder wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Programm simplescreenrecorder wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y simplescreenrecorder')




# HandBrake installieren
if handbrake in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/ghb'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Videobearbeitungs-Programm HandBrake wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Videobearbeitungs-Programm HandBrake wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y handbrake handbrake-gui')
# inkscape frei0r-plugins-opencv blender



# kdenlive installieren
if kdenlive in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/kdenlive'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Videoschnitt-Programm kdenlive wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Videoschnitt-Programm kdenlive wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y kdenlive')



# Codec-Problem !!!!!
# openshot installieren
if openshot in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/openshot-qt'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Videoschnitt-Programm openshot wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Videoschnitt-Programm openshot wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y openshot openshot-lang')




# wine und gamehub
if wine in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/wine'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Emulatoren wine und gamehub wurden bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Emulatoren wine und gamehub werden installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf group install -y c-development')
        os.system('sudo dnf group install -y development-tools')
        os.system('sudo dnf install -y alsa-plugins-pulseaudio.i686 cups-devel.x86_64 cups-devel.i686 glibc-devel.i686 glibc-devel libgcc.i686 libX11-devel.x86_64 libX11-devel.i686 freetype.i686 freetype.x86_64 freetype-devel.x86_64 freetype-devel.i686 libXcursor-devel.x86_64 libXcursor-devel.i686 libXi-devel.x86_64 libXi-devel.i686 libXext-devel.x86_64 libXext-devel.i686 libXxf86vm.x86_64 libXxf86vm.i686 libXxf86vm-devel.x86_64 libXxf86vm-devel.i686 libXrandr-devel.x86_64 libXrandr-devel.i686 libXinerama-devel.x86_64 libXinerama-devel.i686 mesa-libGLU-devel.i686 mesa-compat-libOSMesa-devel.x86_64 mesa-compat-libOSMesa-devel.i686 libXrender-devel.x86_64 libXrender-devel.i686 libpcap-devel.x86_64 libpcap-devel.i686 ncurses-devel.x86_64 ncurses-devel.i686 libzip-devel.i686 lcms2-devel.i686 libv4l-devel.x86_64 libv4l-devel.i686 libgphoto2-devel.x86_64 libgphoto2-devel.i686 libxml2-devel.i686 openldap.i686 openldap-devel.x86_64 openldap-devel.i686 libxslt-devel.x86_64 libxslt-devel.i686 gnutls-devel.x86_64 gnutls-devel.i686 libpng.x86_64 libpng.i686 libpng-devel.x86_64 libpng-devel.i686 libpng12-devel.x86_64 libpng12-devel.i686 flac-libs.i686 json-c-devel.x86_64 json-c-devel.i686 json-c.i686 libICE-devel.x86_64 libICE-devel.i686 libICE.i686 libSM.i686 libSM-devel.x86_64 libSM-devel.i686 libXtst-devel.x86_64 libXtst-devel.i686 libXtst.i686 libasyncns.i686 libedit-devel.x86_64 libedit-devel.i686 libedit.i686 liberation-narrow-fonts.noarch libieee1284.i686 libogg.i686 libsndfile.i686 libuuid.i686 libva.i686 libvorbis.i686 libwayland-client.i686 libwayland-server.i686 llvm-libs.i686 llvm15.i686 mesa-dri-drivers.i686 mesa-filesystem.i686 mesa-libEGL-devel.x86_64 mesa-libEGL-devel.i686 mesa-libEGL.i686 mesa-libgbm-devel.x86_64 mesa-libgbm-devel.i686 mesa-libgbm.i686 nss-mdns.i686 ocl-icd.i686 ocl-icd-devel.x86_64 ocl-icd-devel.i686 pulseaudio-libs.i686 sane-backends-devel.x86_64 sane-backends-devel.i686 sane-backends-libs.i686 tcp_wrappers-libs.i686 unixODBC.i686 samba-common-tools.x86_64 samba-libs.x86_64 samba-winbind.x86_64 samba-winbind-clients.x86_64 samba-winbind-modules.x86_64 mesa-libGL-devel.x86_64 mesa-libGL-devel.i686 fontconfig-devel.x86_64 fontconfig-devel.i686 libXcomposite-devel.x86_64 libXcomposite-devel.i686 libtiff-devel.i686 openal-soft-devel.x86_64 openal-soft-devel.i686 mesa-libOpenCL-devel.i686 alsa-lib-devel.i686 gsm-devel.x86_64 gsm-devel.i686 libjpeg-turbo-devel.x86_64 libjpeg-turbo-devel.i686 pulseaudio-libs-devel.i686 pulseaudio-libs-devel gtk3-devel.x86_64 gtk3-devel.i686 libattr.i686 libattr-devel.x86_64 libattr-devel.i686 libva-devel.x86_64 libva-devel.i686 libexif-devel.x86_64 libexif-devel.i686 libexif.i686 mpg123-devel.i686 mpg123-devel.x86_64 libcom_err-devel.i686 libcom_err-devel.x86_64 libFAudio-devel.i686 libFAudio-devel.x86_64 zlib-ng.x86_64 zlib-ng.i686 zlib-ng-devel.x86_64 zlib-ng-devel.i686')
        os.system('sudo dnf install -y winehq-staging')




# steam installieren
if steam in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.valvesoftware.Steam'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Spieleplattform steam wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Spieleplattform steam wird installiert.' + reset)
        time.sleep(3)
        print()
        os.system('sudo flatpak install -y flathub com.valvesoftware.Steam')




# lutris installieren
if lutris in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/lutris'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Spieleplattform lutris wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Spieleplattform lutris wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y dxvk-native.x86_64 dxvk-native.i686 giflib-devel.x86_64 giflib-devel.i686 libvkd3d.x86_64 libvkd3d.i686 lutris vulkan-loader.x86_64 vulkan-loader.i686 vulkan-loader-devel.x86_64 vulkan-loader-devel.i686 giflib.x86_64 giflib.i686 mpg123.x86_64 v4l-utils.x86_64 ocl-icd.x86_64 ocl-icd.i686 libxslt.x86_64 libxslt.i686 libva.x86_64 libva.i686 gtk3.x86_64 gtk3.i686')
# gstreamer1-plugins-bad-free-devel.i686 gstreamer1-plugins-bad-free-extras.i686 gstreamer1-libav.i686 gstreamer1-plugins-bad-freeworld.i686




# rustdesk installieren (Flatpak Installation)
if anydesk in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.rustdesk.RustDesk'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Remotesoftware rustdesk wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Remotesoftware rustdesk wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y com.rustdesk.RustDesk')




# anydesk installieren (Flatpak Installation)
if anydesk in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.anydesk.Anydesk'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Remotesoftware anydesk wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Remotesoftware anydesk wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y com.anydesk.Anydesk')




# teamviewer über die Webseite
if teamviewer in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/teamviewer'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Remotesoftware teamviewer für den privaten Gebrauch wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Remotesoftware teamviewer für den privaten Gebrauch wird installiert.' + reset)
        time.sleep(3)
        os.system('wget -q https://download.teamviewer.com/download/linux/teamviewer.x86_64.rpm')
        os.system('sudo dnf install -y teamviewer*.rpm')
        os.system('rm teamviewer*.rpm')




# ranger installieren
if ranger in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/ranger'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Terminal-Dateimanager ranger wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Terminal-Dateimanager ranger wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y ranger highlight atool w3m poppler mediainfo xfce4-terminal')
        print(yellow + '>>>>> Für die Konfiguration von Ranger siehe zim-Wiki Dateimanager.ranger' + reset)
        time.sleep(3)




# yazi installieren (Flatpak Installation)
if yazi in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/io.github.sxyazi.yazi'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Terminal-Dateimanager yazi wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Terminal-Dateimanager yazi wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y io.github.sxyazi.yazi')




# zsh installieren
if zsh in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/zsh'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Shell zsh wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Shell zsh wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y zsh zsh-syntax-highlighting zsh-autosuggestions')

        # Variable uzsh wird für die Anpassung des Themes benötigt
        uzsh = os.environ['HOME']
        #uzsh = input(fcyan + 'In welchem /home-Verzeichnis soll das oh-my-zsh git-Verzeichnis angelegt werden? Bitte einen Benutzernamen nennen! ' + reset)
        os.system('cd && sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
        #os.system('git clone git://github.com/robbyrussell/oh-my-zsh.git /home/' + uzsh + '/.oh-my-zsh')
        #os.system('chown -R ' + uzsh + ':users /home/' + uzsh + '/.oh-my-zsh')
        # Theme 'fino' in der Datei .zshrc aktivieren
        os.system("sed -i 's/ZSH_THEME=.*/ZSH_THEME=\"fino\"/g' /home/" + uzsh + "/.zshrc")
        print(yellow + 'Um die Login-Shell auf zsh zu ändern nutzt man als NORMALER Benutzer den Befehl:    $ chsh -s /bin/zsh    ' + reset)




# ghostty installieren
if ghostty in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/ghostty'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Terminal ghostty wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Terminal ghostty wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf copr enable -y scottames/ghostty')
        os.system('sudo dnf install -y ghostty')




# kitty installieren
if kitty in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/kitty'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Terminal kitty wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Terminal kitty wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y kitty')




# tilix installieren
if tilix in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/tilix'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Terminal tilix wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Terminal tilix wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y tilix tilix-nautilus')




# urxvt installieren
if urxvt in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/urxvt'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Terminal urxvt wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Terminal urxvt wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y rxvt-unicode xclip')
        print(yellow + '>>>>> Zum konfigurieren benötigt man eine ~/.Xresources oder ~/.Xdefaults  Datei.\n    Nach ändern dieser Datei muss man ein $ xrdb -merge ~/.Xresources ausführen:' + reset)
        time.sleep(3)




# conky installieren
if conky in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/conky'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Systemmonitor conky wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Systemmonitor conky wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y conky terminus-fonts terminus-fonts-console lm_sensors')




# Zim-Desktop Wiki installieren
if zim in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/zim'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Desktop-Wiki zim wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Desktop-Wiki zim wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y Zim')




# Notizzettel-App xpad installieren
if xpad in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/xpad'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Notizzettel-App xpad wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Notizzettel-App xpad wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y xpad')




# keepassxc installieren
if keepassxc in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/keepassxc'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Passwortmanager keepassxc wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Passwortmanager keepassxc wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y keepassxc')




# gnome-passwordsafe (secrets) installieren
if gsafe in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/org.gnome.World.Secrets'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Passwortmanager gnome-passwordsafe wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Passwortmanager gnome-passwordsafe wird installiert.' + reset)
        time.sleep(3)
        print(yellow + 'Sinnvolle Wahl ist:  2) flathub (system)' + reset)
        os.system('sudo flatpak install -y org.gnome.World.Secrets')




# pycharm Community-IDE installieren (Flatpak Installation)
if pycharm in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.jetbrains.PyCharm-Community'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Community-Version der Python-IDE pycharm wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Community-Version der Python-IDE pycharm wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y com.jetbrains.PyCharm-Community')




# Sublime-Text IDE installieren
if sublime in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/subl'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die IDE sublime-text wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die IDE sublime-text wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg')
        os.system('sudo dnf config-manager addrepo --from-repofile=https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo')
        #os.system('sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo')
        os.system('sudo dnf install -y sublime-text')




# weechat-IRC-Client installieren
if weechat in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/weechat'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der IRC-Client weechat wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der IRC-Client weechat wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y weechat')




# kvm/qemu/virt-manager installieren
if kvm in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/virt-manager'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Virtualisierungsumgebung kvm/qemu/virt-manager wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Virtualisierungsumgebung kvm/qemu/virt-manager wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y @virtualization')




# VirtualBox installieren
if vbox in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/virtualbox'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Virtualisierungsumgebung Virtualbox wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Virtualisierungsumgebung Virtualbox wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y binutils gcc make patch libgomp glibc-headers glibc-devel kernel-headers kernel-devel dkms VirtualBox virtualbox-guest-additions')
        uvbox = getpass.getuser()
        #uvbox = input(yellow + '>>> Welcher Benutzername soll der Gruppe vboxusers hinzugefügt werden? ' + reset)
        os.system('sudo usermod -aG vboxusers ' + uvbox)
        print(yellow + '>>>>> Jetzt noch ein Reboot durchführen' + reset)
        time.sleep(3)
# Seit 2023.01.01 nicht mehr nötig
# VirtualBox installieren (Über Webseite    ;    Kein Repo notwendig)
#vbox = input(blue + 'Soll Virtualbox jetzt installiert werden? (Y/n): ' + reset)
#if vbox=='N' or vbox=='n':
#    print(rot + 'Virtualbox wird nicht installiert.' + reset)
#    print()
#    time.sleep(3)
#else:
#    fileName=r'/usr/bin/virtualbox'
#    if os.path.exists(fileName):
#        print(rot + 'Virtualbox wurde bereits installiert, mache nichts.' + reset)
#        time.sleep(3)
#        print()
#    else:
#        print(green + 'Virtualbox wird installiert.' + reset)
#        time.sleep(3)
#        os.system('wget https://download.virtualbox.org/virtualbox/' + VBOXVER + '/VirtualBox-' + VBOXDET + '-Linux_amd64.run')
#        os.system('chmod 744 VirtualBox*-Linux_amd64.run')
#        os.system('./VirtualBox*-Linux_amd64.run')
#        os.system('rm VirtualBox*-Linux_amd64.run*')
#        os.system('sudo usermod -aG vboxusers ' + USER)
#        print(yellow + '>>> Jetzt noch ein Reboot durchfuehren' + reset)
#        time.sleep(3)
#        print()




# texlive installieren
if texlive in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/latex'
    if os.path.exists(fileName):
        print(rot + '>>>>> Das Textsatzsystem latex/texlive wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Textsatzsystem latex/texlive wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y texlive-scheme-full fontforge openjade psutils-perl texlive texlive-collection-omega texlive-collection-science texlive-fragmaster texlive-gnu-freefont texlive-HA-prosper texlive-koma-moderncvclassic texlive-lacheck texlive-latexdiff texlive-lcdftypetools texmaker texstudio un-core-*-fonts* un-extra-*-fonts*')
