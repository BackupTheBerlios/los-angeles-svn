# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean up spec
# TODO: проверить правильность copyright (copyletf)

%define rpm_name	rpm
%define rpm_ver		4.1
%define rel		los6

Summary:		The RPM package management system.
Summary(ru_RU.KOI8-R):	Менеджер пакетов RPM.
Name:			%{rpm_name}
Version:		%{rpm_ver}
Release:		%{rel}
Packager:		Igor Zubkov <icesik@mail.ru>
Source0:		rpm-4.1.tar.gz
Patch0:			rpm-4.1-los.patch
Patch1:			rpm-4.1-python2.2.patch
Patch2:			rpm-4.1-macros.patch
Patch3:			rpm-4.1-macros2.patch
Patch4:			rpm-4.1-los-kdemacros.patch
License:		GPL
Group:			System/Base
Group(ru_RU.KOI8-R):	Система/База
URL:			http://www.rpm.org/
BuildRoot:		%{_tmppath}/%{name}-%{version}-buildroot

Requires: librpm = %{rpm_ver}-%{rel}
Requires: libpopt = 1.7-%{rel}
Requires: libbeecrypt = 2.2.0-%{rel}

Requires: rpm-macros >= 0.1-los1

Requires: file

#BuildRequires:	python2.2
BuildRequires: python
BuildRequires: doxygen

BuildRequires: libz-dev

Requires: diffutils

BuildRequires: patch

%description
The RPM package management system.

%package build
Summary: Scripts and executable programs used to build packages.
Group: Development/RPM
Group(ru_RU.KOI8-R): Разработка/RPM
Requires: rpm = %{rpm_ver}-%{rel}
Requires: patch
Provides: perl(Specfile)

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

%package -n libpopt
Summary: A C library for parsing command line parameters.
Group: System/Libraries
Group(ru_RU.KOI8-R): Система/Библиотеки
License: X Consortium
Version: 1.7

%description -n libpopt
Popt is a C library for parsing command line parameters.  Popt
was heavily influenced by the getopt() and getopt_long() functions,
but it improves on them by allowing more powerful argument expansion.
Popt can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments.  Popt allows command
line arguments to be aliased via configuration files and includes
utility functions for parsing arbitrary strings into argv[] arrays
using shell-like rules.

Install popt if you're a C programmer and you'd like to use its
capabilities.

%package -n libpopt-dev
Summary: Popt library headers
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Version: 1.7
License: X Consortium
Requires: libpopt = 1.7-%{rel}

%description -n libpopt-dev
Popt library headers.

%package -n libbeecrypt
Summary: An open source cryptography library.
Group: System/Libraries
Group(ru_RU.KOI8-R): Система/Библиотеки
License: LGPL
Version: 2.2.0
URL: http://www.sourceforge.net/projects/beecrypt/

%description -n libbeecrypt
The BeeCrypt Cryptography Library.

%package -n libbeecrypt-dev
Summary: The BeeCrypt Cryptography Library headers
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
License: LGPL
Version: 2.2.0
URL: http://www.sourceforge.net/projects/beecrypt/
Requires: libbeecrypt = 2.2.0-%{rel}

%description -n libbeecrypt-dev
The BeeCrypt Cryptography Library headers.

%package -n libelf-dev
Summary: An ELF object file access library.
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
License: distributable
Version: 0.8.2

%description -n libelf-dev
The libelf-devel package contains a library for accessing ELF object
files. Libelf allows you to access the internals of the ELF object file
format, so you can see the different sections of an ELF file.

%package -n librpm
Summary: Librpm
Group: System/Libraries
Group(ru_RU.KOI8-R): Система/Библиотеки
License: LGPL

%description -n librpm
Librpm

%package -n librpm-dev
Summary: Librpm development files.
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
License: LGPL

%description -n librpm-dev
Librpm development files.

%package -n librpm-static-dev
Summary: Librpm static library.
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
License: LGPL

