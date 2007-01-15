# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		udev - a userspace implementation of devfs.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		udev
%define ver		051
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.tar.bz2.sign
Source2:	udev-config-1.rules
Source3:	udev-config-2.permissions
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
udev is targetted at Linux kernels 2.6 and beyond to provide a
userspace solution for a dynamic /dev directory, with persistent
device naming.

%prep
%setup -q
%{__make} udevdir=/dev %{_smp_mflags} OPTIMIZATION="$RPM_OPT_FLAGS" QUIET=""

%install
%{__make} udevdir=/dev DESTDIR=${RPM_BUILD_ROOT} install

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/rules.d/
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/permissions.d/

cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/rules.d/25-lfs.rules
cp %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/permissions.d/25-lfs.permissions

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog FAQ HOWTO-udev_for_dev README README-gcov_for_udev TODO docs
%config(noreplace) %{_sysconfdir}/dev.d/net/hotplug.dev
%config(noreplace) %{_sysconfdir}/hotplug.d/default/10-udev.hotplug
%config(noreplace) %{_sysconfdir}/udev/rules.d/25-lfs.rules
%config(noreplace) %{_sysconfdir}/udev/rules.d/50-udev.rules
%config(noreplace) %{_sysconfdir}/udev/permissions.d/25-lfs.permissions
%config(noreplace) %{_sysconfdir}/udev/udev.conf
%dir /dev
/sbin/*
%{_bindir}/*
%doc %{_man8dir}/*

%changelog
* Wed Feb 09 2005 Igor Zubkov <icesik@mail.ru> 051-los1
- update to 051.
- add some missing config files.
- mark all config as %%config(noreplace).
- clean up --target build.

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 042-los2
- remove Vendor field.
- add russian group description.

* Fri Nov 05 2004 Igor Zubkov <icesik@mail.ru> 042-los1
- Initial build for Los Angeles GNU/Linux.
