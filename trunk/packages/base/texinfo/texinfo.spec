# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU texinfo package.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		texinfo
%define ver		4.6
%define rel		los3

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Other
Group(ru_RU.KOI8-R):	Разработка/Разное
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libncurses >= 5.4-los1
BuildRequires:	libncurses-dev >= 5.4-los1

%description
The  Texinfo  package  contains programs used for reading, writing and
converting Info documents, which provide system documentation.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
%{__make} DESTDIR=${RPM_BUILD_ROOT} TEXMF=/usr/share/texmf install-tex

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL INTRODUCTION NEWS README TODO
%{_bindir}/*
%{_datadir}/texinfo/*
%doc %{_infodir}/*
%doc %{_mandir}/man[15]/*
%{_datadir}/texmf/tex/texinfo/*
%{_datadir}/texmf/tex/generic/dvips/epsf.tex
%{_datadir}/texmf/pdftex/plain/misc/pdfcolor.tex

%changelog
* Sat Jan 29 2005 Igor Zubkov <icesik@mail.ru> 4.6-los3
- use %%find_lang macros
- rebuild with new glibc

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 4.6-los2
- remove Vendor field.
- change Group to Development/Other
- add russian group description.

* Mon Nov 08 2004 Igor Zubkov <icesik@mail.ru> 4.6-los1
- Initial build for Los Angeles GNU/Linux.
