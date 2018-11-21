# Gnome OSX Theme
OSX like theme remix for gnome GTK3+ based on Apple-Arc-OSX.

![picture alt](https://image.ibb.co/hyc1hA/screenshot.png)

### Tested on:
* CentOS 7
* Fedora 28 & 29

Should work with other distros using gnome. May require additional tweaks (CentOS).

# Install
Make sure you save ALL important data before installing.

Fedora 28+:
```shell
# sudo dnf install Arc-OSX-Remix-0-1.noarch.rpm
# gsettings set org.gnome.shell.extensions.user-theme name "Arc-OSX-Remix"
```
Fedora 28 requires manual setting of theme in gnome tweak tools.

CentOS 7+:
```shell
# sudo curl -o /etc/yum.repos.d/konimex-neofetch-epel-7.repo https://copr.fedorainfracloud.org/coprs/konimex/neofetch/repo/epel-7/konimex-neofetch-epel-7.repo
# sudo yum install Arc-OSX-Remix-0-1.noarch.rpm
# gsettings set org.gnome.shell.extensions.user-theme name "Arc-OSX-Remix"
```

### Requirements:
#### Gnome Extensions
* [dash-to-dock](https://extensions.gnome.org/extension/307/dash-to-dock/)

Configure dash-to-dock location to bottom after installing by clicking gear by extension in gnome tweak tool.

Restart and enjoy! 

# Set Custom Login Wallpaper
```shell
# sudo set-gdm-wallpaper /path/to/image.png
```

# Credit and Licences
* Apple Arc OSX Theme: https://github.com/USBA/Apple-Arc-OSX-theme
* macOS Icons: https://git.opendesktop.org/umayanga/Cupertino-macOS-iCons
* macOS Cursor: https://www.gnome-look.org/p/1084939/
* Gnome Shell: https://github.com/B00merang-Project/macOS
* GDM Wallpaper Script: https://github.com/DimaZirix/fedora-gdm-wallpaper

Author Information
------------------

This theme compilation was created by [Michael Tipton](https://ibeta.org).
