# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Aumix is a tty-based interactive method of controlling a sound card mixer.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define	name		aumix
%define	ver		2.8
%define	rel		los1
%define url		http://jpj.net/~trevor/aumix.html

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Sound
Group(ru_RU.KOI8-R):	Звук
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-ice.patch
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

#BuildRequires:	pkgconfig

%description
Aumix is a tty-based, interactive method of controlling a sound card
mixer. It lets you adjust the input levels from the CD, microphone,
and board synthesizers, as well as the output volume. Aumix can adjust
audio mixers from the command line, from a script, or interactively at
the console or terminal with an ncurses-based interface. The aumix-X11
package provides a GTK+ interface for using aumix with the X Window
System.

Aumix without interface.

#%package	gtk1
#Summary:	Aumix with gtk1 interface.
#Group:		Multimedia/Audio
#Requires:	%{name} = %{version}-%{release}

#%description	gtk1
#Aumix with gtk1 interface.

#%package	gtk2
#Summary:	Aumix with gtk2 interface.
#Group:		Multimedia/Audio
#Requires:	%{name} = %{version}-%{release}

#%description	gtk2
#Aumix with gtk2 interface.

%package	ncurses
Summary:	Aumix with ncurses interface.
Group:		Sound
Group(ru_RU.KOI8-R):	Звук
Requires:	%{name} = %{version}-%{release}
BuildRequires:	libncurses-dev
Requires:	libncurses

%description	ncurses
Aumix with ncurses interface.

%prep
%setup -q
%patch0 -p1

%build
%configure --without-gtk --without-gtk1 --without-alsa --without-gpm --without-ncurses
%{__make} %{_smp_mflags}
cd src
mv aumix aumix-minimal
cd ..
%{__make} clean
#%configure --without-gtk --without-alsa --without-gpm --without-ncurses
#make
#cd src
#mv aumix aumix-gtk1
#cd ..
#make clean
#%configure --without-alsa --without-gtk1 --without-ncurses --without-gpm
#make
#cd src
#mv aumix aumix-gtk2
#cd ..
#make clean
%configure --without-gtk --without-gtk1 --without-alsa --without-gpm
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

cd src
#cp aumix-minimal aumix-gtk1 aumix-gtk2 ${RPM_BUILD_ROOT}%{_bindir}/
cp aumix-minimal ${RPM_BUILD_ROOT}%{_bindir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/aumix-minimal
%{_bindir}/mute
%{_bindir}/xaumix
%{_datadir}/%{name}/*
%{_datadir}/locale/*/*/aumix.mo
%doc %{_man1dir}/*

#%files gtk1
#%defattr(-,root,root)
#%{_bindir}/aumix-gtk1

%files ncurses
%defattr(-,root,root)
%{_bindir}/aumix

#%files gtk2
#%defattr(-,root,root)
#%{_bindir}/aumix-gtk2

%changelog
* Sun Nov 29 2004 Igor Zubkov <icesik@mail.ru> 2.8-los1
- Initial build for Los Angeles GNU/Linux.
