# Gnome OSX Theme
OSX like theme remix for gnome GTK3+ based on Apple-Arc-OSX.

# Tested on:
Fedora 29

Should work with other distros using gnome.

# Usage
```shell
# set-gdm-wallpaper /path/to/image.png

Requires gresource binary (glib2 or glib2-devel library):
Fedora: 
# dnf install glib2-devel
```

# Install
Fedora 28+:
```shell
# dnf install Arc-OSX-Remix-0-1.noarch.rpm
```

# Recovering

If GDM load failed, then press ALT+F6 and:

```shell
# set-gdm-wallpaper --uninstall
OR
# cp /usr/share/gnome-shell/gnome-shell-theme.gresource.backup /usr/share/gnome-shell/gnome-shell-theme.gresource

OR delete RPM:
# dnf remove set-gdm-wallpaper
OR 
# rpm-ostree uninstall set-gdm-wallpaper
```

# Credit and Licences
Apple Arc OSX Theme: https://github.com/USBA/Apple-Arc-OSX-theme
macOS Icons: https://git.opendesktop.org/umayanga/Cupertino-macOS-iCons
macOS Cursor: https://www.gnome-look.org/p/1084939/
Gnome Shell: https://github.com/B00merang-Project/macOS
GDM Wallpaper Script: https://github.com/DimaZirix/fedora-gdm-wallpaper

