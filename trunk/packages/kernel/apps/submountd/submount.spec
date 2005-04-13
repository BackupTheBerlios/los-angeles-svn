# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Automatically mounts and unmounts removable media devices.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		submount
%define ver		0.9
%define rel		los1

Summary:	%{sum}
Name:		%{name}d
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Kernel
Source0:	submount-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The submount system automatically mounts and unmounts removable
media devices when their mountpoints are accessed.

Install submount if you do not wish to mount and unmount removable media
devices manually.

%prep
%setup -q -n submount-%{ver}

%build
cd submountd-%{version}/
./configure --host=%{_host} --build=%{_build} \
	    --target=%{_target_platform} \
	    --mandir=%{_mandir}
%{__make} %{_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}"

%install
./rename-docs %{version}
cd submountd-%{version}/
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/submount-%{ver}

%files
%defattr(-,root,root)
%doc COPYING README INSTALL.submountd README.submountd
/sbin/submountd
/sbin/net-submountd
%doc %{_man8dir}/*

%changelog
* Wed Apr 06 2005 Igor Zubkov <icesik@mail.ru> 0.9-los1
- Initial build for Los Angeles GNU/Linux.
