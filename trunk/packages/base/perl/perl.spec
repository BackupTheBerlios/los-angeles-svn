# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Practical Extraction and Report Language
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		perl
%define ver		5.8.5
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	Artistic
Group:		perl
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The  Perl  package  contains perl, the Practical Extraction and Report
Language.  Perl  combines some of the best features of C, sed, awk and
sh into one powerful language.

%package doc
Summary: Perl documentation.
Group: perl

%description doc
Docs.

#%%package man
#%Summary: Perl mans
#%Group: perl

#%%description man
#%Perl manual pages.

%prep
%setup -q

%build
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
/usr/bin/
/usr/lib/

%files doc
%defattr(-,root,root)
%doc AUTHORS Artistic Changes Changes5.* Copying INSTALL MANIFEST
%doc README README.* Todo.micro

#%%files man
#%%defattr(-,root,root)
#%%{_mandir}/*/*

%changelog
* Sun Jan 16 2005 Igor Zubkov <icesik@mail.ru> 5.8.5-los1
- update to 5.8.5
- disable build man pages.

* Mon Nov 29 2004 Igor Zubkov <icesik@mail.ru> 5.8.4-los1
- update to 5.8.4

* Sat Feb 14 2004 Igor Zubkov <icesik@mail.ru> 5.8.0-los1
- Initial build for Los Angeles GNU/Linux.