%description -n librpm-static-dev
Librpm static library.

%package python
Summary: Python bindings for apps which will manipulate RPM packages.
Group: Development/Python
Group(ru_RU.KOI8-R): Разработка/Python
Requires: %{rpm_name} = %{rpm_ver}-%{rel}
#Requires: python2.2
Requires: python

%description python
The rpm-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the RPM Package Manager libraries.

This package should be installed if you want to develop Python
programs that will manipulate RPM packages and databases.

%package docs
Summary: doxygen documentation for rpm.
Group: Documentation
Group(ru_RU.KOI8-R): Документация
Requires: %{rpm_name} = %{rpm_ver}-%{rel}

%description docs
doxygen documentation for rpm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure --with-python --with-apidocs --without-javaglue
%{__make} %{_smp_mflags}
%{__make} doxygen

cd beecrypt
%{__make} check
cd ..

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

# выносим файлы с макросами - они теперь в отдельном пакете
# это сделано для того что бы не надо было бы пересобирать
# rpm для того что бы добавить новый макрос
rm -f ${RPM_BUILD_ROOT}/usr/lib/rpm/i386-linux/macros
rm -f ${RPM_BUILD_ROOT}/usr/lib/rpm/i486-linux/macros
rm -f ${RPM_BUILD_ROOT}/usr/lib/rpm/i586-linux/macros
rm -f ${RPM_BUILD_ROOT}/usr/lib/rpm/i686-linux/macros
rm -f ${RPM_BUILD_ROOT}/usr/lib/rpm/noarch-linux/macros
rm -f ${RPM_BUILD_ROOT}/usr/lib/rpm/athlon-linux/macros
rm -f ${RPM_BUILD_ROOT}/usr/lib/rpm/macros

# Save list of packages through cron
mkdir -p ${RPM_BUILD_ROOT}/etc/cron.daily/
install -m 755 scripts/rpm.daily ${RPM_BUILD_ROOT}/etc/cron.daily/rpm

mkdir -p ${RPM_BUILD_ROOT}/etc/logrotate.d/
install -m 644 scripts/rpm.log ${RPM_BUILD_ROOT}/etc/logrotate.d/rpm

mkdir -p ${RPM_BUILD_ROOT}/etc/rpm

#mkdir -p ${RPM_BUILD_ROOT}/var/spool/repackage

#mkdir -p ${RPM_BUILD_ROOT}/var/lib/rpm
#for dbi in \
#	Basenames Conflictname Dirnames Group Installtid Name Providename \
#	Provideversion Removetid Requirename Requireversion Triggername \
#	Sigmd5 Sha1header Filemd5s Packages \
#	__db.001 __db.002 __db.003 __db.004 __db.005 __db.006 __db.007 \
#	__db.008 __db.009
#do
#    touch ${RPM_BUILD_ROOT}/var/lib/rpm/$dbi
#done

#%cd ${RPM_BUILD_ROOT}%{_libdir}
#%mv pythonyes python2.2

%post -n libpopt -p /sbin/ldconfig
%postun -n libpopt -p /sbin/ldconfig

%post -n libbeecrypt -p /sbin/ldconfig
%postun -n libbeecrypt -p /sbin/ldconfig

%post -n librpm -p /sbin/ldconfig
%postun -n librpm -p /sbin/ldconfig

%clean
%rm -rf %{buildroot}
%rm -rf %{_builddir}/%{rpm_name}-%{rpm_ver}

