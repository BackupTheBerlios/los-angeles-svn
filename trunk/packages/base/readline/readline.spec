# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Readline library.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		readline
%define altname		readline
%define ver		5.0
%define rel		los2

Summary:	%{sum}
Name:		lib%{name}5
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Libraries
Group(ru_RU.KOI8-R):	Система/Библиотеки
Source0:	ftp://ftp.gnu.org/gnu/readline-%{version}.tar.bz2
Patch0:		readline-5.0-display_wrap-1.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Obsoletes:	libreadline

%description
The Readline library provides a set of functions for use by applications
that allow users to edit command lines as they are typed in.  Both
Emacs and vi editing modes are available.  The Readline library includes
additional functions to maintain a list of previously-entered command
lines, to recall and perhaps reedit those lines, and perform csh-like
history expansion on previous commands.

The history facilites are also placed into a separate library, the
History library, as part of the build process.  The History library
may be used without Readline in applications which desire its
capabilities.

%package dev
Summary: Development files for libreadline.
Group: Development/C
Group(ru_RU.KOI8-R): Разработка/C
Requires: %{name} = %{version}-%{release}

Obsoletes:	libreadline-dev

%description dev
Development files for libreadline.

%prep
%setup -q -n %{altname}-%{ver}
%patch0 -p1

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

cd ${RPM_BUILD_ROOT}%{_libdir}
chmod +x *.so.*

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{altname}-%{version}

%files
%defattr(-,root,root)
%doc CHANGELOG CHANGES COPYING NEWS README USAGE
%{_libdir}/*.so.*
%doc %{_infodir}/*

%files dev
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/readline/*.h
%doc %{_man3dir}/*

%changelog
* Thu Mar 31 2005 Igor Zubkov <icesik@mail.ru> 5.0-los2
- add obsoletes libreadline and libreadline-dev.

* Thu Mar 31 2005 Igor Zubkov <icesik@mail.ru> 5.0-los1
- update to 5.0.

* Wed Jun 16 2004 Igor Zubkov <icesik@mail.ru> 4.3-los1
- Initial build for Los Angeles GNU/Linux.
