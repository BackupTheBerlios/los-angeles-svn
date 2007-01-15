# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Tools for managing a frame buffer's video mode properties.
%define sum_ru		Утилиты для управление параметрами framebuffer'а.
%define maintainer	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		fbset
%define ver		2.1
%define rel		los2

Summary:	%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Utils
Source0:	fbset-2.1.tar.gz
Patch0:		%{name}-%{ver}-makefile.patch
Patch1:		%{name}-%{ver}-fixmode.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Fbset is a utility for maintaining frame buffer resolutions.  Fbset
can change the video mode properties of a frame buffer device, and is
usually used to change the current video mode.

Install fbset if you need to manage frame buffer resolutions.

%description -l ru_RU.KOI8-R
Fbset утилита для управления framebuffer'ом. Она позволяет менять
разрешение, частоту развёрстки и цветность экрана. Также с помощью
Fbset вы можете запросить полную информацию о текущем состоянии экрана.

Если вы используете framebuffer рекомендуем установить этот пакет.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} %{_smp_mflags}

%install
%makeinstall

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc GetVideoMode.c INSTALL
%config	%{_sysconfdir}/fb.modes
%{_sbindir}/*
%{_mandir}/man[58]/*

%changelog
* Fri Oct 29 2004 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 2.1-los2
- Maintainer change
- Added localization
- Spec's clean up for ideology compatibility.

* Sat May 29 2004 Igor Zubkov <icesik@mail.ru> 2.1-los1
- Initial build for Los Angeles GNU/Linux.
