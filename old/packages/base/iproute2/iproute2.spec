# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		iproute2
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		iproute2
%define ver		2.6.9
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{ver}-041019.tar.gz
Patch0:		%{name}-%{ver}_041019-find_update-1.patch
Patch1:		%{name}-%{ver}_041019-remove_db-1.patch
Patch2:		%{name}-%{ver}-los-rpm-flags.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
iproute2

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./configure
%{__make} %{_smp_mflags} SBINDIR=/sbin

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} SBINDIR=/sbin install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/iproute2/*
/sbin/*
%{_libdir}/tc/
%doc %{_datadir}/doc/iproute2/
%doc %{_man8dir}/*

%changelog
* Sat Feb 05 2005 Igor Zubkov <icesik@mail.ru> 2.6.9-los1
- Initial build for Los Angeles GNU/Linux.
