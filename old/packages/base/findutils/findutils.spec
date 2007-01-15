# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		FindUtils
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		findutils
%define ver		4.2.18
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
FindUtils

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README README-alpha THANKS TODO
%{_bindir}/*
%{_libexecdir}/*
%doc %{_infodir}/*
%doc %{_mandir}/man[15]/*

%changelog
* Mon Feb 21 2005 Igor Zubkov <icesik@mail.ru> 4.2.18-los1
- update to 4.2.18.
- remove findutils-4.1.20-missing-newlines-1.patch.
- remove findutils-4.1.20-no-login-shell-1.patch.

* Sat Jun 05 2004 Igor Zubkov <icesik@mail.ru> 4.1.20-los2
- add patches from debian.

* Sun Feb 02 2004 Igor Zubkov <icesik@mail.ru> 4.1.20-los1
- Initial build for Los Angeles GNU/Linux.
