# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A file compression utility.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		bzip2
%define ver		1.0.3
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-los-build.patch
License:	BSD
Group:		System/Base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities
of the best techniques available.  However, bzip2 has the added benefit
of being approximately two times faster at compression and six times
faster at decompression than those techniques.  Bzip2 is not the
fastest compression utility, but it does strike a balance between speed
and compression capability.

Install bzip2 if you need a compression utility.

%package dev
Summary: Development files for bzip2.
Group: Developent/C
Requires: %{name} = %{version}-%{release}

%description dev
Development files for bzip2.

%package manual
Summary: Bzip2 manual.
Group: Documentation

%description manual
Bzip2 manual.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f Makefile-libbz2_so %{_smp_mflags}
%{__make} clean
%{__make} %{_smp_mflags}

%install
%{__make} PREFIX=${RPM_BUILD_ROOT}%{_prefix} install
mkdir -p ${RPM_BUILD_ROOT}/bin
cp bzip2-shared ${RPM_BUILD_ROOT}/bin/bzip2
cp -a libbz2.so* ${RPM_BUILD_ROOT}%{_libdir}
ln -s libbz2.so.1.0 ${RPM_BUILD_ROOT}%{_libdir}/libbz2.so
rm ${RPM_BUILD_ROOT}%{_bindir}/{bunzip2,bzcat,bzip2}
mv ${RPM_BUILD_ROOT}%{_bindir}/{bzip2recover,bzless,bzmore} \
	${RPM_BUILD_ROOT}/bin
ln -s bzip2 ${RPM_BUILD_ROOT}/bin/bunzip2
ln -s bzip2 ${RPM_BUILD_ROOT}/bin/bzcat

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README README.COMPILATION.PROBLEMS Y2K_INFO
/bin/*
%{_bindir}/*
%{_libdir}/*.so.*
%doc %{_man1dir}/*

%files dev
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/bzlib.h

%files manual
%defattr(-,root,root)
%doc README.XML.STUFF *.xml *.xsl *.css xmlproc.sh format.pl
%doc manual.pdf manual.ps manual.html

%changelog
* Thu Mar 24 2005 Igor Zubkov <icesik@mail.ru> 1.0.3-los1
- update to 1.0.3.
- security upload.
- clean up --target build.
- clean up spec file.
- split out bzip2 manual into bzip2-manual package.

* Thu Mar 04 2004 Igor Zubkov <icesik@mail.ru> 1.0.2-los1
- Initial build for Los Angeles GNU/Linux.
