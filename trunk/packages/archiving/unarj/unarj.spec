# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean up build for non i686 target

%define sum		An uncompressor for .arj format archive files.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		unarj
%define ver		2.43
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	distributable
Group:		Archiving
Group(ru_RU.KOI8-R):	Архиваторы
Source0:	ftp://metalab.unc.edu/pub/Linux/utils/compress/%{name}-%{ver}.tar.gz
Patch0:		%{name}-%{ver}-subdir.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The UNARJ program is used to uncompress .arj format archives.  The
.arj format archive was mostly used on DOS machines.

Install the unarj package if you need to uncompress .arj format
archives.

%prep
%setup -q
%patch0 -p1

%build
%{__make} clean
%{__make}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/

install -m 755 unarj ${RPM_BUILD_ROOT}%{_bindir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc unarj.doc
%{_bindir}/unarj

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 2.43-los2
- remove Vendor field.
- add russian group description.

* Sun Jun 06 2004 Igor Zubkov <icesik@mail.ru> 2.43-los1
- Initial build for Los Angeles GNU/Linux.
