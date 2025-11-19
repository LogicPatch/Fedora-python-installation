import unicodedata
import os
import time

# Skripte ausführen mit    $ sudo python3 0?-????.py
# Zuletzt aktualisiert: 06.03.2023

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



'''
Ab den Themes werden hier alle weiteren Installationen festgehalten, damit Redundance bei weiteren Desktopinstallationen vermieden wird.
   Die Komplettinstallation und die Installation weiterer Anwendungen wird weiterhin im entsprechenden Desktop-Script vorgenommen.
'''




# Themes und Styles installieren
def themes():
    # Themes GTK
    print()
    print(green + '>>>>> Weitere Themes für GTK-basierte Desktops werden installiert.' + reset)
    time.sleep(3)
    os.system('sudo dnf install -y adwaita-gtk2-theme arc-theme arc-theme-plank bluebird-gtk3-theme bluebird-xfwm4-theme breeze-gtk deepin-gtk-theme gnome-themes-extra greybird-dark-theme greybird-light-theme greybird-plank greybird-xfwm4-theme yaru-theme')
def themesqt():
    # Themes Qt
    os.system('sudo dnf install -y adwaita-qt6 lxqt-themes materia-kde materia-kde-decorations materia-kde-kvantum')
def icons():
    # Icons
    print()
    print(green + '>>>>> Weitere Icons werden installiert.' + reset)
    os.system('sudo dnf install -y adwaita-icon-theme  breeze-icon-theme cosmic-icon-theme cosmic-wallpapers deepin-icon-theme deepin-wallpapers elementary-icon-theme elementary-xfce-icon-theme gnome-icon-theme papirus-icon-theme')
    time.sleep(3)
def fonts():
    # Fonts
    print()
    print(green + '>>>>> Weitere Schriftarten werden installiert.' + reset)
    time.sleep(3)
    os.system('sudo dnf install -y abattis-cantarell-fonts adobe-source-code-pro-fonts adobe-source-sans-pro-fonts adobe-source-serif-pro-fonts bitstream-vera-fonts-all dejavu-fonts-all fira-code-fonts fontawesome-fonts fontawesome-fonts-web fontawesome5-fonts fontawesome5-fonts-all fontawesome5-brands-fonts fontawesome5-fonts-web gnu-free-fonts-common gnu-free-mono-fonts gnu-free-sans-fonts gnu-free-serif-fonts google-droid-fonts-all lato-fonts levien-inconsolata-fonts overpass-fonts overpass-mono-fonts liberation-fonts liberation-mono-fonts liberation-narrow-fonts liberation-sans-fonts liberation-serif-fonts google-roboto-fonts google-roboto-mono-fonts google-roboto-slab-fonts terminus-fonts terminus-fonts-console')




# Displaymanager
print()
def displaymanager(displaymanager):
    if displaymanager=='1':
        print()
        print(green + '>>>>> LightDM - Der Standarddisplaymanager von xfce, budgie, i3 u.a. wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y lightdm lightdm-gtk lightdm-gtk-greeter-settings slick-greeter lightdm-settings')
        print()
        print(fblue + '>>>>> Will man lightdm als Standard setzen, so muss man den anderen Displaymanager zunaechst deaktivieren und lightdm anschliessend aktivieren:\nsudo systemctl disable gdm.service/sddm.service/cosmic-greeter.service\nsudo systemctl enable lightdm.service' + reset)
    elif displaymanager=='2':
        print()
        print(green + '>>>>> GDM - Der Standard-Displaymanager von Gnome wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y gdm')
        print()
        print(fblue + '>>>>> Will man gdm als Standard setzen, so muss man den anderen Displaymanager zunaechst deaktivieren und gdm anschliessend aktivieren:\nsudo systemctl disable sddm.service/lightdm.service/cosmic-greeter.service\nsudo systemctl enable gdm.service' + reset)
    elif displaymanager=='3':
        print()
        print(green + '>>>>> sddm - Der Simple-Desktop-Display-Manager von KDE-Plasma wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y sddm sddm-kcm sddm-themes sddm-breeze materia-kde-sddm')
        print()
        print(fblue + '>>>>> Will man sddm als Standard setzen, so muss man den anderen Displaymanager zunaechst deaktivieren und sddm anschliessend aktivieren:\nsudo systemctl disable gdm.service/lightdm.service/cosmic-greeter.service\nsudo systemctl enable sddm.service' + reset)
    elif displaymanager=='4':
        print()
        print(green + '>>>>> cosmic-greeter - Der Standard-Displaymanager von Cosmic wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y cosmic-greeter')
        print()
        print(fblue + '>>>>> Will man cosmic-greeter als Standard setzen, so muss man den anderen Displaymanager zunaechst deaktivieren und cosmic-greeter anschliessend aktivieren:\nsudo systemctl disable gdm.service/lightdm.service/sddm.service\nsudo systemctl enable cosmic-greeter.service' + reset)
 
    else:
        pass




