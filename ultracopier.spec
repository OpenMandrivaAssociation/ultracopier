Name:		ultracopier
Version:	0.2.0.15
Release:	%mkrel 2
License:	GPLv3+
Group:		File tools
URL:		http://ultracopier.first-world.info/
Source:		http://files.first-world.info/ultracopier/%{version}/ultracopier-src-%{version}.tar.bz2
BuildRoot:	%_tmppath/%{name}-%{version}
BuildRequires:	qt4-devel
BuildRequires:	desktop-file-utils

Summary:	The QT advanced copier

%description
Ultracopier is an advanced file copier with copy list management.

%prep
%setup -q

#fix the source
%__sed -i "s|\r||g" CHANGELOG
%__chmod 0644 CHANGELOG

%build
qmake
%make 

%install
rm -rf %{buildroot}
install -D src/%{name} %{buildroot}%{_bindir}/%{name}
install -D src/other/*.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D src/other/*16* %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -D src/other/*128* %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*

desktop-file-install --vendor="" \
	--remove-category="Qt" \
	--add-category="System;FileManager;X-MandrivaLinux-System-FileTools;" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/ultracopier
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png


