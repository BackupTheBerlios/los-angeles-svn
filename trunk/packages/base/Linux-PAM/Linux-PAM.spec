# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: --enable-prelude

%define sum		Linux PAM
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		Linux-PAM
%define ver		0.79
%define rel		los0.1
%define url		http://www.kernel.org/pub/linux/libs/pam/

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
Source2:	%{name}-%{version}-docs.tar.bz2
Source3:	%{name}-%{version}-docs.tar.bz2.sign
Source4:	FAQ
Patch0:		%{name}-0.78-los-build.patch
URL:		%{url}
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
%patch0 -p1

%build
./configure --host=%{_host} --build=%{_build} \
	    --target=%{_target_platform} \
	    --infodir=%{_infodir} \
	    --mandir=%{_mandir} \
	    --enable-static-libpam \
	    --with-mailspool=/var/mail \
	    --enable-suplementedir=/usr/lib
%{__make} %{_smp_mflags} OS_CFLAGS="${RPM_OPT_FLAGS}"

cp %{SOURCE4} .

%install
%{__make} FAKEROOT=${RPM_BUILD_ROOT} install

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/

cat > ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/login << "EOF"
# Begin /etc/pam.d/login
auth	requisite	pam_securetty.so
auth	requisite	pam_nologin.so
auth	required	pam_env.so
auth	required	pam_unix.so
account	required	pam_access.so
account	required	pam_unix.so
session	required	pam_motd.so
session	required	pam_limits.so
session	optional	pam_mail.so	dir=/var/mail standard
session	optional	pam_lastlog.so
session	required	pam_unix.so
# End /etc/pam.d/login
EOF

cat > ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/other << "EOF"
# Begin /etc/pam.d/other
auth		required	pam_deny.so
auth		required	pam_warn.so
account		required	pam_deny.so
session		required	pam_deny.so
password	required	pam_deny.so
password	required	pam_warn.so
# End /etc/pam.d/other
EOF

cat > ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/passwd << "EOF"
# Begin /etc/pam.d/passwd
password	required	pam_cracklib.so	\
    retry=3 difok=8 minlen=15 dcredit=3 ocredit=3 ucredit=2 lcredit=2
password	required	pam_unix.so	md5 shadow use_authtok
# End /etc/pam.d/passwd
EOF

cat > ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/shadow << "EOF"
# Begin /etc/pam.d/shadow
auth		sufficient	pam_rootok.so
auth		required	pam_unix.so
account		required	pam_unix.so
session		required	pam_unix.so
password	required	pam_permit.so
# End /etc/pam.d/shadow
EOF

cat > ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/su << "EOF"
# Begin /etc/pam.d/su
auth	sufficient	pam_rootok.so
auth	required	pam_unix.so
account	required	pam_unix.so
session	required	pam_unix.so
# End /etc/pam.d/su

cat > ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/useradd << "EOF"
# Begin /etc/pam.d/useradd
auth		sufficient	pam_rootok.so
auth		required	pam_unix.so
account		required	pam_unix.so
session		required	pam_unix.so
password	required	pam_permit.so
# End /etc/pam.d/useradd
EOF

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGELOG README pgp.keys.asc FAQ
%config(noreplace) %{_sysconfdir}/security/*
%config(noreplace) %{_sysconfdir}/pam.d/*
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
* Tue Apr 26 2005 Igor Zubkov <icesik@mail.ru> 0.79-los0
- update to 0.79.

* Tue Apr 19 2005 Igor Zubkov <icesik@mail.ru> 0.78-los0
- update to 0.78.

* Thu Jan 13 2005 Igor Zubkov <icesik@mail.ru> 0.77-los3
- fix up same rpmlint warnings and errors

* Tue Nov 23 2004 Igor Zubkov <icesik@mail.ru> 0.77-los2
- repackage to Linux-PAM and Linux-PAM-dev

* Sat Jun 19 2004 Igor Zubkov <icesik@mail.ru> 0.77-los1
- Initial build for Los Angeles GNU/Linux.
