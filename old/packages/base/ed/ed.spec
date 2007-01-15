# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU line editor.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		ed
%define ver		0.2
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source:		%{name}-%{ver}.tar.bz2
Patch0:		%{name}-mkstemp.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Ed is a line-oriented text editor, used to create, display, and modify
text files (both interactively and via shell scripts).  For most
purposes, ed has been replaced in normal usage by full-screen editors
(emacs and vi, for example).

Ed was the original UNIX editor, and may be used by some programs.  In
general, however, you probably don't need to install it and you probably
won't use it.

%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=%{_prefix}
%{__make} CFLAGS="${RPM_OPT_FLAGS}" %{_smp_mflags}
%{__make} check || exit 1

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}/
mkdir -p ${RPM_BUILD_ROOT}%{_man1dir}/
install -c ed ${RPM_BUILD_ROOT}%{_bindir}/ed
install -c -m 644 ./ed.info ${RPM_BUILD_ROOT}%{_infodir}/ed.info
install -c -m 644 ./ed.1 ${RPM_BUILD_ROOT}%{_man1dir}/ed.1
cd ${RPM_BUILD_ROOT}%{_bindir}/
ln -s ed red
cd ${RPM_BUILD_ROOT}%{_man1dir}/
ln -s ed.1 red.1

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc ChangeLog NEWS POSIX README THANKS TODO
%{_bindir}/*
%doc %{_infodir}/*
%doc %{_man1dir}/*

%changelog
* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 0.2-los1
- Initial build for Los Angeles GNU/Linux.
