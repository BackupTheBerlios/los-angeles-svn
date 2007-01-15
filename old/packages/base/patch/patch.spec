# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU Patch Program.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		patch
%define ver		2.5.4
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Tools
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The  patch  program modifies a file according to a patch file. A patch
file  usually  is  a  list, created by the diff program, that contains
instructions on how an original file needs to be modified.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_man1dir}/

install -c patch ${RPM_BUILD_ROOT}%{_bindir}/`echo patch | sed 's,^,,; '`
install -c -m 644 ./patch.man ${RPM_BUILD_ROOT}%{_man1dir}/`echo patch | sed 's,^,,; '`.1

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%doc %{_man1dir}/*

%changelog
* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 2.5.4-los1
- Initial build for Los Angeles GNU/Linux.
