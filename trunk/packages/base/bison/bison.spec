# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Bison parser generator. yacc replacement.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		bison
%define ver		1.875
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-attribute.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Bison is a parser generator, a replacement for yacc. Bison generates 
a program that analyzes the structure of a text file.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}
                                                                                
%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS OChangeLog README REFERENCES THANKS TODO doc/FAQ
%{_bindir}/*
%{_datadir}/bison/*
%{_libdir}/*
%doc %{_man1dir}/*
%doc %{_infodir}/*

%changelog
* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 1.875-los1
- Initial build for Los Angeles GNU/Linux.
