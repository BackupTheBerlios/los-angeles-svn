# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		screen - screen manager with VT100/ANSI terminal emulation.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		screen
%define ver		4.0.2
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libncurses-dev
Requires:	libncurses

BuildRequires:	Linux-PAM-dev
Requires:	Linux-PAM

Requires:	shadow

%description
Screen is a full-screen window manager that multiplexes a physical
terminal between several processes, typically interactive shells.  Each
virtual terminal provides the functions of the DEC VT100 terminal and,
in addition, several control functions from the ISO 6429 (ECMA 48, ANSI
X3.64) and ISO 2022 standards (e.g. insert/delete line and support for
multiple character sets).  There is a scrollback history buffer for
each virtual terminal and a copy-and-paste mechanism that allows the
user to move text regions between windows.

%prep
%setup -q

%build
%configure --enable-pam --with-sys-screenrc=%{_sysconfdir}/screenrc
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
cd etc
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/
cp screenrc ${RPM_BUILD_ROOT}%{_sysconfdir}/

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc ChangeLog doc/FAQ NEWS* README TODO doc/README.DOTSCREEN
%config(noreplace) /etc/screenrc
%{_bindir}/screen*
%doc %{_infodir}/*
%doc %{_man1dir}/*
%{_datadir}/screen/*/*

%changelog
* Thu Jun 17 2004 Igor Zubkov <icesik@mail.ru> 4.0.2-los1
- Initial build for Los Angeles GNU/Linux.
