# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A small utility for safely making /tmp files.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		mktemp
%define ver		1.5
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	BSD
Group:		System/Base
Group(ru_RU.KOI8-R): Система/База
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-add_tempfile-1.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The mktemp utility takes a given file name template and overwrites a
portion of it to create a unique file name.  This allows shell scripts
and other programs to safely create and use /tmp files.

Install the mktemp package if you need to use shell scripts or other
programs which will create and use unique /tmp files.

%prep
%setup -q
%patch0 -p1

%build
%configure --with-libc
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_man1dir}/
install -c -m 0555 -s mktemp ${RPM_BUILD_ROOT}%{_bindir}/mktemp
install -c -m 0444 ./mktemp.man ${RPM_BUILD_ROOT}%{_man1dir}/mktemp.1
install -c -m 0555 tempfile ${RPM_BUILD_ROOT}%{_bindir}/tempfile

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc INSTALL LICENSE README RELEASE_NOTES
%{_bindir}/mktemp
%{_bindir}/tempfile
%doc %{_man1dir}/*

%changelog
* Fri Nov 19 2004 Igor Zubkov <icesik@mail.ru> 1.5-los1
- Initial build for Los Angeles GNU/Linux.
