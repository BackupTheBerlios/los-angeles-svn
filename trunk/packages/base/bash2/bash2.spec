# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The Bourne Again Shell.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		bash
%define altname		bash
%define ver		2.05b
%define rel		los3

Summary:	%{sum}
Name:		%{name}2
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Shells
Source0:	%{altname}-%{version}.tar.bz2
Patch0:		%{altname}-%{version}-gnu_fixes-2.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libncurses-dev
Requires:	libncurses

BuildRequires:	libreadline-dev
Requires:	libreadline

%description
bash  is  the  Bourne-Again  SHell,  which  is  a  widely used command
interpreter  on  Unix  systems.  The  bash program reads from standard
input  (the  keyboard).  A  user  types something and the program
will evaluate  what  he  has typed and do something with it, like
running a program.

%package lite
Summary: The Bourne Again Shell - lite version
Group: System/Base

%description lite
The Bourne Again Shell - lite version

%prep
%setup -q -n %{altname}-%{ver}
%patch0 -p1

%build
%configure --without-bash-malloc --without-installed-readline
%{__make} %{_smp_mflags}
mv bash sh
%{__make} clean
%configure --without-bash-malloc --with-installed-readline
%{__make} %{_smp_mflags}
#%%{__make} tests || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

cp sh ${RPM_BUILD_ROOT}/bin/

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

mkdir -p ${RPM_BUILD_ROOT}/bin/

mv ${RPM_BUILD_ROOT}%{_bindir}/bash ${RPM_BUILD_ROOT}/bin/
#mv ${RPM_BUILD_ROOT}%{_bindir}/bashbug ${RPM_BUILD_ROOT}/bin/

#cd ${RPM_BUILD_ROOT}/bin
#ln -s bash sh

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{altname}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES COMPAT NEWS NOTES POSIX RBASH README Y2K
%doc doc/FAQ doc/INTRO doc/article.ms
%doc examples
/bin/bash
%{_bindir}/bashbug
%doc %{_infodir}/*
%doc %{_man1dir}/*

%files lite
%defattr(-,root,root)
/bin/sh

%changelog
* Mon Jan 31 2005 Igor Zubkov <icesik@mail.ru> 2.05b-los3
- split out /bin/sh in to bash2-lite.
- disable tests.

* Fri Nov 19 2004 Igor Zubkov <icesik@mail.ru> 2.05b-los2
- new patch with all official fixes.

* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 2.05b-los1
- Initial build for Los Angeles GNU/Linux.
