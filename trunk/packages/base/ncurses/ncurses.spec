# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A CRT screen handling and optimization package.
%define sum_ru		Библиотеки для текстовых меню
%define maintainer	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		libncurses
%define altname		ncurses
%define ver		5.4
%define rel		los2

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
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

The   Ncurses   package   provides  character  and  terminal  handling
libraries, including panels and menus.

%description -l ru_RU.KOI8-R
Ncurses - бесплатная библиотека, в которой содержится информация о различных 
символьных терминалах, а также содержится набор функций для создания 
пользовательского интерфейса для текстового режима. В неё входят функции для
управления потоками символов, создания панелей и меню.

%package -n libncurses-dev
Summary: Ncurses devel
Summary(ru_RU.KOI8-R): Необходимое для разработки с использованием Ncurses
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description -n libncurses-dev
Libraries and header files for develope using Ncurses

%description -n libncurses-dev -l ru_RU.KOI8-R
Бибилиотеки и заголовочные файлы для разработки программ с использованием
Ncurses.

%package -n terminfo
Summary: Ncurses terminfo files
Summary(ru_RU.KOI8-R): Информация о символьных терминалах
Group: System/Base
Group(ru_RU.KOI8-R): Система/База
Requires: %{name} = %{version}-%{release}

%description -n terminfo
Ncurses terminfo files.

%description -n terminfo -l ru_RU.KOI8-R
Информация о различных символьных терминалах, необходимая Ncurses.

%prep
%setup -q -n %{altname}-%{ver}

%build
%configure --with-shared --without-debug
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

chmod 755 ${RPM_BUILD_ROOT}%{_libdir}/*.5.4
chmod 644 ${RPM_BUILD_ROOT}%{_libdir}/libncurses++.a
mkdir -p ${RPM_BUILD_ROOT}/lib
mv ${RPM_BUILD_ROOT}%{_libdir}/libncurses.so.5* ${RPM_BUILD_ROOT}/lib
ln -sf ../../lib/libncurses.so.5 ${RPM_BUILD_ROOT}%{_libdir}/libncurses.so
ln -sf libncurses.so ${RPM_BUILD_ROOT}%{_libdir}/libcurses.so

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{altname}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ANNOUNCE INSTALL MANIFEST NEWS README README.emx TO-DO
%{_bindir}/*
/lib/*
%{_libdir}/*.so.*
%{_datadir}/tabset/*
%doc %{_mandir}/man[157]/*

%files -n libncurses-dev
%defattr(-,root,root)
%doc doc
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/*
%doc %{_man3dir}/*

%files -n terminfo
%defattr(-,root,root)
%{_datadir}/terminfo/*/*
%{_libdir}/terminfo

%changelog
* Fri Oct 29 2004 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 5.4-los2
- Maintainer change.
- Added spec localization.
- Spec's clean up for ideology compatibility.

* Thu Jun 10 2004 Igor Zubkov <icesik@mail.ru> 5.4-los1
- update to a new release.

* Sat Feb 14 2004 Igor Zubkov <icesik@mail.ru> 5.3-los1
- Initial build for Los Angeles GNU/Linux.
