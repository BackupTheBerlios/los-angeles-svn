# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The Bourne Again Shell.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		bash
%define ver		3.0
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Shells
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Obsoletes:	bash2
Obsoletes:	bash2-lite

BuildRequires:	libncurses-dev
Requires:	libncurses

BuildRequires:	libreadline5-dev
Requires:	libreadline5

%description
bash  is  the  Bourne-Again  SHell,  which  is  a  widely used command
interpreter  on  Unix  systems.  The  bash program reads from standard
input  (the  keyboard).  A  user  types something and the program
will evaluate  what  he  has typed and do something with it, like
running a program.

%prep
%setup -q

%build
%configure --without-bash-malloc --with-installed-readline
%{__make} %{_smp_mflags}
#{__make} tests || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

mkdir -p ${RPM_BUILD_ROOT}/bin/

mv ${RPM_BUILD_ROOT}%{_bindir}/bash ${RPM_BUILD_ROOT}/bin/
cd ${RPM_BUILD_ROOT}/bin
ln -s bash sh

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES COMPAT NEWS NOTES POSIX RBASH README Y2K
%doc doc/FAQ doc/INTRO doc/article.ms
%doc examples
/bin/sh
/bin/bash
%{_bindir}/bashbug
%doc %{_infodir}/*
%doc %{_man1dir}/*
%{_datadir}/locale/en@boldquot/*/bash.mo
%{_datadir}/locale/en@quot/*/bash.mo

%changelog
* Tue Mar 29 2005 Igor Zubkov <icesik@mail.ru> 3.0-los1
- update to 3.0.
- remove bash2-lite package.
- rename bash2 to bash.

* Mon Jan 31 2005 Igor Zubkov <icesik@mail.ru> 2.05b-los3
- split out /bin/sh in to bash2-lite.
- disable tests.

* Fri Nov 19 2004 Igor Zubkov <icesik@mail.ru> 2.05b-los2
- new patch with all official fixes.

* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 2.05b-los1
- Initial build for Los Angeles GNU/Linux.
