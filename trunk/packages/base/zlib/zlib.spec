# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean build for non i686

%define sum		The GNU Compression Libraries
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		zlib
%define ver		1.2.1
%define rel		los4

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	BSD
Group:		System/Libraries
Group(ru_RU.KOI8-R):	Система/Библиотеки
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-security-1.patch
URL:		http://www.gzip.org/zlib/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libz = %{ver}-%{rel}

%description
The  Zlib  package  contains  the  zlib library, which is used by many
programs for its compression and uncompression functions.

Backward compatible.

%package dev
Summary: Development files for zlib
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: libz-dev = %{ver}-%{rel}

%description dev
Development files for zlib

Backward compatible.

%package doc
Summary: Documentation for zlib
Group: Documentation
Group(ru_RU.KOI8-R): Документация
Requires: libz-doc = %{ver}-%{rel}

%description doc
Documentation for zlib.

Backward compatible.

%package -n libz
Summary: The GNU Compression Libraries
Group: System/Libraries
Group(ru_RU.KOI8-R): Система/Библиотеки

%description -n libz
The  Zlib  package  contains  the  zlib library, which is used by many
programs for its compression and uncompression functions.

%package -n libz-dev
Summary: Development files for zlib
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: libz = %{ver}-%{rel}

%description -n libz-dev
Development files for zlib

%package -n libz-doc
Summary: Documentation for zlib
Group: Documentation
Group(ru_RU.KOI8-R): Документация

%description -n libz-doc
Documentation for zlib.

%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=%{_prefix} --shared
%{__make} %{_smp_mflags}
./configure --prefix=%{_prefix}
%{__make} %{_smp_mflags}
%{__make} test || exit 1

%install
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/
mkdir -p ${RPM_BUILD_ROOT}/lib/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man3/
cp zlib.h zconf.h ${RPM_BUILD_ROOT}%{_includedir}/
chmod 644 ${RPM_BUILD_ROOT}%{_includedir}/zlib.h ${RPM_BUILD_ROOT}%{_includedir}/zconf.h
cp libz.so.1.2.1 ${RPM_BUILD_ROOT}/lib/
cd ${RPM_BUILD_ROOT}/lib/; chmod 755 libz.so.1.2.1
ln -s libz.so.1.2.1 libz.so
ln -s libz.so.1.2.1 libz.so.1
cd ${RPM_BUILD_DIR}/
cd %{name}-%{ver}/
cp zlib.3 ${RPM_BUILD_ROOT}%{_mandir}/man3/
chmod 644 ${RPM_BUILD_ROOT}%{_mandir}/man3/zlib.3
cp libz.a ${RPM_BUILD_ROOT}%{_libdir}/
ln -sf ../../lib/libz.so.1 ${RPM_BUILD_ROOT}%{_libdir}/libz.so

%post -n libz -p /sbin/ldconfig
%postun -n libz -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)

%files dev
%defattr(-,root,root)

%files doc
%defattr(-,root,root)

%files -n libz
%defattr(-,root,root)
/lib/*
%exclude /lib/*.so

%files -n libz-dev
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%doc %{_man3dir}/*

%files -n libz-doc
%defattr(-,root,root)
%doc ChangeLog FAQ INDEX README algorithm.txt

%changelog
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
