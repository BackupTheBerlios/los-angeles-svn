# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		GNU time Utility.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		time
%define ver		1.7
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Other
Group(ru_RU.KOI8-R):	Разработка/Разное
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
`time' is a program that measures many of the CPU resources, such as
time and memory, that other programs use.  The GNU version can format
the output in arbitrary ways by using a printf-style format string to
include various resource measurements.  Some systems do not provide
much information about program resource use; `time' reports
unavailable information as zero values.

%prep
%setup -q

%build
#echo "ac_cv_func_wait3=\${ac_cv_func_wait3='yes'}" >> config.cache
%configure
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}/
install -c time ${RPM_BUILD_ROOT}%{_bindir}/
install -c -m 644 ./time.info ${RPM_BUILD_ROOT}%{_infodir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post
/usr/bin/install-info %{_infodir}/time.info.gz %{_infodir}/dir \
        --entry="* time: (time).                GNU time Utility"

%preun
if [ "$1" = 0 ]; then
    /usr/bin/install-info --delete %{_infodir}/time.info.gz %{_infodir}/dir \
        --entry="* time: (time).                GNU time Utility"
fi

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%doc %{_infodir}/*

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 1.7-los2
- remove Vendor field.
- change Group to Development/Other.
- add russian group description.

* Tue Nov 16 2004 Igor Zubkov <icesik@mail.ru> 1.7-los1
- Initial build for Los Angeles GNU/Linux.
