# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

Summary:   Support library for syslog-ng
Name:      libol
Version:   0.3.15
Release:   1
Epoch:     0
License:   GPL
Group:     System Environment/Libraries
Url:       http://www.balabit.com/products/syslog-ng/
Source0:    http://www.balabit.com/downloads/syslog-ng/libol/0.3/%{name}-%{version}.tar.gz
Source1:    http://www.balabit.com/downloads/syslog-ng/libol/0.3/%{name}-%{version}.tar.gz.asc
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Support library for syslog-ng.

%package dev
Summary:   Support library for syslog-ng: headers and libraries
Group:     Development/Libraries
Requires:  %{name} = %{epoch}:%{version}-%{release}

%description dev
Support library for syslog-ng: headers and libraries.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%makeinstall

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING
%{_libdir}/libol.so.0
%{_libdir}/libol.so.0.0.0

%files dev
%defattr(-,root,root,-)
%exclude %{_bindir}/make_class
%{_bindir}/libol-config
%{_libdir}/libol.a
%{_libdir}/libol.la
%{_libdir}/libol.so
%{_includedir}/libol/

%changelog
* Sun Feb 06 2005 Igor Zubkov <icesik@mail.ru> 0:0.3.13-los1
- Initial build for Los Angeles GNU/Linux.