%files
%defattr(-,root,root)
%doc CHANGES CREDITS INSTALL README README.amiga doc/manual
%dir /etc/rpm
%config(noreplace,missingok) /etc/cron.daily/rpm
%config(noreplace,missingok) /etc/logrotate.d/rpm
/bin/rpm
%{_bindir}/gendiff
%{_bindir}/rpm2cpio
%{_bindir}/rpmdb
%{_bindir}/rpmquery
%{_bindir}/rpmsign
%{_bindir}/rpmverify
%{_bindir}/rpmi
%{_bindir}/rpme
%{_bindir}/rpmu
%{_libdir}/rpmrc
%{_libdir}/rpmpopt
/usr/lib/rpm/rpmpopt-4.1
/usr/lib/rpm/rpmrc
/usr/lib/rpm/rpmv
/usr/lib/rpm/rpmu
/usr/lib/rpm/rpmd
/usr/lib/rpm/rpme
/usr/lib/rpm/rpmi
/usr/lib/rpm/rpmk
/usr/lib/rpm/rpmq
/usr/lib/rpm/rpm2cpio.sh
%{_datadir}/locale/*/*/rpm.mo
%doc %{_man1dir}/gendiff.*
%doc %{_man8dir}/rpm.*
%doc %{_man8dir}/rpm2cpio.*
%doc %{_mandir}/ru/man8/rpm.*
%doc %{_mandir}/ru/man8/rpm2cpio.*
%doc %{_mandir}/fr/man8/rpm.*
%doc %{_mandir}/ja/man8/rpm.*
%doc %{_mandir}/ja/man8/rpm2cpio.*
%doc %{_mandir}/ko/man8/rpm.*
%doc %{_mandir}/ko/man8/rpm2cpio.*
%doc %{_mandir}/pl/man8/rpm.*
%doc %{_mandir}/pl/man8/rpm2cpio.*
%doc %{_mandir}/sk/man8/rpm.*

%files build
%defattr(-,root,root)
%{_prefix}/bin/rpmbuild
%{_prefix}/bin/rpmgraph
%dir %{_topdir}
%dir %{_topdir}/BUILD
%dir %{_topdir}/SPECS
%dir %{_topdir}/SOURCES
%dir %{_topdir}/SRPMS
%dir %{_topdir}/RPMS
%{_topdir}/RPMS/*
%{_libdir}/rpm/rpmb
%{_libdir}/rpm/rpmt
%{_libdir}/rpm/rpmcache
%{_libdir}/rpm/rpmdiff
%{_libdir}/rpm/rpmdiff.cgi
%{_libdir}/rpm/Specfile.pm
%{_libdir}/rpm/brp-compress
%{_libdir}/rpm/brp-redhat
%{_libdir}/rpm/brp-sparc64-linux
%{_libdir}/rpm/brp-strip
%{_libdir}/rpm/brp-strip-comment-note
%{_libdir}/rpm/brp-strip-shared
%{_libdir}/rpm/check-files
%{_libdir}/rpm/check-prereqs
%{_libdir}/rpm/config.guess
%{_libdir}/rpm/config.site
%{_libdir}/rpm/config.sub
%{_libdir}/rpm/convertrpmrc.sh
%{_libdir}/rpm/cpanflute
%{_libdir}/rpm/cpanflute2
%{_libdir}/rpm/cross-build
%{_libdir}/rpm/find-debuginfo.sh
%{_libdir}/rpm/find-lang.sh
%{_libdir}/rpm/find-prov.pl
%{_libdir}/rpm/find-provides
%{_libdir}/rpm/find-provides.perl
%{_libdir}/rpm/find-req.pl
%{_libdir}/rpm/find-requires
%{_libdir}/rpm/find-requires.perl
%{_libdir}/rpm/get_magic.pl
%{_libdir}/rpm/getpo.sh
%{_libdir}/rpm/http.req
%{_libdir}/rpm/javadeps
%{_libdir}/rpm/magic.prov
%{_libdir}/rpm/magic.req
%{_libdir}/rpm/mkinstalldirs
%{_libdir}/rpm/perl.prov
%{_libdir}/rpm/perl.req
%{_libdir}/rpm/rpm.daily
%{_libdir}/rpm/rpm.log
%{_libdir}/rpm/rpm.xinetd
%{_libdir}/rpm/sql.prov
%{_libdir}/rpm/sql.req
%{_libdir}/rpm/striptofile
%{_libdir}/rpm/tcl.req
%{_libdir}/rpm/tgpg
%{_libdir}/rpm/trpm
%{_libdir}/rpm/u_pkg.sh
%{_libdir}/rpm/unstripfile
%{_libdir}/rpm/vpkg-provides.sh
%{_libdir}/rpm/vpkg-provides2.sh
%doc %{_man8dir}/rpmbuild.*
%doc %{_man8dir}/rpmcache.*
%doc %{_man8dir}/rpmgraph.*

%files -n librpm
%defattr(-,root,root)
%{_libdir}/librpm*.so

%files -n librpm-dev
%defattr(-,root,root)
%doc TODO
%{_includedir}/rpm/*.h

%files -n librpm-static-dev
%defattr(-,root,root)
%{_libdir}/librpmio.la
%{_libdir}/librpmio.a
%{_libdir}/librpmdb.la
%{_libdir}/librpmdb.a
%{_libdir}/librpm.la
%{_libdir}/librpm.a
%{_libdir}/librpmbuild.la
%{_libdir}/librpmbuild.a

%files -n libelf-dev
%defattr(-,root,root)
%doc libelf/ChangeLog libelf/README
%{_libdir}/libelf.la
%{_libdir}/libelf.a
%{_includedir}/libelf/*.h

%files -n libpopt
%defattr(-,root,root)
%{_libdir}/libpopt.so
%{_libdir}/libpopt.so.*
%{_datadir}/locale/*/*/popt.mo

