# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Library for handling TIFF files.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		libtiff
%define ver		3.7.1
%define rel		los1.1
%define url		http://www.remotesensing.org/libtiff/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/libtiff/tiff-%{version}.tar.gz
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

#BuildRequires:	glut-devel
Requires:	libjpeg
BuildRequires:	libjpeg-dev
Requires:	libz
BuildRequires:	libz-dev

BuildRequires:	task-c++-devel

%description
This package is a library of functions that manipulate TIFF images.

%package dev
Summary:	Header files for developing programs using libtiff.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
This package is all you need to develop programs that manipulate tiff
images.

%package progs
Summary:	Simple clients for manipulating tiff images.
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating tiff images.

%prep
%setup  -q -n tiff-%{version}

%build
%configure \
	--enable-static \
	--enable-cxx=no \
	--enable-ccitt \
	--enable-packbits \
	--enable-lzw \
	--enable-thunder \
	--enable-next \
	--enable-logluv \
	--enable-zlib \
	--enable-pixarlog \
	--enable-jpeg
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
cd ${RPM_BUILD_ROOT}%{_docdir}/
rm -rf tiff-%{ver}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/tiff-%{version}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYRIGHT README*
%{_libdir}/lib*.so.*

%files dev
%defattr(-,root,root)
%doc ChangeLog html/* TODO
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/*
%{_man3dir}/*

%files progs
%defattr(-,root,root)
%{_bindir}/*
%{_man1dir}/*

%changelog
* Mon Mar 21 2005 Igor Zubkov <icesik@mail.ru> 3.7.1-los1
- Initial build for Los Angeles GNU/Linux.
