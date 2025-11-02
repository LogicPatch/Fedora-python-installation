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


print(yellow + '>>>>> Achtung! Die Installation vom Free-Repository ist zwingend erforderlich für die Nonfree Installation.' + reset)
rpmfusionfree = input(cyan + 'Soll das Free-Repository von rpmfusion hinzugefügt werden? (J/n) ' + reset)
print(yellow + '>>>>> Achtung! Die Installation des Nonfree-Repositorys erfordert zwingend vorher die Installation des Free Repositorys' + reset)
rpmfusionnonfree = input(cyan + 'Soll das Nonfree-Repository von rpmfusion hinzugefügt werden? (J/n) ' + reset)
print()
winehq = input(cyan + 'Soll das offizielle winehq-Repository hinzugefügt werden? (J/n) ' + reset)
print()
# Guest Additions nicht notwendig. Fedora Gäste haben bereits die notwendigen Erweiterungen installiert und am laufen!!!!
print(yellow + '>>>>> Die Unterstützung der Grafikeinheit von NVidia/AMD/Intel/VirtualBox wird hier installiert.' + reset)
nvidia = input(cyan + 'Soll die Unterstützung von NVidia-Grafikkarten installiert werden? (J/n): ' + reset)




# Free-Repo von rpmfusion.org
if rpmfusionfree in ('J', 'j', ''):
    print()
    if os.path.isfile('/etc/yum.repos.d/rpmfusion-free.repo'):
        print(rot + '>>>>> Das Free-Repository von rpmfusion wurde bereits hinzugefügt, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Free-Repository von rpmfusion wird dem lokalen Repo hinzugefügt.' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm')
        os.system('sudo dnf update -y')




# Nonfree-Repo von rpmfusion.org
if rpmfusionnonfree in ('J', 'j', ''):
    print()
    if os.path.isfile('/etc/yum.repos.d/rpmfusion-nonfree.repo'):
        print(rot + '>>>>> Das Nonfree-Repository von rpmfusion wurde bereits hinzugefügt, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das Nonfree-Repository von rpmfusion wird dem lokalen Repo hinzugefügt' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm')
        os.system('sudo dnf update -y')




# WineHQ Offizielles Repository
if winehq in ('J', 'j', ''):
    print()
    if os.path.isfile('/etc/yum.repos.d/winehq.repo'):
        print(rot + '>>>>> Das offizielle winehq-Repository wurde bereits hinzugefügt, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das offizielle winehq-Repository wird dem lokalen Repo hinzugefügt' + reset)
        # Fedora Version
#        VERSION = input(yellow + '>>>>> Für welche Fedora-Version soll das Wine-Repositories eingebunden werden (34/35/36)? ' + reset)
#        os.system('sudo dnf config-manager --add-repo https://dl.winehq.org/wine-builds/fedora/' + VERSION + '/winehq.repo')
        os.system('sudo dnf config-manager addrepo --from-repofile=https://dl.winehq.org/wine-builds/fedora/$(rpm -E %fedora)/winehq.repo')
        os.system('sudo dnf update -y')




# NVidia-Repository
if nvidia in ('J', 'j', ''):
    print()
    if os.path.isfile('/etc/yum.repos.d/rpmfusion-nonfree-nvidia-driver.repo'):
        print(rot + '>>>>> Das NVidia-Repository wurde bereits hinzugefügt, mache nichts.' + reset)
    else:
        print(green + '>>>>> Das NVidia-Repo wird dem lokalen Repo hinzugefügt' + reset)
        time.sleep(3)
        os.system('sudo dnf install -y fedora-workstation-repositories')
        os.system('sudo dnf config-manager --set-enabled rpmfusion-nonfree-nvidia-driver')
        os.system('sudo dnf update -y')