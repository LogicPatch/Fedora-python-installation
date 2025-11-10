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




# Basic-System-Packages
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




# vim/neovim installieren
if vim in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/vim'
    if os.path.exists(fileName):
        print(rot + '>>>>> vim/neovim wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Texteditor vim/neovim wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y neovim python3-neovim.noarch vim vim-syntastic vim-syntastic-python vim-jedi')




# Visual Studio Code installieren
if visualstudio in ('J', 'j', ''):
    print()
    fileName=r'/var/lib/flatpak/app/com.visualstudio.code'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die Entwicklungs-IDE Visual Studio Code wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Die Entwicklungs-IDE Visual Studio Code wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo flatpak install -y com.visualstudio.code')




# emacs installieren
if emacs in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/emacs'
    if os.path.exists(fileName):
        print(rot + '>>>>> Der Texteditor emacs wurde bereits installiert, mache nichts.' + reset)
    else:
        print(green + '>>>>> Der Texteditor emacs wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y emacs ripgrep fd-find')
        
        # doom-emacs installieren
        if doom in ('J', 'j', ''):
                print(green + '>>>>> doom-emacs wird aktiviert.' + reset)
                fileName = '.emacs.d'
                if os.path.exists(fileName):
                        os.system('cd && rm -rf .emacs.d/')
                        os.system('cd && git clone --depth 1 https://github.com/hlissner/doom-emacs .emacs.d')
                        print()
                        print(yellow + '>>>>> Alle Fragen fuer die Installation von doom mit Ja bestätigen: ' + reset)
                        os.system('~/.emacs.d/bin/doom install')
                        print(yellow + '>>>>> Der Pfad zu .emacs/bin soll noch den Pfadvariablen hinzugefügt werden.\n Dies geschieht durch Eintragen folgender Zeile entweder in ~/.bashrc oder  ~/.zshrc:\n    export PATH=$HOME/.emacs.d/bin:$PATH ')
# nicht gefunden   elpa-common




# Basistools für Druckernutzung                [hplip, gutenprint, openprint,  system-config-printer]
if cups in ('J', 'j', ''):
    print()
    print(green + '>>>>> Basistools für die Drucker- Scannernutzung werden installiert.' + reset)
    time.sleep(3)
    os.system('sudo dnf install -y hplip hplip-gui sane-airscan system-config-printer xsane')
# ausgelassen/unnötig:  gutenprint gutenprint-extras gutenprint-plugin gutenprint-cups




# Basistools fuer WLAN                          [wpa-supplicant, wireless-tools]
if wlan in ('J', 'j', ''):
    print()
    print(green + '>>>>> Basistools für das WLAN werden installiert.' + reset)
    time.sleep(3)
    os.system('sudo dnf install -y wireless-regdb wpa_supplicant wpa_supplicant-gui')




# Laptop-Nutzung - Akkulaufzeit erhöhen Vorausladen und schnellerer Boot   [zram-generator, powertop, preload, tlp]
if tlp in ('J', 'j', ''):
    print()
    print(green + '>>>>> Notebook-Tools werden installiert.' + reset)
    time.sleep(3)
    os.system('sudo dnf install -y powertop tlp zram zram-generator')      # kein preload verfügbar
    #os.system('sudo systemctl enable acpid.service')
# ausgelassen/unnötig: acpi acpid




# Fedora Grafikkartentreiber
if nvidia in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/nvidia'
    if os.path.exists(fileName):
        print(rot + '>>>>> Die NVidia-Treiber wurden bereits installiert, mache nichts.' + reset)
    else:
#        print(fcyan + 'SecureBoot muss deaktiviert werden. Sie müssen das BIOS/EFI aufrufen, um es zu deaktivieren.' + reset)
#        time.sleep(5)
        print(green + '>>>>> Die NVidia-Treiber werden installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y akmod-nvidia kmod-nvidia nvidia-modprobe nvidia-persistenced nvidia-settings nvidia-xconfig xorg-x11-drv-nvidia xorg-x11-drv-nvidia-cuda xorg-x11-drv-nvidia-cuda-libs xorg-x11-drv-nvidia-cuda-libs xorg-x11-drv-nvidia-devel xorg-x11-drv-nvidia-devel xorg-x11-drv-nvidia-kmodsrc xorg-x11-drv-nvidia-libs xorg-x11-drv-nvidia-libs')
        print(fcyan + 'Warten Sie nach dem Ende der RPM-Transaktion, bis der kmod erstellt wurde.\nDies kann auf einigen Systemen bis zu 5 Minuten dauern.' + reset)
        print(yellow + '>>>>> Der Befehl  "modinfo -F version nvidia"  gibt nach einem Reboot, die Version des\nTreibers (z.B. 565.57) aus und nicht modinfo: FEHLER: Modul nvidia nicht gefunden.' + reset)
        time.sleep(5)
# Intel
if intel in ('J', 'j', ''):
    print()
    fileName=r'/usr/bin/intel'
    if os.path.exists(fileName):
        print(rot + 'Die Unterstützung von Intel-Grafikeinheiten wurde bereits installiert, mache nichts.' + reset)
        time.sleep(3)
    else:
        print(green + '>>>>> Die Unterstützung von Intel-Grafikeinheiten wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y intel-media-driver.x86_64 intel-media-driver.i686 intel-opencl intel-vaapi-driver libva-intel-driver.x86_64 libva-intel-driver.i686 libva-intel-hybrid-driver.x86_64 libva-intel-hybrid-driver.i686 mesa-libGL.x86_64 mesa-libGL.i686 mesa-vdpau-drivers.x86_64 mesa-vdpau-drivers.i686 mesa-vulkan-drivers.x86_64 mesa-vulkan-drivers.i686 ocl-icd.x86_64 ocl-icd.i686 vulkan-loader.x86_64 vulkan-loader.i686 xorg-x11-drv-intel')
# Virtualbox    # Guest Additions nicht notwendig. Fedora Gäste haben bereits die notwendigen Erweiterungen installiert und am laufen!!!!
