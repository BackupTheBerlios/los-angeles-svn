# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A tool for creating scanners (text pattern recognizers).
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		flex
%define ver		2.5.31
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	BSD
Group:          Development/Other
Group(ru_RU.KOI8-R):	Разработка/Разное
Source0:        %{name}-%{version}.tar.bz2
Buildroot:      %{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	task-c++-devel
Requires:	libstdc++

%description
The flex program generates scanners.  Scanners are programs which can
recognize lexical patterns in text.  Flex takes pairs of regular
expressions and C code as input and generates a C source file as
output.  The output file is compiled and linked with a library to
produce an executable.  The executable searches through its input for
occurrences of the regular expressions.  When a match is found, it
executes the corresponding C code.  Flex was designed to work with
both Yacc and Bison, and is used by many programs as part of their
build process.

You should install flex if you are going to use your system for
application development.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
make DESTDIR=${RPM_BUILD_ROOT} install
cd ${RPM_BUILD_ROOT}%{_bindir}/
ln -sf flex lex
cd ${RPM_BUILD_ROOT}%{_man1dir}/
ln -s flex.1 lex.1
ln -s flex.1 flex++.1
cd ${RPM_BUILD_ROOT}%{_libdir}/
ln -s libfl.a libl.a

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS ONEWS README README-alpha README.cvs-snapshot
%doc RoadMap THANKS TODO
%{_bindir}/*
%doc %{_man1dir}/*
%doc %{_infodir}/*
%{_libdir}/*
%{_includedir}/FlexLexer.h
%{_datadir}/locale/*/*/flex.mo

%changelog
* Wed Dec 08 2004 Igor Zubkov <icesik@mail.ru> 2.5.31-los1
- update to 2.5.31

* Wed Nov 03 2004 Igor Zubkov <icesik@mail.ru> 2.5.4a-los1
- Initial build for Los Angeles GNU/Linux.
