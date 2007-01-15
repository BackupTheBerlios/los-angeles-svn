# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Library for PNG pictures.
%define sum_ru		���������� ��� ��������� PNG ������.
%define maintainer	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		libpng
%define ver		1.2.5
%define rel		los1

Summary:	%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Libraries
Group(ru_RU.KOI8-R):	�������/����������
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-link-to-proper-libs.patch
Patch1:		%{name}-%{version}-mans.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libz-dev

%package dev
Group:		Development/Libraries
Group(ru_RU.KOI8-R):	����������/����������
Summary:	Development files for libpng
Summary(ru_RU.KOI8-R):	�������� ��� ���������� ��������� libpng
Requires: pkgconfig

%description
The libpng package contains libraries used by other programs for reading and 
writing PNG files.

%description -l ru_RU.KOI8-R
����� libpng �������� ����������, ������������ ������� ����������� ��� ������ 
� ������ PNG ������.

%description dev
The libpng-dev package contains static libraries and headers to develope 
programs that uses libpng.

%description -l ru_RU.KOI8-R dev
����� libpng �������� ����������� ������������ ���������� � ������������ �����
��� ���������� ����������, ������������ libpng.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
%{__make} %{_smp_mflags} prefix=/usr ZLIBINC=/usr/include \
     ZLIBLIB=/usr/lib -f scripts/makefile.linux

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/share/man
%{__make} prefix=${RPM_BUILD_ROOT}/usr install -f scripts/makefile.linux

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README KNOWNBUG INSTALL TODO 
%{_libdir}/*.so*
%doc %{_man3dir}/*
%doc %{_man5dir}/*

%files dev
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_bindir}/*
%{_libdir}/pkgconfig/*

%changelog
* Fri Oct 29 2004 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 1.2.11-los1
- Initial build for Los-Angeles Linux
