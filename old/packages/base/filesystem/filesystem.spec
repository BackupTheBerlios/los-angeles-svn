# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		File system skelet.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		filesystem
%define ver		0.1
%define rel		los3

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	free
Group:		System/Base
Source1:	fhs-2.3.txt.gz
Source2:	fhs-2.3.html.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch
Autoreq:	off
Provides:	filesystem

%description
Base file system skelet.

%prep
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
%install
mkdir -p ${RPM_BUILD_ROOT}/
cd ${RPM_BUILD_ROOT}
mkdir -p {bin,boot,dev,etc,lib,media,mnt,opt,sbin,srv,tmp,usr,var}
mkdir -p {home,proc,root,sys}

cd dev/
mkdir {pts,shm}
cd ..

cd media/
mkdir {cdrom,floppy}
cd ..

cd usr/

mkdir -p {bin,etc,include,lib,sbin,share,src,local}
mkdir -p share/{dict,doc,info,locale,man}
mkdir -p share/{nls,misc,terminfo,zoneinfo}
mkdir -p share/man/man{1,2,3,4,5,6,7,8}

cd local

mkdir -p {bin,etc,include,lib,sbin,share,src}
mkdir -p share/{dict,doc,info,locale,man}
mkdir -p share/{nls,misc,terminfo,zoneinfo}
mkdir -p share/man/man{1,2,3,4,5,6,7,8}

cd ..
cd ..

mkdir -p var/{lock,log,mail,run,spool}
mkdir -p var/{tmp,opt,cache,lib/misc,local}
mkdir -p opt/{bin,doc,include,info}
mkdir -p opt/{lib,man/man{1,2,3,4,5,6,7,8}}

chmod 0750 root
chmod 1777 tmp var/tmp

%clean
rm -rf %{buildroot}
rm -f %{_builddir}/fhs-2.3.txt.gz
rm -f %{_builddir}/fhs-2.3.html.gz

%files
%defattr(-,root,root)
%doc fhs-2.3.txt.gz fhs-2.3.html.gz
/

%changelog
* Sat Feb 05 2005 Igor Zubkov <icesik@mail.ru> 0.1-los3
- add /dev/pts dir.
- add /dev/shm dir.
- add /media/cdrom dir.
- add /media/floppy dir.
- clean up after build.

* Tue Dec 07 2004 Igor Zubkov <icesik@mail.ru> 0.1-los2
- add /sys dir.

* Tue Jun 01 2004 Igor Zubkov <icesik@mail.ru> 0.1-los1
- Initial build for Los Angeles GNU/Linux.
