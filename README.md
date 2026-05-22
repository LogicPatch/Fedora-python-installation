![](logo.png)
# Fedora Python Installation

Automated Fedora Workstation setup and customization using modular Python scripts.

---

# 🐧 Overview

This project provides a collection of interactive Python scripts to automate the setup and customization of Fedora Workstation systems.

It helps quickly configure a fresh Fedora installation with:

- repositories
- multimedia codecs
- GNOME customization
- Flatpak integration
- development tools
- desktop applications
- gaming tools
- productivity software

The project is designed to create a reproducible and modular Fedora desktop environment.

---

# 🎯 Who is this for?

- Fedora users reinstalling systems frequently
- Developers setting up workstations
- Linux enthusiasts wanting automation
- Users migrating between Fedora versions
- Anyone wanting reproducible desktop setups

---

# 💡 Key Features

- ✅ Interactive installation menus
- ✅ Modular Python scripts
- ✅ Fedora-focused automation
- ✅ RPM Fusion integration
- ✅ Flatpak support
- ✅ GNOME customization
- ✅ Multimedia codec installation
- ✅ Developer environment setup
- ✅ Gaming & virtualization tools
- ✅ Reproducible workstation provisioning

---

# 🌿 Branch Strategy

| Branch | Purpose |
|---|---|
| `main` | Current Fedora release |
| `fedora-43` | Archived Fedora 43 version |


## Workflow

- `main` always targets the latest Fedora release
- Older Fedora releases are archived in separate branches
- Stable release states can additionally be tagged

Example:

```text
main        -> Fedora 45
fedora-44   -> Archived Fedora 44 setup
fedora-43   -> Archived Fedora 43 setup
```

---

# 🛠️ Script Breakdown

## 00-repositories.py

Repository and package source configuration.

### Features

- RPM Fusion setup
- Flatpak integration
- multimedia repositories
- third-party repositories
- codec installation
- Fedora system updates

---

## 01-base-system.py

Base system configuration and essential utilities.

### Features

- terminal utilities
- SSH tools
- system monitoring
- development dependencies
- driver installation
- printer support
- laptop optimizations
- NVIDIA / AMD / VirtualBox support
- editors and CLI tools

---

## 02-gnome.py

GNOME desktop customization and configuration.

### Features

- GNOME extensions
- themes and icons
- fonts
- shell customization
- desktop tweaks
- display manager selection
- file manager alternatives
- screenshot tools
- productivity utilities

---

## 03-applications.py

Desktop applications and user software.

### Includes

#### 🌐 Browsers
- Firefox
- Chromium
- Brave
- Google Chrome

#### 💬 Communication
- Telegram
- Signal
- Discord
- Viber
- Thunderbird

#### 🎬 Multimedia
- VLC
- Celluloid
- Rhythmbox
- HandBrake
- Kdenlive

#### 🎨 Creative Tools
- GIMP
- Krita
- Inkscape
- Blender

#### 💻 Development
- VSCode
- PyCharm
- Sublime Text
- Docker tools

#### 🎮 Gaming & Virtualization
- Steam
- Lutris
- Heroic Games Launcher
- VirtualBox
- KVM/QEMU

#### 🔐 Utilities
- KeePassXC
- GNOME Password Safe
- backup tools
- archive utilities

And much more...

---

# ⚙️ Requirements

- Fedora Workstation
- Python 3
- sudo privileges
- internet connection

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/LogicPatch/Fedora-python-installation.git
cd Fedora-python-installation
```

Run the scripts in order:

```bash
python3 00-repositories.py
python3 01-base-system.py
python3 02-gnome.py
python3 03-applications.py
```

---

# 📋 Recommended Installation Order

```text
1. 00-repositories.py
2. 01-base-system.py
3. 02-gnome.py
4. 03-applications.py
```

---

# 🚧 Planned Features

- reusable helper functions
- automatic Fedora version detection
- package profiles
- KDE support
- backup/import functionality
- improved logging
- configuration files
- non-interactive mode

---

# ⚠️ Disclaimer

These scripts modify:

- repositories
- installed packages
- desktop configuration
- system settings

Always review scripts before executing them.

Use at your own risk.

---

# 📜 License

MIT License