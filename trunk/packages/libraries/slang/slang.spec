# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The shared library for the S-Lang extension language
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		slang
%define ver		1.4.9
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Libraries
Group(ru_RU.KOI8-R):	Система/Библиотеки
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
S-Lang is an interpreted language and a programming library.  The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language.  S-Lang's syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

%package dev
Summary: The development environment for S-Lang
Group: Development/C
Requires: %{name} = %{ver}-%{release}

%description dev
This package contains the S-Lang extension language development libraries
and header files which you'll need if you want to develop S-Lang based
applications.

%prep
%setup -q

%build
%configure
%{__make} elf all

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install-elf

cd ${RPM_BUILD_ROOT}/usr
rm -rf doc/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files dev
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/*.a
%{_includedir}/*.h

%changelog
* Tue Feb 08 2005 Igor Zubkov <icesik@mail.ru> 1.4.9-los1
- Initial build for Los Angeles GNU/Linux.
