%global _beta_version %{version}-BETA-%{release}

Name:           bitwig-studio
Version:        1.3.6
Release:        1%{?dist}
Summary:        A dynamic software solution for music creation and performance to realize all of your musical ideas in every stage of production.

License:        EULA
URL:            http://www.bitwig.com/
Source0:        http://downloads.bitwig.com/%{name}-%{version}.deb

BuildRequires:  dpkg
Requires:       xcb-util-wm


%global __requires_exclude_from ^(/opt/bitwig-studio/bin/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/headless/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/jli/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/server/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/.*\\.so|/opt/bitwig-studio/bin/jre/lib/amd64/xawt/.*\\.so|/opt/bitwig-studio/bin/vamp-plugins/.*\\.so)$


%description 
Bitwig Studio is a dynamic software solution for music creation and performance to realize all of your musical ideas in every stage
of production.

From sound design to music creation, discover the new standard in customized workflow. Bitwig Studio inspires you to take greater
control of your productions, giving you access to every aspect of your workflow as needed. Streamline your creative process and
quickly take your music from ideas to complete songs, tracks and compositions. With Bitwig Studio, you’re in command of a workflow
that works best for you.

Record and arrange, improvise and perform, or do it all at once. Choose between several display profiles. Design your own sounds
with dedicated container devices. Combine built-in instruments, effects, and VST plug-ins. Bitwig Studio’s unified mapping system
allows you to modulate any device or VST parameter using macro controls and modulator devices.
Explore a new world of creative possibilities, including audio and note expressions, histogram-based value editing, layered editing,
extensive bounce-in-place functions, automatic slicing, smart controller integration, and the Open Controller Scripting API. Every
feature in Bitwig Studio was developed by musicians, for musicians. Welcome to the next generation of music creation and performance
software for Windows, Mac OS X, and Linux.
 

%prep


%build


%install
dpkg -x %{_sourcedir}/%{name}-%{version}.deb %{buildroot}

# put things into place
mkdir -m 755 -p %{buildroot}/usr/local/{bin,share}
#mv %{buildroot}/usr/bin %{buildroot}/usr/local/
mv %{buildroot}/usr/share %{buildroot}/usr/local/
#mv %{buildroot}/usr/local/share/icons/gnome %{buildroot}/usr/local/share/icons/hicolor


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
/opt/bitwig-studio
#"/usr/local/share/icons/hicolor/48x48/apps/Bitwig Studio.png"
/usr/bin/bitwig-studio
/usr/local/share/applications/bitwig-studio.desktop
/usr/local/share/icons/hicolor/48x48/apps/bitwig-modular.png
/usr/local/share/icons/hicolor/48x48/apps/bitwig-studio.png
/usr/local/share/icons/hicolor/scalable/apps/bitwig-modular.sh
/usr/local/share/icons/hicolor/scalable/apps/bitwig-studio.svg
/usr/local/share/icons/hicolor/scalable/mimetypes/application-bitwig-clip.svg
/usr/local/share/icons/hicolor/scalable/mimetypes/application-bitwig-device.svg
/usr/local/share/icons/hicolor/scalable/mimetypes/application-bitwig-preset.svg
/usr/local/share/icons/hicolor/scalable/mimetypes/application-bitwig-project-folder.svg
/usr/local/share/icons/hicolor/scalable/mimetypes/application-bitwig-project.svg
/usr/local/share/mime/packages/bitwig-studio.xml


%changelog
* Tue Feb 23 2016 Renich Bon Ciric - 1.3.6-1
* updated to 1.3.6

* Fri May 22 2015 Renich Bon Ciric - 1.1.8-1
- updated to 1.0.18

* Tue Oct 14 2014 Renich Bon Ciric <renich@woralelandia.com - 1.0.15-1
- updated to 1.0.15
- updated source url

* Tue Sep 16 2014 Renich Bon Ciric <renich@woralelandia.com> - 1.0.14-1
- updated to 1.0.14

* Sat Sep 13 2014 Renich Bon Ciric <renich@woralelandia.com> - 1.0.13-2
- updated to 1.0.13
- moved all files to /usr/local

* Thu Apr 10 2014 Renich Bon Ciric <renich@woralelandia.com> - 1.0.6-1
- Updated to version 1.0.6

* Wed Apr 02 2014 Renich Bon Ciric - 1.0.5-1
- Updated to version 1.0.5

* Tue Apr 01 2014 Renich Bon Ciric <renich@woralelandia.com> - 1.0.4-1
- First packaging
