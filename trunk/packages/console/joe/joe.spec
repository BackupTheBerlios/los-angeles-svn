# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		An easy to use, modeless text editor.
%define vendor		Los Angeles GNU/Linux
%define mainatiner	Igor Zubkov <icesik@mail.ru>
%define name		joe
%define ver		3.1
%define rel		los1
%define url		http://sourceforge.net/projects/joe-editor/

Summary:	%{sum}
Vendor:		%{vendor}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Editors
Source0:	%{name}-%{version}.tar.gz
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Joe is a powerful, easy to use, modeless text editor.
It uses the same WordStar keybindings used in Borland's development
environment.

%prep
%setup -q

%build
%configure
make

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog HINTS INFO LIST NEWS README README.cvs TODO
%dir %{_sysconfdir}/joe
%config(noreplace) %{_sysconfdir}/joe/*
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
* Tue Jun 01 2004 Igor Zubkov <icesik@mail.ru> 3.1-los1
- Initial build for Los Angeles GNU/Linux.
