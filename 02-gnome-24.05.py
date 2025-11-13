import unicodedata
import os
import time
import Desktops2505





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
displaymanager = input(cyan + ' 1 LightDM - Den Standarddisplaymanager von xfce, budgie, i3 u.a. verwenden\n 2 GDM     - Den Standard-Displaymanager von Gnome verwenden\n 3 sddm    - Den Simple-Desktop-Display-Manager von KDE-Plasma verwenden\n 4 Kein Displaymanager Installieren bzw. den bereits installierten nutzen\n\n 1, 2, 3 oder 4? ' + reset)
print()
print(cyan + 'Soll ein bestimmter Dateibrowser installiert werden und falls ja welcher?' + reset)
files = input(cyan + ' 1 thunar der Dateibrowser des Xfce4-Desktops\n 2 nautlius der Dateibrowser des Gnome-Desktops\n 3 dolphin der Dateibrowser des KDE-Plasma-Desktops\n 4 Alle genannten Dateibrowser installieren\n 5 Keinen Dateibrowser\n\n 1, 2, 3, 4 oder 5? ' + reset)
print()
print(cyan + 'Soll eine Kalenderapplikation installiert werden und falls ja welche?' + reset)
kalender = input(cyan + ' 1 gnome-calendar des Gnome-Desktops\n 2 korganizer von KDE-Plasma\n 3 deepin-calendar des Deepin-Desktops\n 4 Alle genannten Kalenderapplikation\n 5 Keine Kalenderapplikation\n\n 1, 2, 3, 4 oder 5? ' + reset)
print()
print(cyan + 'Soll ein Editor installiert werden und falls ja welcher?' + reset)
editor = input(cyan + ' 1 gedit des Gnome-Desktops\n 2 kate von KDE-Plasma\n 3 geany - Kann über Plugins erweitert werden\n 4 deepin-editor - Der Editor des Deepin-Desktops\n 5 Alle genannten Editoren installieren\n 6 Keine Editorapplikation\n\n 1, 2, 3, 4, 5 oder 6? ' + reset)
print()
print(cyan + 'Soll ein bestimmter Bildbetrachter installiert werden und falls ja welcher?' + reset)
image = input(cyan + ' 1 eog der Bildbetrachter des Gnome-Desktops\n 2 gwenview der Bildbetrachter des KDE-Plasma-Desktops\n 3 deepin-image-viewer der Bildbetrachter des Deepin-Desktops\n 4 nomacs - ein schneller und schlanker Bildbetrachter\n 5 sxiv - ein schneller und schlanker Bildbetrachter\n 6 Alle genannten Bildbetrachter installieren\n 7 Keinen Bildbetrachter\n\n 1, 2, 3, 4, 5, 6 oder 7? ' + reset)
print()
print(cyan + 'Soll ein bestimmter PDF-Reader installiert werden und falls ja welcher?' + reset)
pdf = input(cyan + ' 1 evince der PDF-Reader des Gnome-Desktops\n 2 okular der PDF-Reader des KDE-Plasma-Desktops\n 3 Alle genannten PDF-Reader installieren\n 4 Keinen PDF-Reader\n\n 1, 2, 3 oder 4? ' + reset)
print()
print(cyan + 'Soll ein Tool für Bildschirmfotos installiert werden und falls ja welches?' + reset)
screen = input(cyan + ' 1 scrot - Bildschirmfotos über die Kommandozeile\n 2 flameshot - GUI um Fotos zu erstellen und vor dem speichern zu bearbeiten\n 3 deepin-screenshot - Screenshots mit dem Tool von Deepin erstellen und bearbeiten\n 4 Alle genannten Tools für Screenshots installieren\n 5 Kein Tool für Screenshots\n\n 1, 2, 3, 4 oder 5? ' + reset)
print()