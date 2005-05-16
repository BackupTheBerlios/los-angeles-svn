# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		wmupmon is a program to monitor system uptime.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		wmupmon
%define ver		0.1.1a
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL v2
Group:		X11
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
wmupmon is a program to monitor system uptime. It is a dockapp that is
supported by X window managers such as Window Maker, AfterStep, BlackBox,
Waimea, and Enlightenment.

The uptime is broken up into 4 parts - days, hours, minutes, and seconds.
It has an LCD look-alike user interface.
The back-light may be turned on/off by clicking the mouse button over the
application.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL THANKS
%{_bindir}/*
%doc %{_man1dir}/*

%changelog
* Wed Apr 27 2005 Igor Zubkov <icesik@mail.ru> 0.1.1a-los1
- Initial build for Los Angeles GNU/Linux.
