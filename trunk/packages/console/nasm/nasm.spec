# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		NASM, the Netwide Assembler.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		nasm
%define ver		0.98.39
%define rel		los1
%define url		http://www.sourceforge.net/projects/nasm/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	LGPL
Group:		Development/Other
Group(ru_RU.KOI8-R):	Разработка/Разное
Source0:	%{name}-%{version}.tar.bz2
URL:		%{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
NASM, the Netwide Assembler.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_man1dir}/

#make INSTALLROOT="${RPM_BUILD_ROOT}" install_everything
%{__make} INSTALLROOT="${RPM_BUILD_ROOT}" install

#make prefix=${RPM_BUILD_ROOT}%{_prefix} mandir=${RPM_BUILD_ROOT}%{_mandir} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES COPYING ChangeLog INSTALL README TODO
%{_bindir}/*
%doc %{_man1dir}/*

%changelog
* Mon Feb 07 2005 Igor Zubkov <icesik@mail.ru> 0.98.39-los1
- update to new release 0.98.39.

* Wed Jan 05 2005 Igor Zubkov <icesik@mail.ru> 0.98.38-los1
- update to new release 0.98.38.

* Tue Nov 16 2004 Igor Zubkov <icesik@mail.ru> 0.98.36-los1
- Initial build for Los Angeles GNU/Linux.
