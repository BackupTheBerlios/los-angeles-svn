# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The Man-pages package contains over 1200 manual pages.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		man-pages
%define ver		1.62
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
Source1:	%{name}-%{version}.lsm
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	noarch

Requires:	man

%description
The Man-pages package contains over 1200 manual pages. This documentation
details the C and C++ functions, describes a few important device files
and provides documents which would otherwise be missing from other packages.

%prep
%setup -q

%install
%{__make} prefix=${RPM_BUILD_ROOT} install
cd ${RPM_BUILD_ROOT}
sync

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc %{_mandir}/*/*

%changelog
* Fri Jun 04 2004 Igor Zubkov <icesik@mail.ru> 1.62-los1
- Initial build for Los Angeles GNU/Linux.
