# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: build docs

%define sum		Debian's Advanced Packaging Tool with RPM support.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		apt
%define ver		0.5.15cnc6
%define rel		los3
%define url		https://moin.conectiva.com.br/AptRpm

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.bz2
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libreadline5
BuildRequires:	libreadline5-dev

Requires:	libz
BuildRequires:	libz-dev

BuildRequires:	bzip2-dev
BuildRequires:	task-c++-devel
BuildRequires:	librpm-dev
BuildRequires:	libpopt-dev

Requires:	libapt = %{version}-%{release}
Requires:	gnupg
Requires:	lost-gpgkeys

%description
A port of Debian's APT tools for RPM based distributions,
or at least for Conectiva. It provides the apt-get utility that
provides a simpler, safer way to install and upgrade packages.
APT features complete installation ordering, multiple source
capability and several other unique features.

%package -n libapt
Summary: APT's core libraries
Group: System/Libraries
Group(ru_RU.KOI8-R): Система/Библиотеки

%description -n libapt
This package contains APT's package manipulation library,
modified for RPM.

%package -n libapt-dev
Summary: Development files and documentation for APT's core libs
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: libapt = %{version}-%{release}, librpm-dev

%description -n libapt-dev
This package contains the header files and libraries for developing with
APT's package manipulation library, modified for RPM.

%package -n libapt-static-dev
Summary: Development static library for APT's libs
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: libapt-dev = %{version}-%{release}, librpm-static-dev

%description -n libapt-static-dev
This package contains static libraries for developing with APT's
package manipulation library, modified for RPM.

%package utils
Summary: Utilities to create APT repositaries (the indices)
Group: Development/Other
Requires: %{name} = %{version}-%{release}
Requires: mktemp
Requires: gnupg
Requires: sed
Requires: diffutils

%description utils
This package contains the utility programs that can prepare a repositary of
RPMS binary and source packages for future access by APT (by generating
the indices).

It relates to 'apt' package analoguously to how 'rpm' relates to 'rpm-build'
package.

%prep
%setup -q

%build
%configure --disable-scripts --disable-docs
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%find_lang %{name}

mkdir -p ${RPM_BUILD_ROOT}/etc/apt/
mkdir -p ${RPM_BUILD_ROOT}/var/lib/apt/lists/
mkdir -p ${RPM_BUILD_ROOT}/var/lib/apt/lists/partial
mkdir -p ${RPM_BUILD_ROOT}/var/cache/apt/archives/partial

%post   -n libapt -p /sbin/ldconfig
%postun -n libapt -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS AUTHORS.RPM COPYING TODO doc/examples contrib
%{_bindir}/apt-*
%{_libdir}/apt/methods/*
/etc/apt/
/var/lib/apt/lists/
/var/lib/apt/lists/partial
/var/cache/apt/archives/partial

%files utils
%defattr(-,root,root)
%{_bindir}/*
%exclude %{_bindir}/apt-*

%files -n libapt
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n libapt-dev
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/apt-pkg/*.h

%files -n libapt-static-dev
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Wed Mar 30 2005 Igor Zubkov <icesik@mail.ru> 0.5.15cnc6-los3
- some fixes.
- rebuild with new libreadline 5.0.

* Wed Nov 24 2004 Igor Zubkov <icesik@mail.ru> 0.5.15cnc6-los2
- repackage.

* Wed Jun 09 2004 Igor Zubkov <icesik@mail.ru> 0.5.15cnc6-los1
- Initial build for Los Angeles GNU/Linux.
