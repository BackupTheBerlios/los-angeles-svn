# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean up build for non i486
# TODO: update

%define sum		Util-Linux
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		util-linux
%define ver		2.12q
%define rel		los2

%define __find_requires	%{_builddir}/%{name}-%{version}/my-find-requires

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.bz2
#Source1:	%{name}-%{version}.tar.bz2.sign
Patch0:		%{name}-%{version}-cramfs-1.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libncurses-dev
Requires:	libncurses

BuildRequires:	libz-dev
Requires:	libz

%description
The  Util-linux  package  contains  a  number of miscellaneous utility
programs.  Some  of  the  more  prominent utilities are used to mount,
unmount,  format, partition and manage disk drives, open tty ports and
fetch kernel messages.

%prep
%setup -q
%patch0 -p1

%build
mkdir -p %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
cat > my-find-requires << EOF
/usr/lib/rpm/find-requires | grep -v tcsh
EOF
chmod +x my-find-requires

cp hwclock/hwclock.c{,.backup}
sed 's%etc/adjtime%var/lib/hwclock/adjtime%' hwclock/hwclock.c.backup > hwclock/hwclock.c
CC=%{__cc} ./configure 
%{__make} HAVE_KILL=yes HAVE_SLN=yes %{_smp_mflags} CC=%{__cc}

%install
mkdir -p ${RPM_BUILD_ROOT}/var/lib/hwclock

%{__make} DESTDIR=${RPM_BUILD_ROOT} HAVE_KILL=yes HAVE_SLN=yes install

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc HISTORY INSTALL MAINTAINER README
%config(noreplace) /etc/fdprm
/bin/*
/sbin/*
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/misc/getopt/*
%doc %{_infodir}/*
%doc %{_man1dir}/*
%doc %{_man5dir}/*
%doc %{_man8dir}/*

%changelog
* Sun Mar 27 2005 Igor Zubkov <icesik@mail.ru> 2.12q-los2
- remove tcsh from depends.

* Sun Mar 27 2005 Igor Zubkov <icesik@mail.ru> 2.12q-los1
- update 2.12q.

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 2.12b-los2
- mark /etc/fdprm noreplace.
- remove Vendor field.

* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 2.12b-los1
- update to 2.12b

* Thu Jun 17 2004 Igor Zubkov <icesik@mail.ru> 2.12a-los1
- update to 2.12a

* Sat May 08 2004 Igor Zubkov <icesik@mail.ru> 2.12-los1
- Initial build for Los Angeles GNU/Linux.
