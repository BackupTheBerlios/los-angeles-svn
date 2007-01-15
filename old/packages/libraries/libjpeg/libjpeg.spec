# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Library for handling different jpeg files.
%define sum_ru		Библиотека для обработки различных jpeg-файлов.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		libjpeg
%define ver		6b
%define rel		los1
%define url		http://www.ijg.org/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The libjpeg package contains a library of functions for manipulating
JPEG images.

%description -l ru_RU.KOI8-R
Библиотека функций для обработки jpeg-изображений и простые клиенты
для такой обработки.

%package dev
Summary:	Headers for developing programs using libjpeg.
Summary(ru):	Хедеры и библиотека для разработки программ, использующих libjpeg.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
The libjpeg-devel package includes the header files and static
libraries necessary for developing programs which will manipulate JPEG
files using the libjpeg library.

If you are going to develop programs which will manipulate JPEG
images, you should install libjpeg-devel. You'll also need to have the
libjpeg package installed.

%description dev -l ru_RU.KOI8-R
В этом пакете содержится все необходимое для разработки программ,
которые работают с jpeg-изображениями включая документацию.

%package progs
Summary:	Simple clients for manipulating jpeg images.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating jpeg images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%prep
%setup -q -n jpeg-%{version}

%build
%configure \
	--enable-static \
	--enable-shared
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_man1dir}
%makeinstall mandir=${RPM_BUILD_ROOT}%{_man1dir}/

install jversion.h ${RPM_BUILD_ROOT}%{_includedir}

# remove HAVE_STD{DEF,LIB}_H
# (not necessary but may generate warnings confusing autoconf)
(cd ${RPM_BUILD_ROOT}%{_includedir}
grep -v 'HAVE_STD..._H' jconfig.h > jconfig.h.new
mv -f jconfig.h.new jconfig.h
)

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/jpeg-%{version}

%files
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files dev
%defattr(-,root,root)
%doc {libjpeg,structure}.doc
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/*.h

%files progs
%defattr(-,root,root)
%{_bindir}/*
%doc %{_man1dir}/*

%changelog
* Tue Mar 22 2005 Igor Zubkov <icesik@mail.ru> 6b-los1
- Initial build for Los Angeles GNU/Linux.
