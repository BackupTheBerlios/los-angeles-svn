# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU Compression Utilities.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		gzip
%define ver		1.3.5
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.gzip.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The GNU Compression Utilities.

%prep
%setup -q

%build
%configure
cp gzexe.in{,.backup}
sed 's%"BINDIR"%/bin%' gzexe.in.backup > gzexe.in
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
mkdir -p ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}%{_bindir}/gzip ${RPM_BUILD_ROOT}/bin
rm ${RPM_BUILD_ROOT}%{_bindir}/{gunzip,zcat}
ln -s gzip ${RPM_BUILD_ROOT}/bin/gunzip
ln -s gzip ${RPM_BUILD_ROOT}/bin/zcat
ln -s gunzip ${RPM_BUILD_ROOT}/bin/uncompress

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README README-alpha THANKS TODO
/bin/*
%{_bindir}/*
%doc %{_infodir}/*
%doc %{_man1dir}/*

%changelog
* Mon Nov 08 2004 Igor Zubkov <icesik@mail.ru> 1.3.5-los1
- Initial build for Los Angeles GNU/Linux.
