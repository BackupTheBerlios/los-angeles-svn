# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		unix2dos - UNIX to DOS text file format converter.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		unix2dos
%define ver		2.2
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	distributable
Group:		Unknown
Source0:	unix2dos-2.2.src.tar.gz
Patch0:		unix2dos-mkstemp.patch
Patch1:		unix2dos-2.2-segfault.patch
Patch2:		unix2dos-2.2-manpage.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%prep
%setup -q -c
%patch -p1
%patch1 -p1
%patch2 -p1

%description
A utility that converts plain text files in UNIX format to DOS format.

%build
gcc ${RPM_OPT_FLAGS} -o unix2dos unix2dos.c

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1/

install -m755 unix2dos ${RPM_BUILD_ROOT}%{_bindir}/
install -m444 unix2dos.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root,0755)
%doc COPYRIGHT
%{_bindir}/unix2dos
%doc %{_mandir}/*/*

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 2.2-los2
- remove Vendor field.

* Tue Jun 01 2004 Igor Zubkov <icesik@mail.ru> 2.2-los1
- Initial build for Los Angeles GNU/Linux.
