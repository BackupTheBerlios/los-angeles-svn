# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Utilities used to manage the build process of sources.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		make
%define ver		3.80
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-crash-1.patch
Patch1:		%{name}-%{version}-eval-1.patch
Patch2:		%{name}-%{version}-variables-1.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Make  determines,  automatically, which pieces of a large program need
to be recompiled and issues the commands to recompile them.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%{__make} CFLAGS="-Iglob/" %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/make
%{_datadir}/locale/*/*/make.mo
%doc %{_mandir}/man1/*
%doc %{_infodir}/*

%changelog
* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 3.80-los1
- Initial build for Los Angeles GNU/Linux.
