# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The Iana-Etc package provides data for network services and protocols.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		iana-etc
%define ver		1.01
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	The Open Software License v. 1.1
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{ver}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	noarch

%description
The Iana-Etc package provides data for network services and protocols.

%prep
%setup -q

%build
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/
%{__make} PREFIX=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc COPYING README
%config(noreplace) %{_sysconfdir}/protocols
%config(noreplace) %{_sysconfdir}/services

%changelog
* Thu Feb 03 2005 Igor Zubkov <icesik@mail.ru> 1.01-los1
- update to 1.01.
- mark config noreplace.

* Thu Jun 17 2004 Igor Zubkov <icesik@mail.ru> 1.0-los1
- Initial build for Los Angeles GNU/Linux.
