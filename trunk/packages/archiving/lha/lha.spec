# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: clean up build for non i686 target!

%define sum		An archiving and compression utility for LHarc format archives.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		lha
%define ver		1.14i
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	freeware
Group:		Archiving
Source0:	http://www2m.biglobe.ne.jp/~dolphin/lha/prog/lha-114i.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
LHA is an archiving and compression utility for LHarc format archives.
LHA is mostly used in the DOS world, but can be used under Linux to
extract DOS files from LHA archives.

Install the lha package if you need to extract DOS files from LHA archives.

%prep
%setup -q -n lha-114i

%build
make

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/

install -m755 -s src/lha ${RPM_BUILD_ROOT}%{_bindir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/lha-114i

%files
%defattr(-,root,root)
%doc PROBLEMS.euc README.euc MACHINES*
%{_bindir}/lha

%changelog
* Sun Jun 06 2004 Igor Zubkov <icesik@mail.ru> 1.14i-los1
- Initial build for Los Angeles GNU/Linux.
