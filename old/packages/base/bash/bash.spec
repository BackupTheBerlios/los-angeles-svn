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
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Shells
Source0:	%{name}-%{version}.tar.gz

# official patches and signes
Patch001:	bash30-001
Source001:	bash30-001.sig
Patch002:	bash30-002
Source002:	bash30-002.sig
Patch003:	bash30-003
Source003:	bash30-003.sig
Patch004:	bash30-004
Source004:	bash30-004.sig
Patch005:	bash30-005
Source005:	bash30-005.sig
Patch006:	bash30-006
Source006:	bash30-006.sig
Patch007:	bash30-007
Source007:	bash30-007.sig
Patch008:	bash30-008
Source008:	bash30-008.sig
Patch009:	bash30-009
Source009:	bash30-009.sig
Patch010:	bash30-010
Source010:	bash30-010.sig
Patch011:	bash30-011
Source011:	bash30-011.sig
Patch012:	bash30-012
Source012:	bash30-012.sig
Patch013:	bash30-013
Source013:	bash30-013.sig
Patch014:	bash30-014
Source014:	bash30-014.sig
Patch015:	bash30-015
Source015:	bash30-015.sig
Patch016:	bash30-016
Source016:	bash30-016.sig

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
%patch001 -p0
%patch002 -p0
%patch003 -p0
%patch004 -p0
%patch005 -p0
%patch006 -p0
%patch007 -p0
%patch008 -p0
%patch009 -p0
%patch010 -p0
%patch011 -p0
%patch012 -p0
%patch013 -p0
%patch014 -p0
%patch015 -p0
%patch016 -p0

%build
%configure \
	--without-bash-malloc \
	--with-installed-readline
%{__make} %{_smp_mflags}
#{__make} tests || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

mkdir -p ${RPM_BUILD_ROOT}/bin/

mv ${RPM_BUILD_ROOT}%{_bindir}/bash ${RPM_BUILD_ROOT}/bin/
cd ${RPM_BUILD_ROOT}/bin
ln -s bash sh

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
* Mon Apr 04 2005 Igor Zubkov <icesik@mail.ru> 3.0-los2
- add all official patches.
- fix install info files.

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
