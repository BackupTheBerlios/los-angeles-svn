# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Shadow password file utilities for Linux.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		shadow
%define ver		4.0.6
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	BSD
Group:		System/Base
Source0:	%{name}-%{ver}.tar.bz2
Source1:	securetty
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	Linux-PAM-dev
Requires:	Linux-PAM

%description
This package includes the programs necessary to convert traditional
V7 UNIX password files to the SVR4 shadow password format and additional
tools to work with shadow passwords.
	- 'pwconv' converts everything to the shadow password format.
	- 'pwunconv' converts back to non-shadow passwords.
	- 'pwck' checks the integrity of the password and shadow files.
	- 'lastlog' prints out the last login times of all users.
	- 'useradd', 'userdel', 'usermod' to manage user accounts.
	- 'groupadd', 'groupdel', 'groupmod' to manage groups.

A number of man pages are also included that relate to these utilities,
and shadow passwords in general.

%prep
%setup -q

%build
./configure --host=%{_host} --build=%{_build} \
            --target=%{_target_platform} \
	    --prefix=%{_prefix} \
	    --mandir=%{_mandir} \
	    --enable-shared \
	    --enable-static \
	    --with-libpam \
	    --without-libcrack
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

mkdir -p ${RPM_BUILD_ROOT}/etc/default

cp %{SOURCE1} ${RPM_BUILD_ROOT}/etc/securetty
cp etc/useradd ${RPM_BUILD_ROOT}/etc/default/useradd
sed 's%/var/spool/mail%/var/mail%' etc/login.defs.linux > ${RPM_BUILD_ROOT}/etc/login.defs

cd ${RPM_BUILD_ROOT}%{_sbindir}
#ln -sf vipw vigr
#rm ${RPM_BUILD_ROOT}/bin/vipw
#mv ${RPM_BUILD_ROOT}/bin/sg ${RPM_BUILD_ROOT}%{_bindir}

mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/

mv ${RPM_BUILD_ROOT}/lib/libshadow.{a,la} ${RPM_BUILD_ROOT}%{_libdir}

cd ${RPM_BUILD_ROOT}%{_libdir}
ln -sf ../../lib/libshadow.so

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ABOUT-NLS ChangeLog NEWS README TODO doc
%dir /etc/default
%config /etc/default/useradd
%config /etc/login.defs
%config(noreplace) /etc/securetty
/bin/*
%{_bindir}/*
%{_sbindir}/*
/lib/*
%{_libdir}/*
%{_datadir}/locale/*/*/shadow.mo
%doc %{_mandir}/cs/man?/*
%doc %{_mandir}/de/man?/*
%doc %{_mandir}/es/man?/*
%doc %{_mandir}/fr/man?/*
%doc %{_mandir}/hu/man?/*
%doc %{_mandir}/id/man?/*
%doc %{_mandir}/it/man?/*
%doc %{_mandir}/ja/man?/*
%doc %{_mandir}/ko/man?/*
%doc %{_mandir}/man?/*
%doc %{_mandir}/pl/man?/*
%doc %{_mandir}/pt_BR/man?/*
%doc %{_mandir}/ru/man?/*
%doc %{_mandir}/zh_CN/man?/*
%doc %{_mandir}/zh_TW/man?/*

%changelog
* Fri Dec 17 2004 Igor Zubkov <icesik@mail.ru> 4.0.6-los1
- Initial build for Los Angeles GNU/Linux.
