# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU version of the awk text processing utility.
%define sum_ru		GNU версия утилиты обработки текстов awk.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		gawk
%define ver		3.1.4
%define rel		los1

Summary:	%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL v2
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{ver}.tar.bz2
Patch0:		%{name}-%{ver}-los-dirs.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs. Gawk
should be upwardly compatible with the Bell Labs research version of
awk and is almost completely compliant with the 1993 POSIX 1003.2
standard for awk.

%description -l ru_RU.KOI8-R
Пакет gawk содержит GNU версию awk, утилиты обработки текстов. awk
интерпретирует специализированный язык программирования для быстрого и
легкого выполнения работ по сопоставлению с шаблонами и
переформатированию текстов. Gawk должен быть совместим с версией awk
от Bell Labs и практически полностью отвечает стандарту 1993 POSIX
1003.2 на awk.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -r ${RPM_BUILD_ROOT}%{_infodir}/dir
rm -f ${RPM_BUILD_ROOT}%{_bindir}/gawk-%{version}
rm -f ${RPM_BUILD_ROOT}%{_bindir}/pgawk-%{version}

%find_lang %{name}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog FUTURES LIMITATIONS NEWS POSIX.STD PROBLEMS
%doc README
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/%{name}-%{version}/*
%doc %{_infodir}/*
%doc %{_man1dir}/*

%changelog
* Fri Mar 18 2005 Igor Zubkov <icesik@mail.ru> 3.1.4-los1
- update to 3.1.4.

* Fri May 14 2004 Igor Zubkov <icesik@mail.ru> 3.1.3-los1
- Initial build for Los Angeles GNU/Linux.
