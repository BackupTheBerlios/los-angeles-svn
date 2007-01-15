# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Ogg Bitstream Library.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		libogg
%define ver		1.1.2
%define rel		los1
%define url		http://www.xiph.org/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	BSD
Group:		Library
Source0:	http://www.vorbis.com/files/1.0.1/unix/%{name}-%{ver}.tar.gz
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Libogg is a library for manipulating ogg bitstreams.  It handles
both making ogg bitstreams and getting packets from ogg bitstreams.

%package dev
Summary: Ogg Bitstream Library Development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description dev
The libogg-dev package contains the header files, static libraries
and documentation needed to develop applications with libogg.

%prep
%setup -q

%build
%configure --enable-static
make

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES COPYING README
%{_libdir}/*.so.*

%files dev
%defattr(-,root,root)
%doc doc/index.html
%doc doc/framing.html
%doc doc/oggstream.html
%doc doc/white-ogg.png
%doc doc/white-xifish.png
%doc doc/stream.png
%doc doc/ogg/*.html
%doc doc/ogg/style.css
%{_includedir}/ogg/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4

%changelog
* Sun Jan 16 2005 Igor ZUbkov <icesik@mail.ru> 1.1.2-los1
- update to a new stable release 1.1.2

* Tue Nov 16 2004 Igor Zubkov <icesik@mail.ru> 1.1-los1
- Initial build for Los Angeles GNU/Linux.
