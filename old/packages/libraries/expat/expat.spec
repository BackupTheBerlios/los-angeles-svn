# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Library for XML files.
%define sum_ru		Библиотека для обработки XML файлов.
%define maintainer	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		libexpat
%define altname		expat
%define ver		1.95.7
%define rel		los1

Summary:	%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Libraries
Group(ru_RU.KOI8-R):	Система/Библиотеки
Source0:	%{altname}-%{version}.tar.gz
Patch0:		%{altname}-%{version}-mans.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%package dev
Group:		Development/Libraries
Group(ru_RU.KOI8-R):	Разработка/Библиотеки
Summary:	Development files for expat
Summary(ru_RU.KOI8-R):	Комплект для разработки используя expat

%description
The expat package contains a stream oriented C library for parsing XML.

%description -l ru_RU.KOI8-R
Пакет expat содержит C-ориентированную библиотеку для обработки XML

%description dev
The libexpat-dev package contains static libraries and headers to develope 
programs that uses libexpat.

%description -l ru_RU.KOI8-R dev
Пакет libexpat-dev содержит статические слинкованные библиотеки и заголовочные файлы
для разработки приложений, использующих libexpat.

%prep
%setup -q -n %{altname}-%{version} 
%configure
%patch0 -p1

%build
%{__make} %{_smp_mflags} 

%install
%{makeinstall} mandir=${RPM_BUILD_ROOT}/usr/share/man/man1 

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{altname}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README 
%{_libdir}/*.so*
%{_bindir}/*
%doc %{_man1dir}/*

%files dev
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Fri Oct 29 2004 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 1.2.11-los1
- Initial build for Los-Angeles Linux
