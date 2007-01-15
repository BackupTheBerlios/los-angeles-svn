# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		XviD - MPEG-4 video codec.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		libxvid
%define altname		xvid
%define ver		1.0.0
%define rel		los1
%define url		http://www.xvid.org

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Library
Source0:	%{altname}core-%{version}.tar.bz2
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	nasm

%description
XviD is a high performance and high quality MPEG-4 video de-/encoding solution.

%package dev
Summary: Development files of XviD video codec.
Group: Development
Requires: %{name} = %{version}-%{release}

%description dev
Development files of XviD video codec.

%prep
%setup -q -n %{altname}core-%{ver}

%build
cd build/generic
%configure
%{__make} %{_smp_mflags}

%install
cd build/generic
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{altname}core-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_libdir}/*.so.*

%files dev
%defattr(-,root,root)
%doc CodingStyle doc
%{_libdir}/*.a
%{_includedir}/*

%changelog
* Sun May 30 2004 Igor Zubkov <icesik@mail.ru> 1.0.0-los1
- Initial build for Los Angeles GNU/Linux.
