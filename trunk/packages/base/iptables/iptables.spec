# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Classic Linux firewall.
%define sum_ru		Классический Linux firewall.
%define maintainer	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		iptables
%define ver		1.2.11
%define rel		los1

Summary:	%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Networking
Group(ru_RU.KOI8-R):	Система/Сеть
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-pathes.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Iptables is used to set up, maintain, and inspect the tables of IP packet
filter rules in the Linux kernel.

%description -l ru_RU.KOI8-R
Iptables используется для управление таблицей правил IP пакетов в ядре 
Linux.

%prep
%setup -q 
%patch0 -p1

%build
%{__make} %{_smp_mflags} PREFIX=/usr CC=gcc

%install
%{__make} PREFIX=${RPM_BUILD_ROOT}/usr install


%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc COMMIT_NOTES INSTALL TODO INCOMPATIBILITIES CURRENT_ISSUES
%{_sbindir}/*
%{_libdir}/iptables/
%doc %{_man8dir}/*


%changelog
* Fri Oct 29 2004 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 1.2.11-los1
- Initial build for Los-Angeles Linux
