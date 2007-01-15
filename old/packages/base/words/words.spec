# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		dict words
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		words
%define ver             0
%define rel             los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	Public Domain
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	http://www.cotse.com/wordlists/allwords
#Source0:	allwords.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	noarch

%description
dict words

%install
cd /usr/src/Lost/SOURCES

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/dict/
cp allwords.bz2 ${RPM_BUILD_ROOT}%{_datadir}/dict/
cd ${RPM_BUILD_ROOT}%{_datadir}/dict/
bzip2 -d allwords.bz2
ln -s allwords words

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/dict/*

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 0-los2
- change Group to System/Base.
- add russian Group information.
- remove Vendor field.

* Mon Feb 02 2004 Igor Zubkov <icesik@mail.ru> 0-los1
- Initial build for Los Angeles GNU/Linux.
