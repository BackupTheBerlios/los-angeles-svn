# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Lynx-style info browser.
%define sum_ru		Удобный вьюер info-файлов.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		pinfo
%define ver		0.6.8
%define rel		los1

Summary:	%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL

Group:			Utilities/System
Group(ru_RU.KOI8-R):	Утилиты/Система

Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libncurses >= 5.3-los1
BuildRequires:	libncurses-dev >= 5.3-los1

%description
Pinfo is a ncurses based lynx-style info documentation browser.

%description -l ru_RU.KOI8-R
Гипертекстовый вьюер info-файлов. Пользовательский интерфейс аналогичен
lynx'у. Базируется на ncurses. Умеет также работать с man-страницами.
Поддерживает regexp-поиск.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL NEWS README TECHSTUFF TODO
%config /etc/pinforc
%{_bindir}/pinfo
%{_datadir}/locale/
%doc %{_infodir}/*
%doc %{_mandir}/man1/*

%changelog
* Tue Nov 16 2004 Igor Zubkov <icesik@mail.ru> 0.6.8-los1
- Initial build for Los Angeles GNU/Linux.
