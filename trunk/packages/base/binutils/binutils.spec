# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A GNU collection of binary utilities.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		binutils
%define ver		2.15
%define rel		los2

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), size (for listing the section sizes of an
object or archive file), strings (for listing printable strings from
files), strip (for discarding symbols), and addr2line (for converting
addresses to file and line).

%prep
%setup -q

%build
%configure --enable-shared
%{__make} tooldir=%{_prefix} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} tooldir=/usr install
cp include/libiberty.h ${RPM_BUILD_ROOT}%{_prefix}/include

# Remove Windows/Novell only man pages
rm -f %{buildroot}%{_mandir}/man1/{dlltool,nlmconv,windres}*

# This one comes from gcc
rm -f %{buildroot}%{_prefix}/bin/c++filt
rm -rf %{buildroot}%{_prefix}/%{_target_platform}

# Remove this so the system info dir gets updated properly
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*.h
%{_datadir}/locale/*/*/*.mo
%doc %{_infodir}/*
%doc %{_man1dir}/*

%changelog
* Fri Jan 28 2005 Igor Zubkov <icesik@mail.ru> 2.15-los2
- rebuild

* Mon Nov 29 2004 Igor Zubkov <icesik@mail.ru> 2.15-los1
- update to 2.15

* Wed May 19 2004 Igor Zubkov <icesik@mail.ru> 2.13.2.1-los1
- Initial build for Los Angeles GNU/Linux.
