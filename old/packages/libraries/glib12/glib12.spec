# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A library of useful routines for C programming.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		glib
%define altname		glib
%define ver		1.2.10
%define rel		los1

Summary:	%{sum}
Name:		%{name}12
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	LGPL
Group:		base
Source0:	%{altname}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
glib 1.2

%package dev
Summary:	Development files from glib
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description dev
Development files from glib

%prep
%setup -q -n %{altname}-%{ver}

%build
%configure --enable-static --enable-shared

# dirty hack!
./ltconfig ltmain.sh %{_host}

%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{altname}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL NEWS README README.win32
%{_libdir}/*.so
%{_libdir}/*.so.*

%files dev
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_libdir}/glib/
%doc %{_mandir}/man1/*
%doc %{_infodir}/*
%{_includedir}/glib-1.2/*.h
%{_datadir}/aclocal/*

%changelog
* Thu Nov 04 2004 Igor Zubkov <icesik@mail.ru> 1.2.10-los1
- Initial build for Los Angeles GNU/Linux.
