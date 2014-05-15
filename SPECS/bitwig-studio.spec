Name: 			bitwig-studio
Version: 		1.0.8
Release: 		1%{?dist}
Summary: 		A dynamic software solution for music creation and performance to realize all of your musical ideas in every stage of production.

License: 		EULA
URL: 			http://www.bitwig.com/
Source0: 		http://packs.bitwig.com/downloads/%{name}-%{version}.deb

BuildRequires: 	dpkg
Requires:		xcb-util-wm


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


%files
/opt/bitwig-studio
/usr/bin/bitwig-studio
/usr/share/applications/bitwig-studio.desktop
/usr/share/icons/gnome/48x48/apps/bitwig-studio.png
/usr/share/icons/gnome/scalable/apps/bitwig-studio.svg
/usr/share/icons/gnome/scalable/mimetypes/application-bitwig-clip.svg
/usr/share/icons/gnome/scalable/mimetypes/application-bitwig-preset.svg
/usr/share/icons/gnome/scalable/mimetypes/application-bitwig-project.svg
/usr/share/icons/gnome/scalable/mimetypes/application-bitwig-device.svg
/usr/share/icons/gnome/scalable/mimetypes/application-bitwig-project-folder.svg
/usr/share/mime/packages/bitwig-studio.xml


%changelog
* Thu Apr 10 2014 Renich Bon Ciric <renich@woralelandia.com> - 1.0.6-1
- Updated to version 1.0.6

* Wed Apr 02 2014 Renich Bon Ciric - 1.0.5-1
- Updated to version 1.0.5

* Tue Apr 01 2014 Renich Bon Ciric <renich@woralelandia.com> - 1.0.4-1
- First packaging
