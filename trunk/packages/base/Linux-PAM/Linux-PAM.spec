# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Linux PAM
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		Linux-PAM
%define ver		0.77
%define rel		los3

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Libraries
Group(ru_RU.KOI8-R):	Система/Библиотеки
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.tar.bz2.sign
URL:		http://www.kernel.org/pub/linux/libs/pam/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	cracklib
Requires:	cracklib
Requires:	words

%description
Linux PAM nothing else ;-)

%package dev
Summary: Development files for Linux-PAM.
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: %{name} = %{version}-%{release}

%description dev
Development files for Linux-PAM.

%prep
%setup -q

%build
./configure --host=%{_host} --build=%{_build} \
	    --target=%{_target_platform} \
	    --infodir=%{_infodir} \
	    --mandir=%{_mandir} \
	    --enable-static-libpam \
	    --with-mailspool=/var/mail \
	    --enable-suplementedir=/usr/lib
%{__make} %{_smp_mflags}

%install
%{__make} FAKEROOT=${RPM_BUILD_ROOT} install
cd ${RPM_BUILD_ROOT}/lib
ln -s libpam.so.0.77 libpam.so.0
ln -s libpam_misc.so.0.77 libpam_misc.so.0
ln -s libpamc.so.0.77 libpamc.so.0

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGELOG README pgp.keys.asc
%config(noreplace) %{_sysconfdir}/security/*
/lib/security/
/lib/*.so.*
%{_libdir}/*
%doc %{_man8dir}/*
#%doc %{_docdir}/*/*/*

%files dev
%defattr(-,root,root)
/lib/*.a
/lib/*.so
%{_includedir}/security/*
%doc %{_man3dir}/*

%changelog
* Thu Jan 13 2005 Igor Zubkov <icesik@mail.ru> 0.77-los3
- fix up same rpmlint warnings and errors

* Tue Nov 23 2004 Igor Zubkov <icesik@mail.ru> 0.77-los2
- repackage to Linux-PAM and Linux-PAM-dev

* Sat Jun 19 2004 Igor Zubkov <icesik@mail.ru> 0.77-los1
- Initial build for Los Angeles GNU/Linux.
