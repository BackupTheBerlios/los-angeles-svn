# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A development library for text mode user interfaces.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		newt
%define ver		0.50.39
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

Requires:	slang
BuildRequires:	slang-dev

%description
Newt is a programming library for color text mode, widget based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
checkboxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces.  This package also contains the
shared library needed by programs built with newt, as well as a
/usr/bin/dialog replacement called whiptail.  Newt is based on the
slang library.

%prep
%setup -q

%build
%configure
%{__make} CC=%{__cc}

%install
%{__make} CC=%{__cc} instroot=${RPM_BUILD_ROOT} install

%post -p   /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_bindir}/whiptail
%{_includedir}/newt.h
%{_libdir}/lib*.so
%{_libdir}/lib*.so.*
%{_libdir}/lib*.a
%{_libdir}/python2.2/*/*

%changelog
* Tue Feb 08 2005 Igor Zubkov <icesik@mail.ru> 0.50.39-los1
- Initial build for Los Angeles GNU/Linux.
