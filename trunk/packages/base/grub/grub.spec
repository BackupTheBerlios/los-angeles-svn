# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The Grub package contains a bootloader.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		grub
%define ver		0.94
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}.tar.gz.sig
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libncurses
BuildRequires:	libncurses-dev

%description
The Grub package contains a bootloader.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --infodir=%{_infodir} --mandir=%{_mandir}
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog INSTALL MAINTENANCE NEWS README THANKS TODO
%{_bindir}/mbchk
%{_sbindir}/*
%{_datadir}/grub/*/*
%doc %{_infodir}/grub.*
%doc %{_infodir}/multiboot.*
%doc %{_mandir}/man[18]/*

%changelog
* Wed Jun 16 2004 Igor Zubkov <icesik@mail.ru> 0.94-los1
- Initial build for Los Angeles GNU/Linux.
