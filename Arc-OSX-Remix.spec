Name:    Arc-OSX-Remix
Version: 0
Release: 2 
Summary: OSX like Theme for Gnome GTK3

Source0: macOS_mojave_wallpaper_mid-day.png
Source1: set-gdm-wallpaper
Source2: fonts
Source3: icons
Source4: themes

License: MIT
URL: https://github.com/CastawayEGR/arc-osx-remix

Requires(post): info
Requires(preun): info

Requires: glib2-devel neofetch gnome-tweak-tool

BuildArch: noarch


%description
Arc-OSX-Remix is a OSX like theme for Gnome. 
Includes GTK3 themes, cursor, icons, and background.

This is just a compiled version of the following sources with tweaks:

https://github.com/USBA/Apple-Arc-OSX-theme
https://git.opendesktop.org/umayanga/Cupertino-macOS-iCons
https://www.gnome-look.org/p/1084939/
https://github.com/B00merang-Project/macOS
https://github.com/DimaZirix/fedora-gdm-wallpaper

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/gnome-shell/wallpaper/
install -p -m 644 %{SOURCE0} %{buildroot}/usr/share/gnome-shell/wallpaper/

mkdir -p %{buildroot}/usr/share/backgrounds/macOS/

mkdir -p %{buildroot}/usr/share/fonts/SanFrancisco/
cp -aR %{SOURCE2} %{buildroot}/usr/share/

mkdir -p %{buildroot}/usr/share/icons/
cp -aR %{SOURCE3} %{buildroot}/usr/share/

mkdir -p %{buildroot}/usr/share/themes/Arc-OSX-Remix/
cp -aR %{SOURCE4} %{buildroot}/usr/share/

mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}

%post
set-gdm-wallpaper --rpm 2> /dev/null
cp /usr/share/gnome-shell/wallpaper/macOS_mojave_wallpaper_mid-day.png /usr/share/backgrounds/macOS/macOS_mojave_wallpaper_mid-day.png
cp /usr/share/themes/Arc-OSX-Remix/org.gnome.shell.gschema.override /usr/share/glib-2.0/schemas/org.gnome.shell.gschema.override 

users=`ls /home/ | grep -v lost`
release=`cat /etc/os-release | grep NAME | head -n 1 | cut -f 2 -d =`

for i in "$users"; do
  sudo -u $i mkdir -p /home/$i/.local/share/gnome-shell/extensions
  sudo -u $i gsettings set org.gnome.desktop.background picture-uri file:///usr/share/backgrounds/macOS/macOS_mojave_wallpaper_mid-day.png
  sudo -u $i gsettings set org.gnome.desktop.screensaver picture-uri file:///usr/share/backgrounds/macOS/macOS_mojave_wallpaper_mid-day.png
  sudo -u $i gsettings set org.gnome.desktop.interface gtk-theme "Arc-OSX-Remix"
  sudo -u $i gsettings set org.gnome.desktop.interface icon-theme "macOS"
  sudo -u $i gsettings set org.gnome.desktop.interface cursor-theme "OSX-ElCap"
  sudo -u $i gsettings set org.gnome.desktop.interface font-name "San Francisco Display 11"
  sudo -u $i gsettings set org.gnome.desktop.interface document-font-name "San Francisco Display 11"
  sudo -u $i gsettings set org.gnome.desktop.wm.preferences titlebar-font "San Francisco Display Bold 11"
  sudo -u $i gnome-shell-extension-tool -e user-theme@gnome-shell-extensions.gcampax.github.com 2> /dev/null

  if [[ $release == *CentOS* ]]; then 
        sudo -u $i gsettings set org.gnome.shell.extensions.classic-overrides button-layout "close,minimize,maximize:appemenu"
  else
        sudo -u $i gsettings set org.gnome.desktop.wm.preferences button-layout 'close,minimize,maximize:'
  fi
done

if [[ $release == *CentOS* ]]; then
  cp /usr/share/themes/Arc-OSX-Remix/gnome-shell/assets/view-grid-symbolic-active.svg.centos /usr/share/themes/Arc-OSX-Remix/gnome-shell/assets/view-grid-symbolic-active.svg
  cp /usr/share/themes/Arc-OSX-Remix/gnome-shell/assets/view-grid-symbolic.svg.centos /usr/share/themes/Arc-OSX-Remix/gnome-shell/assets/view-grid-symbolic.svg
  if [[ -f /usr/share/icons/hicolor/scalable/apps/start-here.svg ]]; then
      mv /usr/share/icons/hicolor/scalable/apps/start-here.svg /usr/share/icons/hicolor/scalable/apps/start-here.svg.bak
  fi
  if [[ -d /usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/ ]]; then
      mv /usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/  /usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com.bak/
  fi
  if [[ -d /usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/ ]]; then
      mv /usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/  /usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com.bak/
  fi
fi

glib-compile-schemas /usr/share/glib-2.0/schemas/ 2> /dev/null

killall -HUP gnome-shell

%files
%{_bindir}/set-gdm-wallpaper
/usr/share/gnome-shell/wallpaper/macOS_mojave_wallpaper_mid-day.png
/usr/share/backgrounds/macOS/
/usr/share/fonts/SanFrancisco/
/usr/share/icons/OSX-ElCap/
/usr/share/icons/macOS/
/usr/share/themes/Arc-OSX-Remix/

%preun 
set-gdm-wallpaper --uninstall

%changelog
* Wed Nov 21 2018 Michael Tipton <mike@ibeta.org> 0-2
- Added file/dir check logic 
- Set button-layout for CentOS 
* Tue Nov 20 2018 Michael Tipton <mike@ibeta.org> 0-1
- Initial Packaging
