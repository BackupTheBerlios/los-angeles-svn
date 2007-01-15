# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		hotplug script
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		hotplug
%define ver		2004_09_23
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{ver}.tar.bz2
Source1:	%{name}-%{ver}.tar.bz2.sign
Buildroot:      %{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	noarch

%description
hotplug script.

%prep
%setup -q

%build

%install
%{__make} prefix=${RPM_BUILD_ROOT} install

rm -rf ${RPM_BUILD_ROOT}/etc/init.d/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%config(noreplace) /etc/hotplug/dasd.agent
%config(noreplace) /etc/hotplug/firmware.agent
%config(noreplace) /etc/hotplug/ieee1394.agent
%config(noreplace) /etc/hotplug/input.agent
%config(noreplace) /etc/hotplug/net.agent
%config(noreplace) /etc/hotplug/pci.agent
%config(noreplace) /etc/hotplug/scsi.agent
%config(noreplace) /etc/hotplug/tape.agent
%config(noreplace) /etc/hotplug/usb.agent
%config(noreplace) /etc/hotplug/input.rc
%config(noreplace) /etc/hotplug/pci.rc
%config(noreplace) /etc/hotplug/pnp.rc
%config(noreplace) /etc/hotplug/usb.rc
%config(noreplace) /etc/hotplug/hotplug.functions
%config(noreplace) /etc/hotplug/blacklist
%config(noreplace) /etc/hotplug/usb.usermap
%config(noreplace) /etc/hotplug/usb.handmap
%config(noreplace) /etc/hotplug/usb.distmap
%config(noreplace) /etc/hotplug.d/default/default.hotplug
/sbin/hotplug
%{_man8dir}/hotplug.*
/etc/hotplug/usb
/etc/hotplug/pci
/var/log/hotplug
/var/run/usb

%changelog
* Sat Feb 05 2005 Igor Zubkov <icesik@mail.ru> 2004_09_23-los1
- Initial build for Los Angeles GNU/Linux.
