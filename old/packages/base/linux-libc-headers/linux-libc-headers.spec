# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Linux Libc headers
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		linux-libc-headers
%define ver		2.6.10.0
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/C
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	i386

%description
Linux Libc headers

%prep
%setup -q
%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/asm/
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/linux/
cp -R include/asm-i386 ${RPM_BUILD_ROOT}%{_includedir}/asm/
cp -R include/linux ${RPM_BUILD_ROOT}%{_includedir}/
chown -R root:root ${RPM_BUILD_ROOT}%{_includedir}/{asm,linux}/
cd ${RPM_BUILD_ROOT}%{_includedir}/asm/
mv asm-i386 ../
cd ..
rm -rf asm
ln -s asm-i386 asm

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc doc/*
%{_includedir}/

%changelog
* Fri Jan 28 2005 Igor Zubkov <icesik@mail.ru> 2.6.10.0-los1
- update to 2.6.10.0

* Fri Dec 10 2004 Igor Zubkov <icesik@mail.ru> 2.6.9.1-los3
- another fix up build.

* Fri Dec 10 2004 Igor Zubkov <icesik@mail.ru> 2.6.9.1-los2
- fix up build.

* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 2.6.9.1-los1
- Initial build for Los Angeles GNU/Linux.
