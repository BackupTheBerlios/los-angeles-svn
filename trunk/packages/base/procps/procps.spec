# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		System and process monitoring utilities.
%define maintaner	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		procps
%define ver		3.2.4
%define rel		los1
%define url		http://procps.sourceforge.net/

Summary:        %{sum}
Name:           %{name}
Version:        %{ver}
Release:        %{rel}
Packager:       %{maintaner}
License:        LGPL, GPL, BSD-like
Group:          System/Base
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-3.2.1.patch
Patch1:         %{name}-3.2.1-topd.patch
Patch2:		%{name}-3.2.1-no-ldconfig.patch
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libncurses
BuildRequires:	libncurses-dev

%description
The Procps package provides programs to monitor and halt system processes.
Procps gathers information about processes via the /proc directory.

Procps includes ps, free, sysctl, skill, snice,
tload, top, uptime, vmstat, w and watch. You need some of these.

%description -l ru_RU.KOI8-R
В пакете Procps содержатся программы для управления процессами системы. Пакет
Procps собирает информацию о процессах через директорию /proc.

Procps также содержит ps, free, sysctl, skill, snice,
tload, top, uptime, vmstat, w и watch.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
%{__make} CFLAGS="${RPM_OPT_FLAGS}" %{_smp_mflags} CC=gcc

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -rf ${RPM_BUILD_ROOT}/lib/libproc.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS CodingStyle NEWS README README.top TODO
/bin/*
/sbin/*
/lib/libproc*
%{_bindir}/*
%doc %{_mandir}/man[158]/*

%changelog
* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 3.2.4-los1
- NMU: update to 3.2.4
- disable all patches.

* Sun Oct 24 2004 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 3.2.1-los2
- Then maintaner was changed to Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
- Added topd patch.
- Add procps-3.2.1-no-ldconfig.patch from Igor Zubkov.

* Sat May 08 2004 Igor Zubkov <icesik@mail.ru> 3.2.1-los1
- Initial build for Los Angeles GNU/Linux.
