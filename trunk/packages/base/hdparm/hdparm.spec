# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		hdparm - get/set hard disk parameters for Linux IDE drives.
%define sum_ru		������� ��� ����������� ��� ��������� ���������� (E)IDE ���������.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		hdparm
%define ver		5.7
%define rel		los1
%define url		ftp://ibiblio.org/pub/Linux/system/hardware

Summary:		%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:			%{name}
Version:		%{ver}
Release:		%{rel}
Packager:		%{maintainer}
License:		BSD
Group:			System/Base
Group(ru_RU.KOI8-R):	�������/����
Source0:		%{name}-%{version}.tar.bz2
Source1:		hdparm-sysconfig
Patch0:			hdparm-5.7-alt-makefile.patch
Patch1:			hdparm-5.7-lost1.patch
URL:			%{url}
Buildroot:		%{_tmppath}/%{name}-%{version}-buildroot

%description
Hdparm is a useful system utility for setting (E)IDE hard drive
parameters.  For example, hdparm can be used to tweak hard drive
performance and to spin down hard drives for power conservation.

%description -l ru_RU.KOI8-R
Hdparm - ��� ������� ��������� ������� ��� ��������� ���������� (E)IDE
���������.  ��������, hdparm ����� ���� ����������� ��� ����������
�������� ������ �������� ����� ��� ��� ��������� ������� ��������
���������� ��� ���������� ������� (��� ��������� ����).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
mkdir -p ${RPM_BUILD_ROOT}/sbin/
mkdir -p ${RPM_BUILD_ROOT}%{_man8dir}/

%{__make} DESTDIR=${RPM_BUILD_ROOT} install

#install -pD -m644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/harddisks
#mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/harddisk

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc Changelog README.acoustic hdparm-sysconfig hdparm.lsm contrib
/sbin/*
%doc %{_man8dir}/*

%changelog
* Tue Nov 16 2004 Igor Zubkov <icesik@mail.ru> 5.7-los1
- Initial build for Los Angeles GNU/Linux.
