# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Xdelta -- A binary delta generator
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		xdelta
%define ver		1.1.3
%define rel		los1
%define url		http://xdelta.sourceforge.net/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.gz
URL:		%{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libz
BuildRequires:	libz-dev
Requires:	glib12
BuildRequires:	glib12-dev

Requires:	libxdelta

%description
Xdelta is an application program designed to compute changes between files.
These changes (deltas) are similar to the output of the "diff" program in 
that they may be used to store and transmit only the changes between files.
However, unlike diff, the output of Xdelta is not expressed in a 
human-readable format--Xdelta can also also apply these deltas to a copy of 
the original file.  Xdelta uses a fast, linear algorithm and performs well
on both binary and text files.

%package -n libxdelta
Summary: libxdelta
Group: System/Libraries
Group(ru_RU.KOI8-R): Система/Библиотеки

%description -n libxdelta
libxdelta

%package -n libxdelta-dev
Summary: Development files for libxdelta.
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: lib%{name} = %{version}-%{release}

%description -n libxdelta-dev
Development files for libxdelta.

%description -n libxdelta-dev -l ru_RU.KOI8-R
Разработческие файлы для libxdelta.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post -n libxdelta -p /sbin/ldconfig
%postun -n libxdelta  -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/xdelta
%doc %{_man1dir}/xdelta.*

%files -n libxdelta
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files -n libxdelta-dev
%defattr(-,root,root)
%{_bindir}/xdelta-config
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_datadir}/aclocal/xdelta.m4

%changelog
* Thu Jan 13 2005 Igor Zubkov <icesik@mail.ru> 1.1.3-los1
- Initial build for Los Angeles GNU/Linux.
