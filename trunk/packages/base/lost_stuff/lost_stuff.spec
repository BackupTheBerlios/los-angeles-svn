# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Lost stuff
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		lost_stuff
%define ver		0
%define rel		los6

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	free
Group:		System
Source2:	issue
Source3:	motd
Source4:	hosts
Source5:	hostname
Source6:	los_angeles-release
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

AutoReq:	off

BuildArch:	noarch

%description
Lost stuff

%prep

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/
cd ${RPM_BUILD_ROOT}%{_sysconfdir}/
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .
cp %{SOURCE6} .
ln -s los_angeles-release lost-release

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/issue
%config(noreplace) %{_sysconfdir}/motd
%config(noreplace) %{_sysconfdir}/hosts
%config(noreplace) %{_sysconfdir}/hostname
%config(noreplace) %{_sysconfdir}/los_angeles-release
%config(noreplace) %{_sysconfdir}/lost-release

%changelog
* Tue Dec 14 2004 Igor Zubkov <icesik@mail.ru> 0-los1
- Initial build for Los Angeles GNU/Linux.
