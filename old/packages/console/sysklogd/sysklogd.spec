# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		System Logger.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		sysklogd
%define ver		1.4.1
%define rel		los5

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):    Система/База
Source0:	%{name}-%{version}.tar.bz2
Source1:	syslog.conf
Patch0:		%{name}-%{version}-kernel_headers-1.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Provides:	syslog-daemon-any

Obsoletes:      syslog-ng metalog

%description
The Sysklogd package contains programs for recording system log messages,
such as those reported by the kernel.

%prep
%setup -q
%patch0 -p1

%build
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man5/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8/
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}

%{__make} BINDIR=${RPM_BUILD_ROOT}%{_sbindir} MANDIR=${RPM_BUILD_ROOT}%{_mandir} install

cp %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/syslog.conf
%doc ANNOUNCE CHANGES COPYING INSTALL MANIFEST NEWS README.1st README.linux
%{_sbindir}/*
%doc %{_man5dir}/*
%doc %{_man8dir}/*

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 1.4.1-los3
- remove Vendor field.
- change Group to System/Base.
- add russian group description.

* Tue Dec 14 2004 Igor Zubkov <icesik@mail.ru> 1.4.1-los2
- add noreplace option to /etc/syslog.conf
- some fixes

* Mon Nov 22 2004 Igor Zubkov <icesik@mail.ru> 1.4.1-los1
- Initial build for Los Angeles GNU/Linux.
