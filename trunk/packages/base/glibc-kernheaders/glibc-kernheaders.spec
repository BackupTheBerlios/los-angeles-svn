# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Glibc kernel headers.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		glibc-kernheaders
%define ver		2.6.11
%define fullver		2.6.11.4
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{fullver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development
Source0:	linux-%{ver}.tar.bz2
Patch0:		patch-2.6.11.4.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

AutoReq:	off

%description
Glibc kernel headers.

Warning: this is package need only if you want compile glibc
from srpm.

%prep
%setup -q -n linux-%{ver}
%patch0 -p1

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
rm -rf %{_builddir}/linux-%{ver}

%files
%defattr(-,root,root)
/opt/glibc-kernheaders/

%changelog
* Sun Mar 27 2005 Igor Zubkov <icesik@mail.ru> 2.6.11.4-los1
- update to 2.6.11.4.

* Thu Nov 25 2004 Igor Zubkov <icesik@mail.ru> 2.6.9-los1
- Initial build for Los Angeles GNU/Linux.
