# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Ext2/3 File System Programs and Utilities.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		e2fsprogs
%define ver		1.35
%define rel		los1
%define url		http://e2fsprogs.sourceforge.net/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{version}.tar.gz
URL:		%{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
E2fsprogs provides the filesystem utilities for use with the ext2 filesystem.
It also supports the ext3 filesystem with journaling support.

%package dev
Summary: Development files for E2fsprogs.
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description dev
Development files for E2fsprogs.

%prep
%setup -q

%build
%configure --with-root-prefix="" --enable-elf-shlibs --with-cc=gcc
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install-libs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc ABOUT-NLS COPYING ChangeLog INSTALL INSTALL.dllbin INSTALL.elfbin README RELEASE-NOTES
%{_bindir}/*
/sbin/*
/usr/sbin/*
/lib/evms/*
/lib/*.so.*
%{_libdir}/*.so
%doc %{_mandir}/man[18]/*
%doc %{_infodir}/*
%{_datadir}/locale/*/*/*
%{_datadir}/et/*
%{_datadir}/ss/*

%files dev
%defattr(-,root,root)
%{_libdir}/*.a
%doc %{_mandir}/man3/*
%{_includedir}/*/*

%changelog
* Fri May 14 2004 Igor Zubkov <icesik@mail.ru> 1.35-los1
- Initial build for Los Angeles GNU/Linux.
