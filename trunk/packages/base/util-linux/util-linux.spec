# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean up build for non i486
# TODO: update

%define sum		Util-Linux
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		util-linux
%define ver		2.12b
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.tar.bz2.sign
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libncurses-dev
Requires:	libncurses

BuildRequires:	libz-dev
Requires:	libz

%description
The  Util-linux  package  contains  a  number of miscellaneous utility
programs.  Some  of  the  more  prominent utilities are used to mount,
unmount,  format, partition and manage disk drives, open tty ports and
fetch kernel messages.

%prep
%setup -q

%build
cp hwclock/hwclock.c{,.backup}
sed 's%etc/adjtime%var/lib/hwclock/adjtime%' hwclock/hwclock.c.backup > hwclock/hwclock.c
CC=gcc ./configure 
%{__make} HAVE_KILL=yes HAVE_SLN=yes %{_smp_mflags} CC=gcc

%install
mkdir -p ${RPM_BUILD_ROOT}/var/lib/hwclock

%{__make} DESTDIR=${RPM_BUILD_ROOT} HAVE_KILL=yes HAVE_SLN=yes install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc HISTORY INSTALL MAINTAINER README
%config(noreplace) /etc/fdprm
/bin/*
/sbin/*
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/locale/*/*/util-linux.mo
%{_datadir}/misc/getopt/*
%doc %{_infodir}/*
%doc %{_mandir}/man[158]/*

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 2.12b-los2
- mark /etc/fdprm noreplace.
- remove Vendor field.

* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 2.12b-los1
- update to 2.12b

* Thu Jun 17 2004 Igor Zubkov <icesik@mail.ru> 2.12a-los1
- update to 2.12a

* Sat May 08 2004 Igor Zubkov <icesik@mail.ru> 2.12-los1
- Initial build for Los Angeles GNU/Linux.
