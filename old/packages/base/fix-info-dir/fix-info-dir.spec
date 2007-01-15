# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

Summary:	Creates a top-level info `dir' file.
Summary(pl):	Tworzy g³ówny plik 'dir' dla systemu Info.
Name:		fix-info-dir
Version:	0.13
Release:	los1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.pld.org.pl/software/fix-info-dir/fix-info-dir-%{version}.tar.gz
BuildRequires:	libz-dev
Requires:	libz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Utility which creates a top-level `dir' file in the Info system.

%description -l pl
Narzêdzie tworz±ce g³ówny plik 'dir' dla systemu Info

%prep
%setup -q

%build
%{__make} CFLAGS="${RPM_OPT_FLAGS} -fomit-frame-pointer -DNDEBUG" \
	%{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}/

install %{name} ${RPM_BUILD_ROOT}%{_sbindir}

touch ${RPM_BUILD_ROOT}%{_infodir}/{dir,dir.old}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post
%{_sbindir}/fix-info-dir %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%ghost %{_infodir}/dir
%ghost %{_infodir}/dir.old

%changelog
* Fri Mar 11 2005 Igor Zubkov <icesik@mail.ru> 0.13-los1
- Initial build for Los Angeles GNU/Linux.
