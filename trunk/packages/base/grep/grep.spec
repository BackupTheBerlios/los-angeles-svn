# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU versions of grep pattern matching utilities.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		grep
%define ver		2.5.1
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-1-option-io-combo-1.patch
Patch1:		%{name}-%{version}-option-w-1.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

#Requires:	libpcre
#BuildRequires:	libpcre-dev

%description
The GNU versions of commonly used grep utilities.  Grep searches
through textual input for lines which contain a match to a specified
pattern and then prints the matching lines.  GNU's grep utilities
include grep, egrep and fgrep.

You should install grep on your system, because it is a very useful
utility for searching through text.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --with-included-regex
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%makeinstall
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README README-alpha README.DOS THANKS TODO
%{_bindir}/*
%doc %{_infodir}/*
%doc %{_man1dir}/*

%changelog
* Sun Jun 06 2004 Igor Zubkov <icesik@mail.ru> 2.5.1-los2
- add patches from linux from scratch.

* Tue May 18 2004 Igor Zubkov <icesik@mail.ru> 2.5.1-los1
- Initial build for Los Angeles GNU/Linux.
