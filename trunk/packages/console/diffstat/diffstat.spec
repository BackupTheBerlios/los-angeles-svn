# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A utility which provides statistics based on the output of diff.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		diffstat
%define ver		1.28
%define rel		los1
%define url		http://dickey.his.com/diffstat/diffstat.html

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	distributable
Group:		Development/Other
Group(ru_RU.KOI8-R):	Разработка/Разное
Source0:	ftp://dickey.his.com/diffstat/diffstat.tar.gz
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	diffutils

%description
The diff command compares files line by line.  Diffstat reads the
output of the diff command and displays a histogram of the insertions,
deletions and modifications in each file.  Diffstat is commonly used
to provide a summary of the changes in large, complex patch files.

Install diffstat if you need a program which provides a summary of the
diff command's output.  You'll need to also install diffutils.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%makeinstall mandir=${RPM_BUILD_ROOT}%{_man1dir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_bindir}/diffstat
%doc %{_mandir}/*/*

%changelog
* Mon May 31 2004 Igor Zubkov <icesik@mail.ru> 1.28-los1
- Initial build for Los Angeles GNU/Linux.
