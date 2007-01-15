# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		CPU identification utility.
%define sum_ru		Утилита идентификации CPU.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		cpuid
%define ver		3.3
%define rel		los1
%define url		http://www.ka9q.net/code/cpuid/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	free
Group:		Utils
Source0:	http://www.ka9q.net/code/cpuid/%{name}-%{ver}.tar.gz
Url:		%{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This is a fairly complete CPU identification utility. 
It has been tested on several Intel, AMD and Cyrix CPUs. 
If the Pentium III serial number misfeature is present and enabled,
this program will display it.

%prep
%setup -q

%build
%{__make} CC=gcc %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}/bin

install -c -m 755 cpuid ${RPM_BUILD_ROOT}/bin

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
/bin/cpuid

%changelog
* Mon Nov 29 2004 Igor Zubkov <icesik@mail.ru> 3.3-los1
- Initial build for Los Angeles GNU/Linux.
