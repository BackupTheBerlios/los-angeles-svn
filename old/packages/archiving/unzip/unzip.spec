# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A utility for unpacking zip files.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		unzip
%define ver		5.51
%define rel		los1
%define url		http://www.info-zip.org/pub/infozip/UnZip.html

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	BSD
Group:		Archiving
Group(ru_RU.KOI8-R):	Архиваторы
Source0:	ftp://ftp.info-zip.org/pub/infozip/src/unzip551.tar.gz
Patch0:		unzip542-rpmoptflags.patch
Patch1:		unzip-5.51-dont-make-noise.patch
Patch2:		unzip-5.51-fix-Makefile.patch
Patch3:		unzip-5.51-fix-libz.patch
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The unzip utility is used to list, test, or extract files from a zip
archive.  Zip archives are commonly found on MS-DOS systems.  The zip
utility, included in the zip package, creates zip archives.  Zip and
unzip are both compatible with archives created by PKWARE(R)'s PKZIP
for MS-DOS, but the programs' options and default behaviors do differ
in some respects.

Install the unzip package if you need to list, test or extract files from
a zip archive.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

ln -s unix/Makefile Makefile

%build
%{__make} linux_noasm LF2="" %{_smp_mflags}

%install
%{__make} prefix=${RPM_BUILD_ROOT}%{_prefix}/ MANDIR=${RPM_BUILD_ROOT}%{_mandir}/man1 install LF2=""

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README BUGS LICENSE INSTALL COPYING.OLD Contents History.550 ToDo
%doc WHERE
%{_bindir}/*
%doc %{_mandir}/*/*

%changelog
* Tue Mar 15 2005 Igor Zubkov <icesik@mail.ru> 5.51-los1
- update to 5.51.

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 5.50-los2
- remove Vendor field.
- change Group to Archiving.
- add russian Group description.

* Sun Jun 06 2004 Igor Zubkov <icesik@mail.ru> 5.50-los1
- Initial build for Los Angeles GNU/Linux.
