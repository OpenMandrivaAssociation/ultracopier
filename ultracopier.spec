Name:		ultracopier
Version:	0.2.0.16
Release:	%mkrel 1
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




%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.2.0.16-1mdv2011.0
+ Revision: 645473
- update to new version 0.2.0.16

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.0.15-2mdv2011.0
+ Revision: 615327
- the mass rebuild of 2010.1 packages

* Mon May 24 2010 Emmanuel Andry <eandry@mandriva.org> 0.2.0.15-1mdv2010.1
+ Revision: 545820
- import ultracopier


