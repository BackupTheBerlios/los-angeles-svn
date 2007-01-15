# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		libtool
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		libtool
%define ver		1.5.10
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Tools
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}.tar.gz.sig
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GNU libtool is a generic library support script. Libtool hides the
complexity of using shared libraries behind a consistent, portable interface.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog ChangeLog.0 ChangeLog.1 NEWS README THANKS TODO
%{_bindir}/*
%{_libdir}/*
%doc %{_infodir}/*
%{_includedir}/*
%{_datadir}/libtool/
%{_datadir}/aclocal/*

%changelog
* Wed Nov 03 2004 Igor Zubkov <icesik@mail.ru> 1.5.10-los1
- update to 1.5.10

* Thu May 13 2004 Igor Zubkov <icesik@mail.ru> 1.5-los1
- Initial build for Los Angeles GNU/Linux.
