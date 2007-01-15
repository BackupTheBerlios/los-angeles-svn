# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean up after build!

%define sum		The GNU C library.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		glibc
%define ver		2.3.4
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.tar.bz2.sig
Source2:	nsswitch.conf
License:	GPL
Group:		System/Libraries
Group(ru_RU.KOI8-R):	Система/Библиотеки
URL:		http://www.gnu.org/software/libc/libc.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	linux-libc-headers >= 2.6.9.1
BuildRequires:	glibc-kernheaders

PreReq:		lost_stuff
BuildRequires:	lost_stuff
Requires:	lost_stuff

PreReq:		ldconfig

%description
Glibc  provides the  C  library  that  provides  the system calls and basic
functions such as open, malloc, printf, etc. The C library is used by
all dynamically linked programs.

The glibc package contains standard libraries which are used by
multiple programs on the system. In order to save disk space and
memory, as well as to make upgrading easier, common system code is
kept in one place and shared between programs. This particular package
contains the most important sets of shared libraries: the standard C
library and the standard math library. Without these two libraries, a
Linux system will not function.

%package dev
Summary: Development files for GNU Lib C.
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C

%description dev
Development files for GNU C library.

%package info
Summary: info files for GNU C library.
Group: Documentation
Group(ru_RU.KOI8-R): Документация

%description info
info files for GNU C library.

%package zoneinfo
Summary: zoneinfo files for GNU C library.
Group: System/Base
Group(ru_RU.KOI8-R): Система/База

%description zoneinfo
zoneinfo files for GNU C library.

%package doc
Summary: Documentation for GNU C library.
Group: Documentation
Group(ru_RU.KOI8-R): Документация

%description doc
Documentation for GNU C library

%package -n ldconfig
Summary: configure dynamic linker run time bindings
Group: System/Base
Group(ru_RU.KOI8-R): Система/База

%description -n ldconfig
ldconfig creates the necessary links and cache to the most
recent shared libraries found in the directories specified
on the command line, in the file /etc/ld.so.conf, and in
the trusted directories (/lib and /usr/lib). The cache is
used by the run-time linker, ld.so or ld-linux.so. ldconfig
checks the header and file names of the libraries it
encounters when determining which versions should have
their links updated.

%prep
%setup -q

%build
cd ${RPM_BUILD_DIR}
rm -rf build-%{name}
mkdir -p build-%{name}
cd ${RPM_BUILD_DIR}/build-%{name}/

../%{name}-%{ver}/configure \
	--host=%{_host} \
	--build=%{_build} \
	--target=%{_target_platform} \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--disable-profile \
	--enable-add-ons=nptl \
	--with-tls \
	--libexecdir=%{_libdir}/glibc \
	--without-cvs \
	--with-__thread \
	--enable-kernel=2.6.0 \
	--with-headers=/opt/glibc-kernheaders

%{__make} %{_smp_mflags}
#make check

%install
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/

cd ${RPM_BUILD_DIR}/build-%{name}
%{__make} install_root=${RPM_BUILD_ROOT} install
%{__make} install_root=${RPM_BUILD_ROOT} localedata/install-locales

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

# Don't include ld.so.cache
rm -f ${RPM_BUILD_ROOT}%{_sysconfdir}/ld.so.cache

# Include ld.so.conf
echo '/usr/lib' > ${RPM_BUILD_ROOT}%{_sysconfdir}/ld.so.conf
echo 'include ld.so.conf.d/*.conf' >> ${RPM_BUILD_ROOT}%{_sysconfdir}/ld.so.conf
chmod 644 ${RPM_BUILD_ROOT}%{_sysconfdir}/ld.so.conf
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/ld.so.conf.d

cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_sysconfdir}/

rm -f ${RPM_BUILD_ROOT}%{_sysconfdir}/localtime
cp -f ${RPM_BUILD_ROOT}%{_datadir}/zoneinfo/US/Eastern ${RPM_BUILD_ROOT}%{_sysconfdir}/localtime

# striping down all
cd ${RPM_BUILD_ROOT}/lib/
strip --strip-debug *.so
cd ${RPM_BUILD_ROOT}%{_libdir}/
strip --strip-debug *.a
cd ${RPM_BUILD_ROOT}%{_bindir}/
strip --strip-debug gencat getconf getent iconv lddlibc4 locale localedef pcprofiledump rpcgen sprof
cd ${RPM_BUILD_ROOT}%{_sbindir}/
strip --strip-debug *
cd ${RPM_BUILD_ROOT}%{_libdir}/gconv/
strip --strip-debug *.so
cd ${RPM_BUILD_ROOT}%{_libdir}/glibc/
strip --strip-debug pt_chown
cd getconf/
strip --strip-debug *
cd ${RPM_BUILD_ROOT}/sbin/
strip --strip-debug *

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/nsswitch.conf
%{_sysconfdir}/localtime
%{_sysconfdir}/rpc
/lib/*.so.*
/lib/*.so
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*.so
%{_libdir}/glibc/pt_chown
%{_libdir}/glibc/getconf/*
/sbin/sln
%{_libdir}/gconv/*.so
%{_libdir}/gconv/gconv-modules
%{_datadir}/i18n/charmaps/*
%{_datadir}/i18n/locales/*
%{_datadir}/locale/*/*/*
%{_datadir}/locale/locale.alias
%{_libdir}/locale/locale-archive

%files dev
%defattr(-,root,root)
%{_includedir}/
%{_libdir}/*.a
%{_libdir}/*.o

%files info
%defattr(-,root,root)
%{_infodir}/*

%files zoneinfo
%defattr(-,root,root)
%{_datadir}/zoneinfo/*

%files doc
%defattr(-,root,root)
%doc BUGS CONFORMANCE COPYING COPYING.LIB ChangeLog ChangeLog.* FAQ INSTALL
%doc INTERFACE LICENSES NAMESPACE NEWS NOTES PROJECTS README README.libm
%doc README.template

%files -n ldconfig
%defattr(-,root,root)
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/ld.so.conf
%dir /etc/ld.so.conf.d
/sbin/ldconfig

%changelog
* Sat Jan 29 2005 Igor Zubkov <icesik@mail.ru> 2.3.4-los1
- update to 2.3.4

* Mon Jan 17 2005 Igor Zubkov <icesik@mail.ru> 2.3.3-los3
- repackage.

* Tue Dec 14 2004 Igor Zubkov <icesik@mail.ru> 2.3.3-los2
- add lost_stuff to Requires.
- some clean up.
- strip all.

* Sat Nov 27 2004 Igor Zubkov <icesik@mail.ru> 2.3.3-los1
- repackage.
- update to 2.3.3

* Sat Feb 28 2004 Igor Zubkov <icesik@mail.ru> 2.3.2-los1
- Initial build for Los Angeles GNU/Linux.
