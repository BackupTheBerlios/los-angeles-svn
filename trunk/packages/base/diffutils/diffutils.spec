# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		GNU diff.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		diffutils
%define ver		2.8.1
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Tools
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package contains the GNU diff, diff3, sdiff, and cmp utilities.
Their features are a superset of the Unix features and they are
significantly faster.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%makeinstall

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALLME NEWS README THANKS
%{_bindir}/*
%doc %{_mandir}/man1/*
%doc %{_infodir}/*
%{_datadir}/locale/*/*/*

%changelog
* Fri May 14 2004 Igor Zubkov <icesik@mail.ru> 2.8.1-los1
- Initial build for Los Angeles GNU/Linux.
