# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The Man-pages package contains over 1200 manual pages.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		man-pages
%define ver		1.67
%define rel		los1.1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Documentation
Group(ru_RU.KOI8-R):	Документация
Source0:	%{name}-%{version}.tar.bz2
#Source1:	%{name}-%{version}.lsm
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	noarch

Requires:	man

%description
The Man-pages package contains over 1200 manual pages. This documentation
details the C and C++ functions, describes a few important device files
and provides documents which would otherwise be missing from other packages.

%package -n man-pages-POSIX
Summary: Man (manual) pages from the Institute of Electrical and Electronics Engineers and The Open Group
Summary(ru_RU.KOI8-R): Руководства пользователя от The Institute of Electrical and Electronics Engineers and The Open Group
License: for reprint only
Group: Documentation
Group(ru_RU.KOI8-R): Документация

%description -n man-pages-POSIX
A large collection of man pages (reference material) from the 
IEEE Std 1003.1, 2003 Edition, Standard for Information Technology -- Portable
Operating System Interface (POSIX), The Open Group Base Specifications Issue 6,
Copyright (C) 2001-2003 by the Institute of Electrical and Electronics
Engineers, Inc and The Open Group.003.1, 2003 Edition, Standard for
Information Technology -- Portable Operating System Interface (POSIX),
The Open Group Base Specifications Issue 6, Copyright (C) 2001-2003 by the
Institute of Electrical and Electronics Engineers, Inc and The Open Group.
The man pages are organized into the following sections:
	0p: POSIX headers
	1p: POSIX utilities
	3p: POSIX functions

%prep
%setup -q

%install
%{__make} prefix=${RPM_BUILD_ROOT} install

# remove dups!
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/diff.*
rm -f ${RPM_BUILD_ROOT}%{_man3dir}/getspnam.*
rm -f ${RPM_BUILD_ROOT}%{_man5dir}/passwd.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/chgrp.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/chmod.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/chown.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/cp.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/dd.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/df.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/dir.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/dircolors.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/du.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/install.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/ln.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/ls.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/mkdir.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/mkfifo.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/mknod.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/mv.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/rm.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/rmdir.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/touch.*
rm -f ${RPM_BUILD_ROOT}%{_man1dir}/vdir.*

cd ${RPM_BUILD_ROOT}
sync

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README man-pages-1.67.Announce man-pages-1.67.lsm
%doc %{_mandir}/man?/*

%files -n man-pages-POSIX
%defattr(-,root,root)
%doc POSIX-COPYRIGHT
%doc %{_mandir}/man0p/*
%doc %{_mandir}/man1p/*
%doc %{_mandir}/man3p/*

%changelog
* Sat Mar 12 2005 Igor Zubkov <icesik@mail.ru> 1.67-los1.1
- update to 1.67.
- remove dups.

* Fri Jun 04 2004 Igor Zubkov <icesik@mail.ru> 1.62-los1
- Initial build for Los Angeles GNU/Linux.
