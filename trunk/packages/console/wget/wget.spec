# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A utility for retrieving files using the HTTP or FTP protocols.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		wget
%define ver		1.9.1
%define rel		los3

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Unknown
Source0:	%{name}-%{ver}.tar.gz
Source1:	%{name}-%{ver}.tar.gz.sig
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Provides:	webclient

Prereq:		/usr/bin/install-info

BuildRequires:	perl
BuildRequires:	openssl-dev
Requires:	openssl

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you are logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%prep
%setup -q

%build
%configure --with-ssl
%{__make} %{_smp_mflags}

%install
%makeinstall

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%post
/usr/bin/install-info %{_infodir}/wget.info.gz %{_infodir}/dir

%preun
if [ "$1" = 0 ]; then
    /usr/bin/install-info --delete %{_infodir}/wget.info.gz %{_infodir}/dir
fi

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog ChangeLog.README INSTALL MACHINES MAILING-LIST NEWS
%doc PATCHES README README.cvs TODO doc/ChangeLog
%doc doc/ChangeLog-branches/1.6_branch.ChangeLog
%config(noreplace) %{_sysconfdir}/wgetrc
%{_bindir}/wget
%doc %{_man1dir}/wget.*
%doc %{_infodir}/*

%changelog
* Mon Feb 14 2005 Igor Zubkov <icesik@mail.ru> 1.9.1-los3
- clean up and commit.

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 1.9.1-los2
- remove Vendor field.

* Thu Jun 10 2004 Igor Zubkov <icesik@mail.ru> 1.9.1-los1
- update to 1.9.1

* Wed May 19 2004 Igor Zubkov <icesik@mail.ru> 1.8.2-los1
- Initial build for Los Angeles GNU/Linux.
