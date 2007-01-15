# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean target build

%define sum		Doxygen is the documentation system for C/C++.
%define sum_ru		Система документирования для C та C++.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		doxygen
%define ver		1.4.1
%define rel		los1
%define url		http://www.doxygen.org/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		base
Source0:	%{name}-%{version}.src.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	perl
BuildRequires:	task-c++-devel

%description
Doxygen is a documentation system for C, C++ and IDL. It can generate
an on-line class browser (in HTML) and/or an off-line reference manual
(in LaTeX) from a set of documented source files. There is also
support for generating man pages and for converting the generated
output into Postscript, hyperlinked PDF or compressed HTML. The
documentation is extracted directly from the sources.

Doxygen can also be configured to extract the code-structure from
undocumented source files. This can be very useful to quickly find
your way in large source distributions.

%description -l ru_RU.KOI8-R
Doxygen - это система документирования для C, C++ и IDL. Она может
создать онлайновый броузер классов (в HTML) и/или оффлайновый
справочник (в LaTeX) из набора документированных файлов. Есть также
поддержка создания man-страниц и конвертации сгенерированного вывода в
Postscript, PDF с гиперссылками и компрессированный HTML. Документация
извлекается непосредственно из исходных файлов.

Doxygen можно также сконфигурировать для получения структуры кода из
нелокументированных исходных файлов. Это может быть очень полезным для
того, чтобы бысто разобраться в большом проекте.

%prep
%setup -q

%build
./configure
%{__make}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 bin/doxygen ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 bin/doxytag ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_bindir}/doxygen
%{_bindir}/doxytag

%changelog
* Mon Apr 04 2005 Igor Zubkov <icesik@mail.ru> 1.4.1-los1
- update to 1.4.1.

* Mon Dec 06 2004 Igor Zubkov <icesik@mail.ru> 1.3.6-los1
- Initial build for Los Angeles GNU/Linux.
