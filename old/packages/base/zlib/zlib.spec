# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU Compression Libraries.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		libz
%define altname		zlib
%define ver		1.2.2
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	BSD
Group:		System/Libraries
Group(ru_RU.KOI8-R):	Система/Библиотеки
Source0:	%{altname}-%{version}.tar.bz2
Patch0:		%{altname}-1.2.1-security-1.patch
URL:		http://www.gzip.org/zlib/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The  Zlib  package  contains  the  zlib library, which is used by many
programs for its compression and uncompression functions.

%package dev
Summary: Development files for zlib
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: %{name} = %{ver}-%{rel}

%description dev
Development files for zlib

%package doc
Summary: Documentation for zlib
Group: Documentation
Group(ru_RU.KOI8-R): Документация

%description doc
Documentation for zlib.

%prep
%setup -q -n %{altname}-%{ver}
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --shared
%{__make} %{_smp_mflags}
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}
%{__make} %{_smp_mflags}
%{__make} test || exit 1

%install
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/
mkdir -p ${RPM_BUILD_ROOT}/lib/
mkdir -p ${RPM_BUILD_ROOT}%{_man3dir}/
cp zlib.h zconf.h ${RPM_BUILD_ROOT}%{_includedir}/
chmod 644 ${RPM_BUILD_ROOT}%{_includedir}/zlib.h ${RPM_BUILD_ROOT}%{_includedir}/zconf.h
cp libz.so.1.2.2 ${RPM_BUILD_ROOT}/lib/
cd ${RPM_BUILD_ROOT}/lib/; chmod 755 libz.so.1.2.2
ln -s libz.so.1.2.2 libz.so
ln -s libz.so.1.2.2 libz.so.1
cd ${RPM_BUILD_DIR}/
cd %{altname}-%{ver}/
cp zlib.3 ${RPM_BUILD_ROOT}%{_man3dir}/
chmod 644 ${RPM_BUILD_ROOT}%{_man3dir}/zlib.3
cp libz.a ${RPM_BUILD_ROOT}%{_libdir}/
ln -sf ../../lib/libz.so.1 ${RPM_BUILD_ROOT}%{_libdir}/libz.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{altname}-%{version}

%files
%defattr(-,root,root)
/lib/*
%exclude /lib/*.so

%files dev
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%doc %{_man3dir}/*

%files doc
%defattr(-,root,root)
%doc ChangeLog FAQ INDEX README algorithm.txt

%changelog
* Thu Mar 24 2005 Igor Zubkov <icesik@mail.ru> 1.2.2-los1
- update to 1.2.2.
- clean --target build.
- clean spec file.
- drop backward compitable packages zlib, zlib-dev and zlib-doc.

* Tue Feb 01 2005 Igor Zubkov <icesik@mail.ru> 1.2.1-los4
- security fix - CAN-2004-0797.

* Mon Jan 10 2005 Igor Zubkov <icesik@mail.ru> 1.2.1-los3
- rename zlib -> libz.
- rename zlib-dev -> libz-dev.
- rename zlib-doc -> libz-doc.
- make zlib, zlib-dev and zlib-doc empty and requires libz, libz-dev
- and libz-doc.

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 1.2.1-los2
- clean up Group information.
- correct depends information.
- remove Vendor field.

* Mon May 10 2004 Igor Zubkov <icesik@mail.ru> 1.2.1-los1
- Initial build for Los Angeles GNU/Linux.
