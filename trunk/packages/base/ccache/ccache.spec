# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Compiler Cache
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		ccache
%define ver		2.4
%define rel		los1
%define url		http://ccache.samba.org/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Other
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.gz
URL:		%{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

#Requires:	gcc3.3

%description
ccache caches gcc output files

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
install -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}/
install -m 0755 ccache ${RPM_BUILD_ROOT}%{_bindir}/
install -d -m 0755 ${RPM_BUILD_ROOT}%{_man1dir}/
install -m 0644 ccache.1 ${RPM_BUILD_ROOT}%{_man1dir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README web
%{_bindir}/ccache
%doc %{_man1dir}/ccache.1*

%changelog
* Fri Dec 10 2004 Igor Zubkov <icesik@mail.ru> 2.4-los1
- Initial build for Los Angeles GNU/Linux.
