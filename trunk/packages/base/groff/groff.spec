# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The Gnu roff package
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		groff
%define ver		1.19.1
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{version}.tar.gz
Patch0:		groff-1.19.1-sed.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The Gnu roff package

%prep
%setup -q
%patch0 -p1

%build
PAGE=A4 %configure
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
%makeinstall
ln -s soelim ${RPM_BUILD_ROOT}%{_bindir}/zsoelim
ln -s eqn ${RPM_BUILD_ROOT}%{_bindir}/geqn
ln -s tbl ${RPM_BUILD_ROOT}%{_bindir}/gtbl

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc BUG-REPORT COPYING ChangeLog FDL INSTALL LICENSE MANIFEST MORE.STUFF
%doc NEWS PROBLEMS PROJECTS README README.CVS README.MinGW TODO
%{_bindir}/*
%doc %{_infodir}/*
%doc %{_mandir}/man[157]/*
%{_datadir}/groff/%{ver}/eign
%{_datadir}/groff/%{ver}/font/
%{_datadir}/groff/%{ver}/tmac/
%{_datadir}/groff/site-tmac/*
%doc %{_datadir}/doc/groff/

%changelog
* Tue Feb 15 2005 Igor Zubkov <icesik@mail.ru> 1.19.1-los1
- update to 1.19.1.

* Thu May 13 2004 Igor Zubkov <icesik@mail.ru> 1.18.1-los1
- Initial build for Los Angeles GNU/Linux.
