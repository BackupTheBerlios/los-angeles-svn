# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Glibc kernel headers.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		glibc-kernheaders
%define ver		2.6.9
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development
Source0:	linux-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

AutoReq:	off

%description
Glibc kernel headers.

Warning: this is package need only if you want compile glibc
from srpm.

%prep
%setup -q -n linux-%{ver}

%build
%{__make} mrproper
%{__make} include/linux/version.h
%{__make} include/asm

%install
mkdir -p ${RPM_BUILD_ROOT}/opt/glibc-kernheaders
cp -HR include/asm ${RPM_BUILD_ROOT}/opt/glibc-kernheaders/
cp -R include/asm-generic ${RPM_BUILD_ROOT}/opt/glibc-kernheaders/
cp -R include/linux ${RPM_BUILD_ROOT}/opt/glibc-kernheaders/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/linux-%{version}

%files
%defattr(-,root,root)
/opt/glibc-kernheaders/

%changelog
* Thu Nov 25 2004 Igor Zubkov <icesik@mail.ru> 2.6.9-los1
- Initial build for Los Angeles GNU/Linux.
