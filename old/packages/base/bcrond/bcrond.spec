# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Bisqwit's crond
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		bcrond
%define ver		1.0.8
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.html
Patch0:		%{name}-%{version}-los-build.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Provides:	cron-daemon-any

BuildRequires:	task-c++-devel

%description
Bisqwit's crond.

%prep
%setup -q
%patch0 -p1

%build
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}/var/spool/crontabs
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}/

install -c -s -m 755 bcrond ${RPM_BUILD_ROOT}%{_sbindir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_sbindir}/bcrond
/var/spool/crontabs

%changelog
* Thu Mar 31 2005 Igor Zubkov <icesik@mail.ru> 1.0.8-los2
- rebuild with gcc3.4-3.4.3.

* Sat Apr 03 2004 Igor Zubkov <icesik@mail.ru> 1.0.8-los1
- Initial build for Los Angeles GNU/Linux.
