# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		System V initialization program.
%define sum_ru		Программы, управляющие базовыми системными процессами.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		sysvinit
%define ver		2.86
%define rel		los1

Summary:	%{sum}
Summary(ru):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{ver}.tar.bz2
Patch0:		%{name}-%{ver}-los-rpmflags.patch
License:	GPL v2
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The SysVinit package contains a group of processes that control the
very basic functions of your system. SysVinit includes the init
program, the first program started by the Linux kernel when the system
boots. Init then controls the startup, running and shutdown of all
other programs.

%description -l ru
Пакет SysVinit содержит группу процессов, которые управляют самыми
базовыми функциями вашей системы. SysVinit включает программу init,
самую первую программу, которая запускается ядром Linux при загрузке
системы. После этого init управляет запуском, исполнением и остановом
всех остальных программ.

%prep
%setup -q
%patch0 -p1

%build
cp src/init.c{,.backup}
sed 's/Sending processes/Sending processes started by init/g' \
	src/init.c.backup > src/init.c

%{__make} -C src %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}/bin/
mkdir -p ${RPM_BUILD_ROOT}/sbin/
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,5,8}/
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/

%{__make} -C src ROOT=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc COPYRIGHT doc contrib obsolete
/bin/*
/sbin/*
%{_bindir}/*
%{_includedir}/*
%doc %{_man1dir}/*
%doc %{_man5dir}/*
%doc %{_man8dir}/*

%changelog
* Fri Mar 18 2005 Igor Zubkov <icesik@mail.ru> 2.86-los1
- update to 2.86.

* Fri Jan 28 2005 Igor Zubkov <icesik@mail.ru> 2.85-los5
- move file /etc/inittab to base-scripts.

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 2.85-los4
- s/packager/maintainer.
- remove Vendor field.
- change Group to System/Base.
- add russian group description.

* Tue Dec 14 2004 Igor Zubkov <icesik@mail.ru> 2.85-los3
- clean up.

* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 2.85-los1
- update to 2.85

* Wed May 19 2004 Igor Zubkov <icesik@mail.ru> 2.84-los1
- Initial build for Los Angeles GNU/Linux.
