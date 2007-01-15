# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Text file format converter.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		dos2unix
%define ver		3.1
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	Freely distributable
Group:		Utils
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}.patch
Patch1:		%{name}-%{version}-segfault.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Dos2unix converts DOS or MAC text files to UNIX format.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make clean
make CFLAGS="${RPM_OPT_FLAGS}"
make link

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_man1dir}/

install -m755 dos2unix ${RPM_BUILD_ROOT}%{_bindir}
install -m755 mac2unix ${RPM_BUILD_ROOT}%{_bindir}
install -m444 dos2unix.1 ${RPM_BUILD_ROOT}%{_man1dir}/
install -m444 mac2unix.1 ${RPM_BUILD_ROOT}%{_man1dir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root,0755)
%doc COPYRIGHT INSTALL
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%doc %{_man1dir}/*

%changelog
* Tue Jun 01 2004 Igor Zubkov <icesik@mail.ru> 3.1-los1
- Initial build for Los Angeles GNU/Linux.
