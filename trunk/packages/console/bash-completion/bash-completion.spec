# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		bash-completion - some programmable completion functions for bash.
%define sum_ru		bash-completion - функции автодополнения для шелла bash.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		bash-completion
%define ver		20050112
%define rel		los1
%define url		http://www.caliban.org/bash/index.shtml#completion

Summary:		%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:			%{name}
Version:		%{ver}
Release:		%{rel}
Packager:		%{maintainer}
License:		GPL
Group:			Shells
Group(ru_RU.KOI8-R):	Оболочки
Source0:		%{name}-%{version}.tar.bz2
URL:			%{url}
Buildroot:		%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:		noarch

Requires:		bash2

%description
bash-completion - some programmable completion functions for bash.

%description -l ru_RU.KOI8-R
bash-completion - функции автодополнения для шелла bash.

%prep
%setup -q -n bash_completion

%build
%install
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
install -c -m 644 bash_completion ${RPM_BUILD_ROOT}%{_sysconfdir}/bash_completion

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/bash_completion

%files
%doc COPYING BUGS Changelog README contrib
%config(noreplace) %{_sysconfdir}/bash_completion

%changelog
* Thu Jan 13 2005 Igor Zubkov <icesik@mail.ru> 20050112-los1
- update to new stable version 20050112.

* Wed Jan 05 2005 Igor Zubkov <icesik@mail.ru> 20050103-los1
- update to new stable version 20050103.

* Sun Nov 29 2004 Igor Zubkov <icesik@mail.ru> 20041017-los1
- Initial build for Los Angeles GNU/Linux.
