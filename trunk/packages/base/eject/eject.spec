# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A program that ejects removable media using software control.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		eject
%define ver		2.0.13
%define rel		los1
%define url		http://www.pobox.com/~tranter

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	http://metalab.unc.edu/pub/Linux/utils/disk-management/%{name}-%{version}.tar.gz
Patch0:		%{name}-2.0.12-autoclose.patch
URL:		%{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
ExcludeArch:	s390 s390x

%description
The eject program allows the user to eject removable media (typically
CD-ROMs, floppy disks or Iomega Jaz or Zip disks) using software
control. Eject can also control some multi-disk CD changers and even
some devices' auto-eject features.

Install eject if you'd like to eject removable media using software
control.

%prep
%setup -q
%patch0 -p0

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README TODO ChangeLog NEWS PORTING PROBLEMS
%{_bindir}/*
%doc %{_man1dir}/*

%changelog
* Sun Nov 29 2004 Igor Zubkov <icesik@mail.ru> 2.0.13-los1
- Initial build for Los Angeles GNU/Linux.
