# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Three programs that help manage the /proc directory.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		psmisc
%define ver		21.5
%define rel		los1

%define _exec_prefix	/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libncurses >= 5.3-los1
BuildRequires:	libncurses-dev >= 5.3-los1

%description
The Psmisc package contains three programs which help manage the /proc
directory.

%prep
%setup -q

%build
./configure --host=%{_host} --build=%{_build} --target=%{_target_platform} \
	    --prefix=%{_prefix} --exec-prefix=/ --mandir=%{_mandir}
%{__make} %{_smp_mflags}
#make check

%install
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/
%{__make} prefix=${RPM_BUILD_ROOT}%{_prefix}/ exec_prefix=${RPM_BUILD_ROOT}/ mandir=${RPM_BUILD_ROOT}%{_mandir} install

%find_lang %{name}

cd ${RPM_BUILD_ROOT}%{_bindir}/
ln -s killall pidof

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%doc %{_man1dir}/*

%changelog
* Sat Feb 05 2005 Igor Zubkov <icesik@mail.ru> 21.5-los1
- update to 21.5.
- add simlink `ln -s killall pidof`.

* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 21.4-los1
- Initial build for Los Angeles GNU/Linux.
