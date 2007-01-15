# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		cracklib
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		cracklib
%define ver		2.7
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	Artistic Licence
Group:		Base system
Source0:	http://www.users.dircon.co.uk/~crypto/download/cracklib,2.7.tgz
Source1:	crack.h
Source2:	create_cracklib_dict
Patch0:		cracklib,2.7-los1.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
cracklib

%prep
%setup -q -n cracklib,2.7
%patch0 -p1

%build
cp %{SOURCE1} .
cp %{SOURCE2} util/

cd cracklib
%{__make} %{_smp_mflags}
cd ..

cd util
%{__make} DICTPATH=/usr/lib/cracklib_dict
cd ..

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/
cp cracklib/libcrack.a ${RPM_BUILD_ROOT}%{_libdir}/
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/
cp crack.h ${RPM_BUILD_ROOT}%{_includedir}/
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}/
cp util/{mkdict,packer,create_cracklib_dict} ${RPM_BUILD_ROOT}%{_sbindir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name},%{version}

%files
%defattr(-,root,root)
%doc HISTORY LICENCE POSTER README
%{_includedir}/crack.h
%{_libdir}/libcrack.a
%{_sbindir}/*

%changelog
* Tue Dec 14 2004 Igor Zubkov <icesik@mail.ru> 2.7-los2
- little fixup of build.

* Thu Jun 17 2004 Igor Zubkov <icesik@mail.ru> 2.7-los1
- Initial build for Los Angeles GNU/Linux.
