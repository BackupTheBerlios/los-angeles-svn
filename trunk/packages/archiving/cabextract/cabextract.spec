# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: update

%define sum		a program to extract Microsoft Cabinet files
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		cabextract
%define ver		0.6
%define rel		los1
%define url		http://www.kyz.uklinux.net/cabextract.php3

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.kyz.uklinux.net/downloads/%{name}-%{ver}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%makeinstall

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(0644, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%attr(0755, root, root) %{_bindir}/cabextract
%doc %{_mandir}/man1/cabextract.1*

%changelog
* Fri Dec 03 2004 Igor Zubkov <icesik@mail.ru> 0.6-los1
- Initial build for Los Angeles GNU/Linux.
