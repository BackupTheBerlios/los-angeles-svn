# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		GNU cpio -- a program to manage archives of files.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		cpio
%define ver		2.5
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL/LGPL
Group:		Utils
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GNU cpio is a tool for creating and extracting archives, or copying
files from one place to another.  It handles a number of cpio formats
as well as reading and writing tar files.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%makeinstall mandir=${RPM_BUILD_ROOT}%{_man1dir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README
%{_bindir}/*
%{_libexecdir}/*
%doc %{_mandir}/*/*
%doc %{_infodir}/*

%changelog
* Tue Dec 07 2004 Igor Zubkov <icesik@mail.ru> 2.5-los2
- fix build.

* Tue Nov 16 2004 Igor Zubkov <icesik@mail.ru> 2.5-los1
- Initial build for Los Angeles GNU/Linux.
