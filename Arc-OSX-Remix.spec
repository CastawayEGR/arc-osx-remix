Name:    Arc-OSX-Remix
Version: 0
Release: 2
Summary: OSX like Theme for Gnome GTK3

Source0: usr/share/backgrounds/macOS/macOS_mojave_wallpaper_mid-day.jpg
Source1: set-gdm-wallpaper
Source3: fonts
Source4: icons
Source5: themes

License: MIT
URL: https://github.com/CastawayEGR

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
install -p -m 644 %{SOURCE0} %{buildroot}/usr/share/backgrounds/macOS/

mkdir -p %{buildroot}/usr/share/fonts/SanFrancisco/
cp -aR %{SOURCE3} %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/share/icons/
cp -aR %{SOURCE4} %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/share/themes/Arc-OSX-Remix/
cp -aR %{SOURCE5} %{buildroot}/usr/share/

mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}

%post
set-gdm-wallpaper --rpm

%files
%{_bindir}/set-gdm-wallpaper
/usr/share/gnome-shell/wallpaper/macOS_mojave_wallpaper_mid-day.jpg
/usr/share/backgrounds/macOS/macOS_mojave_wallpaper_mid-day.jpg
/usr/share/fonts/SanFrancisco/
/usr/share/icons/OSX-ElCap/
/usr/share/icons/macOS/
/usr/share/themes/Arc-OSX-Remix/


%preun 
set-gdm-wallpaper --uninstall

%changelog
* Mon Nov 19 2018 Michael Tipton <mike@ibeta.org> 0-2
- Updated Package Version
* Sun Nov 18 2018 Michael Tipton <mike@ibeta.org> 0-1
- Initial Packaging
