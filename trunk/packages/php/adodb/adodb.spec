# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Unique interface to access different SQL databases.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define	name		adodb
%define	ver		4.54
%define	rel		los1

Summary:	%{sum}
Name:		php-%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	BSD and LGPL
Group:		PHP
Source0:	adodb454.tgz
Url:		http://adodb.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	noarch

Requires:	php

%description
PHP's database access functions are not standardised. This creates a
need for a database class library to hide the differences between the
different databases (encapsulate the differences) so we can easily
switch databases.

We currently support MySQL, Interbase, Sybase, PostgreSQL, Oracle,
Microsoft SQL server,  Foxpro ODBC, Access ODBC, Informix, DB2,
Sybase SQL Anywhere, generic ODBC and Microsoft's ADO.

%prep
%setup -q -n adodb

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/
cd ..
cp -pr adodb ${RPM_BUILD_ROOT}%{_datadir}/
cd adodb

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}

%files
%defattr(-,root,root)
%{_datadir}/adodb/

%changelog
* Thu Feb 10 2005 Igor Zubkov <icesik@mail.ru> 4.54-los1
- Initial build for Los Angeles GNU/Linux.
