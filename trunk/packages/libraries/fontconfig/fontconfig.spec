# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Library for configuring fonts
%define sum_ru		Библиотека для настройки доступа к шрифтам
%define maintainer	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		fontconfig
%define ver		2.2.3
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
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%package dev
Group:		Development/Libraries
Group(ru_RU.KOI8-R):	Разработка/Библиотеки
Summary:	Development files for %{name}
Summary(ru_RU.KOI8-R):	Комплект для разработки программ использующих %{name}
Requires: pkgconfig

%description
The %{name} package contains a stream oriented C library to manage
acces to fonts.

%description -l ru_RU.KOI8-R
Пакет %{name} содержит C-ориентированную библиотеку для управления  
доступом к шрифтам.

%description dev
The %{name}-dev package contains static libraries and headers to develope 
programs that uses %{name}.

%description -l ru_RU.KOI8-R dev
Пакет %{name}-dev содержит статические слинкованные библиотеки и заголовочные файлы
для разработки приложений, использующих %{name}.

%prep
%setup -q  
%configure

%build
%{__make} %{_smp_mflags} 

%install
%{makeinstall} 

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README ChangeLog
%config(noreplace) %{_sysconfdir}/fonts
%{_libdir}/*.so*
%{_bindir}/*
%doc %{_mandir}/man[135]/*
%doc %{_datadir}/doc/%{name}/*

%files dev
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*


%changelog
* Fri Oct 29 2004 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 1.2.11-los1
- Initial build for Los-Angeles Linux
