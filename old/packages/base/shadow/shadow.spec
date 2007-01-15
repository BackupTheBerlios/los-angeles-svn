# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Shadow password file utilities for Linux.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		shadow
%define ver		4.0.7
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
CFLAGS="$RPM_OPT_FLAGS" \
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

%find_lang %{name}

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO doc contrib
%dir /etc/default
%config(noreplace) /etc/default/useradd
%config(noreplace) /etc/login.defs
%config(noreplace) /etc/securetty
/bin/*
/lib/*
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*
%doc %{_mandir}/man?/*
%lang(cs) %doc %{_mandir}/cs/man?/*
%lang(de) %doc %{_mandir}/de/man?/*
%lang(es) %doc %{_mandir}/es/man?/*
%lang(fr) %doc %{_mandir}/fr/man?/*
%lang(hu) %doc %{_mandir}/hu/man?/*
%lang(id) %doc %{_mandir}/id/man?/*
%lang(it) %doc %{_mandir}/it/man?/*
%lang(ja) %doc %{_mandir}/ja/man?/*
%lang(ko) %doc %{_mandir}/ko/man?/*
%lang(pl) %doc %{_mandir}/pl/man?/*
%lang(pt_BR) %doc %{_mandir}/pt_BR/man?/*
%lang(ru) %doc %{_mandir}/ru/man?/*
%lang(zh_CN) %doc %{_mandir}/zh_CN/man?/*
%lang(zh_TW) %doc %{_mandir}/zh_TW/man?/*

%changelog
* Mon Mar 28 2005 Igor Zubkov <icesik@mail.ru> 4.0.7-los1
- update to 4.0.7.

* Fri Dec 17 2004 Igor Zubkov <icesik@mail.ru> 4.0.6-los1
- Initial build for Los Angeles GNU/Linux.