%files -n libpopt-dev
%defattr(-,root,root)
%{_includedir}/popt.h
%{_libdir}/libpopt.la
%{_libdir}/libpopt.a
%doc %{_mandir}/man3/popt.*

%files -n libbeecrypt
%defattr(-,root,root)
%doc beecrypt/AUTHORS beecrypt/BENCHMARKS beecrypt/CONTRIBUTORS beecrypt/NEWS
%doc beecrypt/README beecrypt/README.DLL beecrypt/README.WIN32
%{_libdir}/libbeecrypt.so
%{_libdir}/libbeecrypt.so.*

%files -n libbeecrypt-dev
%defattr(-,root,root)
%doc beecrypt/BUGS
%{_libdir}/libbeecrypt.la
%{_libdir}/libbeecrypt.a
%{_includedir}/beecrypt/*.h

%files python
%defattr(-,root,root)
%doc python/ChangeLog
%{_libdir}/python2.2/

%files docs
%defattr(-,root,root)
%doc apidocs

%changelog
* Tue Feb 15 2005 Igor Zubkov <icesik@mail.ru> 4.1-los6
- rpm: remove Requires: patch.
- rpm-build: add Requires: patch.

* Tue Jan 11 2005 Igor Zubkov <icesik@mail.ru> 4.1-los5
- remove all macros to rpm-macros package and add 
    rpm-macros to Requires.
- remove rpm-build to rpm-build package.
- clean up Group information.
- add russian Group information.
- added `diffutils' to Requires.
- added `patch' to Requires.
- added new macros.
- change BuildRequires: zlib-dev to libz-dev.

* Wed Dec 08 2004 Igor Zubkov <icesik@mail.ru> 4.1-los4
- added new macros.
- added `file' to Requires.
- added `patch' to BuildRequires.
- added `zlib-dev' to BuildRequires.

* Wed Dec 08 2004 Igor Zubkov <icesik@mail.ru> 4.1-los3
- fixed up broken dependes.

* Tue Dec 07 2004 Igor Zubkov <icesik@mail.ru> 4.1-los2
- enable doxygen documentation.
- enable python.

* Mon Nov 01 2004 Igor Zubkov <icesik@mail.ru> 4.1-los1
- Initial build for Los Angeles GNU/Linux.
