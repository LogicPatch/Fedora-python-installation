import unicodedata
import os
import time
import Desktops2511





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


print()
print(cyan + '>>>>> Hier wird eine komplettinstallation von Gnome angeboten, für den Fall dass noch\n      keine Installation von Gnome durchgeführt wurde oder die Installation von Gnome\n      fehlerhaft ist und die Konfiguration zurückgesetzt werden soll.' + reset)




print()
gnome = input(cyan + 'Soll eine Komplettinstallation von gnome durchgeführt werden? (J/n): ' + reset)
appsgnome = input(cyan + 'Sollen noch weitere Anwendungen speziell für den Gnome-Desktop installiert werden? (J/n): ' + reset)
themes = input(cyan + 'Sollen weitere Themes und Styles für GTK-basierte Desktops wie Budgie, Gnome oder Mate installiert werden? (J/n): ' + reset)
print()
print(cyan + 'Soll ein Displaymanager installiert werden und falls ja welcher Displaymanager soll verwendet werden?' + reset)
displaymanager = input(cyan + ' 1 LightDM        - Den Standarddisplaymanager von xfce, budgie, i3 u.a. verwenden\n 2 GDM            - Den Standard-Displaymanager von Gnome verwenden\n 3 sddm           - Den Simple-Desktop-Display-Manager von KDE-Plasma verwenden\n 4 cosmic-greeter - Der Standard-Displaymanager von Cosmic verwenden.\n 5 Kein Displaymanager Installieren bzw. den bereits installierten nutzen\n\n 1, 2, 3, 4 oder 5? ' + reset)
print()
print(cyan + 'Soll ein bestimmter Dateibrowser installiert werden und falls ja welcher?' + reset)
files = input(cyan + ' 1 thunar der Dateibrowser des Xfce4-Desktops\n 2 nautlius der Dateibrowser des Gnome-Desktops\n 3 dolphin der Dateibrowser des KDE-Plasma-Desktops\n 4 cosmic-files der Dateibrowser des Cosmic-Desktops\n 5 Alle genannten Dateibrowser installieren\n 6 Keinen Dateibrowser\n\n 1, 2, 3, 4, 5 oder 6? ' + reset)
print()
print(cyan + 'Soll eine Kalenderapplikation installiert werden und falls ja welche?' + reset)
kalender = input(cyan + ' 1 gnome-calendar des Gnome-Desktops\n 2 korganizer von KDE-Plasma\n 3 calindori für Plasma-Mobile wird installiert\n 4 Alle genannten Kalenderapplikation\n 5 Keine Kalenderapplikation\n\n 1, 2, 3, 4 oder 5? ' + reset)
print()
print(cyan + 'Soll ein Editor installiert werden und falls ja welcher?' + reset)
editor = input(cyan + ' 1 gedit des Gnome-Desktops\n 2 kate von KDE-Plasma\n 3 geany - Kann über Plugins erweitert werden\n 4 elementary-code - Der Editor des Pantheon-Desktops\n 5 Alle genannten Editoren installieren\n 6 Keine Editorapplikation\n\n 1, 2, 3, 4, 5 oder 6? ' + reset)
print()
print(cyan + 'Soll ein bestimmter Bildbetrachter installiert werden und falls ja welcher?' + reset)
image = input(cyan + ' 1 eog der Bildbetrachter des Gnome-Desktops\n 2 gwenview der Bildbetrachter des KDE-Plasma-Desktops\n 3 lximage - Der Bildbetrachter des LxQT-Desktops\n 4 elementary-photos - Der Bildbetrachter des Pantheon-Desktops\n 5 nomacs - ein schneller und schlanker Bildbetrachter\n 6 sxiv - ein schneller und schlanker Bildbetrachter\n 7 Alle genannten Bildbetrachter installieren\n 8 Keinen Bildbetrachter\n\n 1, 2, 3, 4, 5, 6, 7 oder 8? ' + reset)
print()
print(cyan + 'Soll ein bestimmter PDF-Reader installiert werden und falls ja welcher?' + reset)
pdf = input(cyan + ' 1 evince der PDF-Reader des Gnome-Desktops\n 2 okular der PDF-Reader des KDE-Plasma-Desktops\n 3 cosmic-reader - Der PDF-Reader des Cosmic-Desktops\n 4 Alle genannten PDF-Reader installieren\n 5 Keinen PDF-Reader\n\n 1, 2, 3, 4 oder 5? ' + reset)
print()
print(cyan + 'Soll ein Tool für Bildschirmfotos installiert werden und falls ja welches?' + reset)
screen = input(cyan + ' 1 flameshot - GUI um Fotos zu erstellen und vor dem speichern zu bearbeiten\n 2 cosmic-screenshot - Screenshots mit dem Tool von Cosmic erstellen\n 3 scrot - Bildschirmfotos über die Kommandozeile\n 4 Alle genannten Tools für Screenshots installieren\n 5 Kein Tool für Screenshots\n\n 1, 2, 3, 4 oder 5? ' + reset)
print()




# Komplettinstallation von gnome
if gnome in ('J', 'j', ''):
    print()
    fileName=r'/usr/share/xsessions/gnome.desktop'
    if os.path.exists(fileName):
        sessiongnome = input (rot + '>>>>> Es wurde bereits eine gnome-Session gefunden. Soll dennoch die gnome-Komplettinstallation durchgeführt werden? (1/2)\n' + reset + yellow + '>>> 1. Ja, die vorhandene Installation ist fehlerhaft und muss reinstalliert werden.\n>>> 2. Nein, ich überprüfe erst noch die bereits installierte gnome-Session, bevor ich Tools überschreibe. ' + reset)
        if sessiongnome=='1':
            print(green + '>>>>> Eine Komplettinstallation von gnome, mit allen Anwendungen wird installiert.' + reset)
            time.sleep(3)
            os.system('sudo dnf group install -y workstation-product-environment')
        else:
            print(rot + '>>>>> Die vorhandene Installation wird zur Überprüfung beibehalten, mache nichts.' + reset)
            time.sleep(3)
    else:
        print(green + '>>>>> Eine Komplettinstallation von gnome, mit allen Anwendungen wird installiert.' + reset)
        time.sleep(3)
        os.system('sudo dnf group install -y workstation-product-environment')




# Weitere Anwendungen speziell für gnome
if appsgnome in ('J', 'j', ''):
    print()
    print(green + '>>>>> Es werden noch weitere Anwendungen speziell für Gnome installiert.' + reset)
    time.sleep(3)
    os.system('sudo dnf install -y gnome-extensions-app gnome-shell-extension-gamemode gnome-shell-extension-pop-shell gnome-shell-extension-user-theme gnome-tweaks transmission-gtk')




# Themes und Styles installieren
if themes in ('J', 'j', ''):
    Desktops2511.themes()
    Desktops2511.icons()
    Desktops2511.fonts()

# Displaymanager
Desktops2511.displaymanager(displaymanager)

# Dateibrowser installieren
Desktops2511.files(files)

# Kalenderapplikation(en) installieren
Desktops2511.kalender(kalender)

# Editoren(en) installieren
Desktops2511.editor(editor)

# Bildbetrachter installieren
Desktops2511.image(image)

# PDF-Reader installieren
Desktops2511.pdf(pdf)

# Tool für Bildschirmfotos installieren
Desktops2511.screen(screen)