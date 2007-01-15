# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		File utility to identify file types.
%define sum_ru		Утилита для идентификации типа файла.
%define maintainer	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		file
%define ver		4.13
%define rel		los1

Summary:	%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libz >= 1.2.1-los3
Requires:	libmagic = %{ver}-%{rel}
BuildRequires:	libz-dev >= 1.2.1-los3

%description -n file
File is a utility used to determine file types.

%description -n file -l ru_RU.KOI8-R
File - утилита для выяснения типа файла.

%package -n libmagic
Summary: Library which contains functions to operate on the magic database.
Summary(ru_RU.KOI8-R): Библиотека для оперирования базами данных magic. Используется пакетом file.
Group: System/Libraries
Group(ru_RU.KOI8-R): Система/Библиотеки

%description -n libmagic 
Library which contains functions to operate on the magic database. Needed for 
working file package.

%description -n libmagic -l ru_RU.KOI8-R
Библиотека для оперирования базами данных magic. Необходима для работы пакета
file.

%package -n libmagic-dev
Summary: The header files and libraries needed for development using file package.
Summary(ru_RU.KOI8-R): Необходимое для разработки программ, использующих пакета file.
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: libmagic = %{ver}-%{rel}

%description -n libmagic-dev
The header files and libraries needed for development using file package.

%description -n libmagic-dev -l ru_RU.KOI8-R
Библиотеки и заголовочные файлы для разработки программ использующих пакет file.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%post -n libmagic -p /sbin/ldconfig
%postun -n libmagic -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc ChangeLog LEGAL.NOTICE MAINT README
%{_bindir}/file
%{_datadir}/file/
%doc %{_man1dir}/*
%doc %{_man4dir}/*

%files -n libmagic
%{_libdir}/libmagic.so*
%doc %{_man3dir}/*

%files -n libmagic-dev
%{_libdir}/libmagic.a
%{_libdir}/libmagic.la
%{_includedir}/magic.h

%changelog
* Tue Feb 15 2005 Igor Zubkov <icesik@mail.ru> 4.13-los1
- NMU.
- update to 4.13.

* Mon Jan 10 2005 Igor Zubkov <icesik@mail.ru> 4.03-los3
- NMU.
- clean up Group infomation.
- fix depends from zlib to libz.

* Fri Oct 29 2004 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 4.03-los2
- maintainer change
- package cut into three parts (file, libmagic, libmagic-dev)
- added spec localisation

* Sat Feb 14 2004 Igor Zubkov <icesik@mail.ru> 4.03-los1
- Initial build for Los Angeles GNU/Linux.
