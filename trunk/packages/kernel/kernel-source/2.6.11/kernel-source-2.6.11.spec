# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Vanilla kernel source from www.kernel.org.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		kernel-source-2.6.11
%define ver		2.6.11
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Kernel/Source
Source0:	linux-%{ver}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

AutoReq:	off

BuildArch:	noarch

%description
Vanilla kernel source from www.kernel.org.

%prep

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/src/kernel-source/
cd ${RPM_BUILD_ROOT}%{_prefix}/src/kernel-source/
cp %{SOURCE0} .

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/src/kernel-source/*

%changelog
* Tue Apr 05 2005 Igor Zubkov <icesik@mail.ru> 2.6.11-los1
- Initial build for Los Angeles GNU/Linux.
