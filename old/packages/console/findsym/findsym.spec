# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		search through all your shared libraries for a specific symbol.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define	name		findsym
%define	ver		1.1
%define	rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

%description
This program will attempt to search through all your shared libraries
for a specific symbol.  This is useful when trying to compile something
and the compiler complains about an undefined reference similar to this:

/tmp/cceuy0nE.o(.text+0x7): undefined reference to `foo'

Running "findsym foo" would try to locate the symbol foo and indicate
what library you should be linking with.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
cp findsym ${RPM_BUILD_ROOT}%{_bindir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}

%files
%defattr(-,root,root)
%doc CHANGES COPYING
%{_bindir}/findsym

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 1.1-los1
- Initial build for Los Angeles GNU/Linux.
