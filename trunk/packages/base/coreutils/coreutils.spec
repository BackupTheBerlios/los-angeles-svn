# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: run expensive tests

%define sum		The GNU core utilities: a set of tools commonly used in shell scripts
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		coreutils
%define ver		5.2.1
%define rel		los3

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-los-kill-uptime.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
These are the GNU core utilities.  This package is the combination of
the old GNU fileutils, sh-utils, and textutils packages.

%prep
%setup -q
%patch0 -p1

%build
DEFAULT_POSIX2_VERSION=199209 %configure
%{__make} %{_smp_mflags}
#%%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

mkdir -p ${RPM_BUILD_ROOT}/bin/
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}

#mv ${RPM_BUILD_ROOT}%{_bindir}/{basename,cat,chgrp,chmod,chown,cp,dd,df} ${RPM_BUILD_ROOT}/bin
#mv ${RPM_BUILD_ROOT}%{_bindir}/{dir,dircolors,du,date,echo,false,head} ${RPM_BUILD_ROOT}/bin
#mv ${RPM_BUILD_ROOT}%{_bindir}/{install,ln,ls,mkdir,mkfifo,mknod,mv,pwd} ${RPM_BUILD_ROOT}/bin
#mv ${RPM_BUILD_ROOT}%{_bindir}/{rm,rmdir,shred,sync,sleep,stty,su,test} ${RPM_BUILD_ROOT}/bin
##mv ${RPM_BUILD_ROOT}%{_bindir}/{touch,true,uname,vdir} ${RPM_BUILD_ROOT}/bin
#mv ${RPM_BUILD_ROOT}%{_bindir}/{touch,true,uname,vdir,[} ${RPM_BUILD_ROOT}/bin
#mv ${RPM_BUILD_ROOT}%{_bindir}/chroot ${RPM_BUILD_ROOT}%{_sbindir}/

mv ${RPM_BUILD_ROOT}%{_bindir}/{[,basename,cat,chgrp,chmod,chown,cp,dd,df} ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}%{_bindir}/{date,echo,false,head,install,ln,ls} ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}%{_bindir}/{mkdir,mknod,mv,pwd,rm,rmdir,sync} ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}%{_bindir}/{sleep,stty,test,touch,true,uname} ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}%{_bindir}/hostname ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}%{_bindir}/chroot ${RPM_BUILD_ROOT}%{_sbindir}/

#ln -s test ${RPM_BUILD_ROOT}/bin/[
ln -s ../../bin/install ${RPM_BUILD_ROOT}%{_bindir}

# remove groups man page
cd ${RPM_BUILD_ROOT}%{_man1dir}
rm -rf groups.1*

# remove su man page (it already in shadow)
rm -rf su.1*

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post
/usr/bin/install-info %{_infodir}/coreutils.info.gz %{_infodir}/dir

%preun
if [ $1 = 0 ]; then
# uninstall the info reference in the dir file
/usr/bin/install-info --delete %{_infodir}/coreutils.info.gz %{_infodir}/dir
fi

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS THANKS-to-translators TODO old
/bin/*
%{_bindir}/*
%{_sbindir}/*
%doc %{_infodir}/coreutils.*
%doc %{_man1dir}/*

%changelog
* Sat Feb 06 2005 Igor Zubkov <icesik@mail.ru> 5.2.1-los3
- move back /bin/hostname!
- corect install info files.
- disable checks

* Fri Dec 17 2004 Igor Zubkov <icesik@mail.ru> 5.2.1-los2
- remove su man page
- remove groups man page

* Mon Jun 14 2004 Igor Zubkov <icesik@mail.ru> 5.2.1-los1
- update to 5.2.1

* Wed May 19 2004 Igor Zubkov <icesik@mail.ru> 5.0-los1
- Initial build for Los Angeles GNU/Linux.
