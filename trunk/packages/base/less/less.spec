# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Text Pager.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		less
%define ver		382
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libncurses
BuildRequires:	libncurses-dev

%description
Less is a file pager, or text viewer. It displays the contents of a file,
or stream, and has the ability to scroll. Less has a few features not
included in the more pager, such as the ability to scroll backwards.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} prefix=${RPM_BUILD_ROOT}%{_prefix} \
	sysconfdir=${RPM_BUILD_ROOT}%{_sysconfdir}/ \
	bindir=${RPM_BUILD_ROOT}/bin/ \
	mandir=${RPM_BUILD_ROOT}%{_mandir}/ install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc COPYING INSTALL LICENSE NEWS README
/bin/*
%doc %{_man1dir}/*

%changelog
* Tue Feb 15 2005 Igor Zubkov <icesik@mail.ru> 382-los1
- update to 382.

* Fri Jun 04 2004 Igor Zubkov <icesik@mail.ru> 381-los1
- update to 381.

* Tue Mar 02 2004 Igor Zubkov <icesik@mail.ru> 378-los1
- Initial build for Los Angeles GNU/Linux.
