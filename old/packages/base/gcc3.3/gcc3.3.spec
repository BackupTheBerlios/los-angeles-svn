# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU cc and gcc C compilers.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		gcc3.3
%define altname		gcc
%define ver		3.3.3
%define rel		los1
%define url		http://gcc.gnu.org/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/C
Source0:	%{altname}-%{version}.tar.bz2
Patch0:		gcc-3.3.3-no_fixincludes-1.patch
Patch1:		gcc-3.3.2-suppress-libiberty-1.patch
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The gcc package includes the cc and gcc GNU compilers for compiling C
code.

%package -n g++3.3
Summary: C++ support for the GNU gcc compiler.
Group: Development/C++

%description -n g++3.3
The gcc-c++ package adds C++ support to the GNU C compiler. It
includes support for most of the current C++ specification, including
templates and exception handling. The static standard C++ library and
C++ header files are included; however, the library for dynamically
linking programs is available separately.

%package -n libstdc++3.3
Summary: The GNU Standard C++ Library v3.
Group: Libraries

%description -n libstdc++3.3
The libstdc++ package contains a snapshot of the GNU Standard C++
Library v3, an ongoing project to implement the ISO 14882 Standard C++
library.

%package -n libstdc++3.3-dev
Summary: The header files and libraries needed for C++ development.
Group: Developer/C++

%description -n libstdc++3.3-dev
The libstdc++ library is the GNU implementation of the standard C++
libraries. This package includes the header files and libraries
needed for C++ development, including SGI's implementation of the
STL.

%package -n cpp3.3
Summary: Cpp is the GNU C-Compatible Compiler Preprocessor.
Summary(ru_RU.KOI8-R): ������������ C.
Group: Developer/C

%description -n cpp3.3
Cpp is the GNU C-Compatible Compiler Preprocessor. Cpp is a macro
processor which is used automatically by the C compiler to transform
your program before actual compilation. It is called a macro processor
because it allows you to define macros (abbreviations for longer
constructs).

The C preprocessor provides four separate functionalities: the
inclusion of header files (files of declarations that can be
substituted into your program); macro expansion (you can define macros
and the C preprocessor will replace the macros with their definitions
throughout the program); conditional compilation (using special
preprocessing directives, you can include or exclude parts of the
program according to various conditions); and line control (if you use
a program to combine or rearrange source files into an intermediate
file which is then compiled, you can use line control to inform the
compiler about where each source line originated).

%package -n libgcc3.3
Summary: libgcc3.3
Group: System/Base

%description -n libgcc3.3
libgcc3.3

%prep
%setup -q -n %{altname}-%{ver}
%patch0 -p1
%patch1 -p1

%build
mv ChangeLog ChangeLog.all
%configure --enable-shared --enable-threads=posix --enable-__cxa_atexit --enable-clocale=gnu --enable-languages=c,c++
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

cd ${RPM_BUILD_ROOT}%{_mandir}/man7/

rm -rf fsf-funding.*
rm -rf gfdl.*
rm -rf gpl.*

%post -n libstdc++3.3 -p /sbin/ldconfig
%postun -n libstdc++3.3 -p /sbin/ldconfig

%post -n libgcc3.3 -p /sbin/ldconfig
%postun -n libgcc3.3 -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{altname}-%{ver}

%files
%defattr(-,root,root)
%doc gcc/ChangeLog* gcc/FSFChangeLog* gcc/README-fixinc gcc/README.Portability
%doc gcc/ABOUT-GCC-NLS gcc/NEWS gcc/ONEWS
%doc BUGS ChangeLog.all FAQ MAINTAINERS README README.SCO bugs.html
%{_bindir}/gcc
%{_bindir}/*-pc-linux-gcc-%{ver}
%{_bindir}/*-pc-linux-gcc
%{_bindir}/gcov
%{_bindir}/gccbug
%{_datadir}/locale/*/*/gcc.mo
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/include/*.h
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/collect2
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/crtbegin.o
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/crtbeginS.o
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/crtbeginT.o
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/crtend.o
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/crtendS.o
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/specs
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/libgcc.a
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/libgcc_eh.a
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/install-tools/
%doc %{_infodir}/gcc.*
%doc %{_infodir}/gccint.*
%doc %{_mandir}/man1/gcc.*
%doc %{_mandir}/man1/gcov.*

%files -n g++3.3
%defattr(-,root,root)
%doc gcc/cp/ChangeLog* gcc/cp/NEWS
%{_bindir}/c++
%{_bindir}/g++
%{_bindir}/*-pc-linux-g++
%{_bindir}/*-pc-linux-c++
%doc %{_mandir}/man1/g++.*
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/cc1plus

%files -n libstdc++3.3
%defattr(-,root,root)
%{_libdir}/libstdc++.so
%{_libdir}/libstdc++.so.*
%{_datadir}/locale/*/*/libstdc++.mo

%files -n libstdc++3.3-dev
%defattr(-,root,root)
%doc libstdc++-v3/ChangeLog libstdc++-v3/ChangeLog-2000
%doc libstdc++-v3/ChangeLog-2001 libstdc++-v3/README libstdc++-v3/docs/html
%{_includedir}/c++/%{ver}/
%{_libdir}/libsupc++.la
%{_libdir}/libsupc++.a
%{_libdir}/libstdc++.la
%{_libdir}/libstdc++.a

%files -n cpp3.3
%defattr(-,root,root)
%{_bindir}/cpp
%{_libdir}/gcc-lib/*-pc-linux/%{ver}/cc1
%doc %{_infodir}/cpp.*
%doc %{_infodir}/cppinternals.*
%doc %{_mandir}/man1/cpp.*

%files -n libgcc3.3
%defattr(-,root,root)
%{_libdir}/libgcc_s.so
%{_libdir}/libgcc_s.so.1

%changelog
* Mon Nov 29 2004 Igor Zubkov <icesik@mail.ru> 3.3.3-los1
- Initial build for Los Angeles GNU/Linux.
