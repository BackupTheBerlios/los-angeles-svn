# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU version of the new awk text processing utility.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		gawk
%define ver		3.1.3
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs.

Install the gawk package if you need a text processing utility. Gawk is
considered to be a standard Linux tool for processing text.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog FUTURES LIMITATIONS NEWS POSIX.STD PROBLEMS README
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/%{name}-%{version}/*
%doc %{_infodir}/*
%doc %{_man1dir}/*

%changelog
* Fri May 14 2004 Igor Zubkov <icesik@mail.ru> 3.1.3-los1
- Initial build for Los Angeles GNU/Linux.
