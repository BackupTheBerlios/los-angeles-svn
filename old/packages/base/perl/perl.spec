# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Practical Extraction and Report Language
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		perl
%define ver		5.8.6
%define rel		los1

%define __find_requires	%{_builddir}/%{name}-%{version}/my-find-requires

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	Artistic
Group:		System/Base
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The  Perl  package  contains perl, the Practical Extraction and Report
Language.  Perl  combines some of the best features of C, sed, awk and
sh into one powerful language.

%prep
%setup -q

%build
mkdir -p %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
cat > my-find-requires << EOF
/usr/lib/rpm/find-requires | grep -v perl
EOF
chmod +x my-find-requires

./configure.gnu --prefix=%{_prefix} \
    -Dinstallprefix=${RPM_BUILD_ROOT}%{_prefix} \
    -Dcf_by='Los Angeles GNU/Linux' \
    -Dusethreads -Duseithreads
%{__make} %{_smp_mflags}
#make test || exit 1

%install
%{__make} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS Artistic Changes Changes5.* Copying INSTALL MANIFEST
%doc README README.* Todo.micro
/usr/bin/
/usr/lib/
%doc %{_mandir}/*/*

%changelog
* Sun Mar 27 2005 Igor Zubkov <icesik@mail.ru> 5.8.6-los1
- update to 5.8.6.
- build man pages.
- remove any perl requires from perl package.
- move all man pages to perl package from perl-man package.
- move all docs to perl package from perl-doc package.
- mark all man pages as docs.

* Sun Jan 16 2005 Igor Zubkov <icesik@mail.ru> 5.8.5-los1
- update to 5.8.5
- disable build man pages.

* Mon Nov 29 2004 Igor Zubkov <icesik@mail.ru> 5.8.4-los1
- update to 5.8.4

* Sat Feb 14 2004 Igor Zubkov <icesik@mail.ru> 5.8.0-los1
- Initial build for Los Angeles GNU/Linux.
