# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A tool for testing TCP connections.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		ttcp
%define ver		1.12
%define rel             los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	Public Domain
Group:		Unknown
Source0:	ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.c
Source1:	ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.1
Source2:	ftp://ftp.sgi.com/sgi/src/ttcp/README
Buildroot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
ttcp is a tool for testing the throughput of TCP connections.  Unlike other
tools which might be used for this purpose (such as FTP clients), ttcp does
not read or write data from or to a disk while operating, which helps ensure
more accurate results.

%prep
%setup -c -T
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} .
chmod 644 *

%build
%{__cc} -o ttcp ${RPM_OPT_FLAGS} ttcp.c

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -m755 ttcp ${RPM_BUILD_ROOT}%{_bindir}
install -m644 ttcp.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%doc %{_man1dir}/*

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 1.12-los2
- remove Vendor field.
- some clean up's.

* Fri Nov 19 2004 Igor Zubkov <icesik@mail.ru> 1.12-los1
- Initial build for Los Angeles GNU/Linux.