# Dateibrowser installieren
print()
def files(files):
    if files=='1':
        print()
        print(green + '>>>>> thunar - Der Dateibrowser des Xfce4-Desktops wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y Thunar tumbler thunar-archive-plugin thunar-media-tags-plugin thunar-volman')
    elif files=='2':
        print()
        print(green + '>>>>> nautlius - Der Dateibrowser des Gnome-Desktop wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y nautilus kde-connect-nautilus nautilus-extensions nautilus-gsconnect sushi nautilus-python')
    elif files=='3':
        print()
        print(green + '>>>>> dolphin - Der Dateibrowser des KDE-Plasma-Desktops wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y dolphin dolphin-plugins')
    elif files=='4':
        print()
        print(green + '>>>>> Es werden zunächst alle Dateibrowser für eine spätere Selektion installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y Thunar tumbler thunar-archive-plugin thunar-media-tags-plugin thunar-volman nautilus kde-connect-nautilus nautilus-extensions nautilus-gsconnect sushi nautilus-python dolphin dolphin-plugins')
    else:
        pass




# Kalenderapplikation(en) installieren
print()
def kalender(kalender):
    if kalender=='1':
        print()
        print(green + '>>>>> gnome-calendar des Gnome-Desktops wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y gnome-calendar')
    elif kalender=='2':
        print()
        print(green + '>>>>> korganizer von KDE-Plasma wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y korganizer')
    elif kalender=='3':
        print()
        print(green + '>>>>> calindori für Plasma-Mobile wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y calindori')
    elif kalender=='4':
        print()
        print(green + '>>>>> Es werden zunächst alle Kalenderapplikationen für eine spätere Selektion installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y gnome-calendar korganizer calindori')
    else:
        pass




# Editoren(en) installieren
print()
def editor(editor):
    if editor=='1':
        print()
        print(green + '>>>>> gedit des Gnome-Desktops wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y gedit gedit-plugins-data gedit-plugins')
    elif editor=='2':
        print()
        print(green + '>>>>> kate von KDE-Plasma wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y kate kate-plugins')
    elif editor=='3':
        print()
        print(green + '>>>>> geany - Kann über Plugins erweitert werde.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y geany geany-plugins-* geany-themes')
    elif editor=='4':
        print()
        print(green + '>>>>> elementary-code- Der Editor des Pantheon-Desktops.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y elementary-code')
    elif editor=='5':
        print()
        print(green + '>>>>> Es werden zunächst alle Editorapplikationen für eine spätere Selektion installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y gedit gedit-plugins-data gedit-plugins gedit-latex kate kate-plugins geany geany-plugins-* geany-themes elementary-code')
    else:
        pass




# Bildbetrachter installieren
print()
def image(image):
    if image=='1':
        print()
        print(green + '>>>>> eog - Der Bildbetrachter des Gnome-Desktops wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y eog eog-plugins')
    elif image=='2':
        print()
        print(green + '>>>>> gwenview - Der Bildbetrachter des KDE-Plasma-Desktop wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y gwenview')
    elif image=='3':
        print()
        print(green + '>>>>> lximage - Der Bildbetrachter des LxQT-Desktops wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y lximage-qt lximage-qt-l10n')
    elif image=='4':
        print()
        print(green + '>>>>> elementary-photos - Der Bildbetrachter des Pantheon-Desktops wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y elementary-photos')
    elif image=='5':
        print()
        print(green + '>>>>> nomacs - Ein schlanker und schneller Bildbetrachter mit vielen Funktionen wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y nomacs nomacs-plugins')
    elif image=='6':
        print()
        print(green + '>>>>> sxiv - Ein schlanker und schneller Bildbetrachter mit vielen Funktionen wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y sxiv')
    elif image=='7':
        print()
        print(green + '>>>>> Es werden zunächst alle Bildbetrachter für eine spätere Selektion installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y eog eog-plugins gwenview lximage-qt lximage-qt-l10n elementary-photos nomacs nomacs-plugins sxiv')
    else:
        pass




# PDF-Reader installieren
print()
def pdf(pdf):
    if pdf=='1':
        print()
        print(green + '>>>>> papers - Der PDF-Reader des Gnome-Desktops wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y papers')
    elif pdf=='2':
        print()
        print(green + '>>>>> okular - Der PDF-Reader des KDE-Plasma-Desktop wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y okular')
    elif pdf=='3':
        print()
        print(green + '>>>>> cosmic-reader - Der PDF-Reader des Cosmic-Desktop wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y cosmic-reader')
    elif pdf=='4':
        print()
        print(green + '>>>>> Es werden zunächst alle PDF-Reader für eine spätere Selektion installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y evince okular cosmic-reader')
    else:
        pass




# Tool für Bildschirmfotos installieren
print()
def screen(screen):
    if screen=='1':
        print()
        print(green + '>>>>> flameshot wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y flameshot')
    elif screen=='2':
        print()
        print(green + '>>>>> cosmic-screenshot vom Cosmic-Desktop wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y cosmic-screenshot')
    elif screen=='3':
        print()
        print(green + '>>>>> scrot für die Kommandozeile wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y scrot')
    elif screen=='4':
        print()
        print(green + '>>>>> Für eine spätere Selektion werden zunächst alle Tools für Screenshots installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y flameshot cosmic-screenshot scrot')
    else:
        pass