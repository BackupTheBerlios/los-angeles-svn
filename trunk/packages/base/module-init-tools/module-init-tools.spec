# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean up build for non i686 target

%define sum		Utilities for inserting and removing modules from the Linux kernel.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		module-init-tools
%define ver		3.1
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.tar.bz2.sign.pgp
Source2:	%{name}-testsuite-%{version}.tar.bz2
Source3:	%{name}-testsuite-%{version}.tar.bz2.sign.pgp
Source4:	module-test-framework.tar.bz2
Source5:	module-test-framework.tar.bz2.sign.pgp
Source6:	FAQ
Source7:	TODO
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libz
BuildRequires:	libz-dev

%description
Utilities for inserting and removing modules from the Linux kernel.

%prep
%setup -q

%build
./configure --prefix="" --enable-zlib
%{__make} %{_smp_mflags} -i
%{__make} -i check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install -i

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
/sbin/insmod.static
/sbin/depmod
/sbin/modinfo
/sbin/generate-modprobe.conf
/sbin/modprobe
/sbin/rmmod
/sbin/insmod
/bin/lsmod
%doc %{_man5dir}/modules.dep.5*
%doc %{_man5dir}/modprobe.conf.5*
%doc %{_man8dir}/depmod.8*
%doc %{_man8dir}/insmod.8*
%doc %{_man8dir}/lsmod.8*
%doc %{_man8dir}/rmmod.8*
%doc %{_man8dir}/modinfo.8*
%doc %{_man8dir}/modprobe.8*

%changelog
* Mon Jan 10 2005 Igor Zubkov <icesik@mail.ru> 3.1-los2
- change depends:
- zlib -> libz
- zlib-dev -> libz-dev

* Sun Nov 21 2004 Igor Zubkov <icesik@mail.ru> 3.1-los1
- Initial build for Los Angeles GNU/Linux.
