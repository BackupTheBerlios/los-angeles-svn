# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		GNU `m4' is an implementation of the traditional Unix macro processor.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		m4
%define ver		1.4.3
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.tar.bz2.sig
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GNU `m4' is an implementation of the traditional Unix macro
processor.  It is mostly SVR4 compatible, although it has some
extensions (for example, handling more than 9 positional parameters
to macros).  `m4' also has built-in functions for including files,
running shell commands, doing arithmetic, etc.  Autoconf needs GNU
`m4' for generating `configure' scripts, but not for running them.
GNU `m4' has been originally written by René Seindal, from Denmark.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%makeinstall

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc BACKLOG COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/m4
#%{_datadir}/locale/*/*/m4.mo
%doc %{_infodir}/m4.*
#%{_mandir}/man1/m4.*
#%{_datadir}/m4/*

%changelog
* Mon Apr 04 2005 Igor Zubkov <icesik@mail.ru> 1.4.3-los1
- update to 1.4.3.
- run check's.

* Mon Mar 14 2005 Igor Zubkov <icesik@mail.ru> 1.4.2-los1
- update to 1.4.2.

* Thu Jun 10 2004 Igor Zubkov <icesik@mail.ru> 1.4.1-los1
- update (or downgrade ;-)) ) to a new release.

* Wed May 26 2004 Igor Zubkov <icesik@mail.ru> 1.4o-los1
- Initial build for Los Angeles GNU/Linux.
