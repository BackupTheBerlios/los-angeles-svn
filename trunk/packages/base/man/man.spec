# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean up build for non i686

%define sum		Man is a man pager.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		man
%define ver		1.5m2
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
Patch0:		%{name}-%{version}-80cols.patch
Patch1:		%{name}-%{version}-manpath.patch
Patch2:		%{name}-%{version}-pager.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Man is a man pager.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./configure -default -confdir=%{_sysconfdir}
%{__make} %{_smp_mflags}

%install
%{__make} PREFIX=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%config /etc/*
%doc COPYING HISTORY INSTALL LSM README README.GNU-WIN32 README.HP README.IRIX TODO
%{_bindir}/*
%{_sbindir}/*
%doc %{_mandir}/*/*

%changelog
* Tue Nov 30 2004 Igor Zubkov <icesik@mail.ru> 1.5m2-los1
- Initial build for Los Angeles GNU/Linux.
