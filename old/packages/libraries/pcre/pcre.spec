Summary:	Perl-Compatible Regular Expression library
Name:		pcre
Version:	5.0
Release:	los1
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
PCRE stands for the Perl Compatible Regular Expression library. It
contains routines to match text against regular expressions similar to
Perl's. It also contains a POSIX compatibility library.

%package dev
Summary:	Perl-Compatible Regular Expression header files and development documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
Perl-Compatible Regular Expression header files and development
documentation.

%package -n pcregrep
Summary:	Grep using Perl Compatible Regular Expressions
Group:		Applications/Text
License:	GPL

%description -n pcregrep

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-utf8 \
	--enable-shared
%{__make}

%install
mkdir -p ${RPM_BUILD_ROOT}/lib

%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS
%{_bindir}/pcretest
%{_libdir}/lib*.so.*
%{_man1dir}/pcretest.*

%files dev
%defattr(644,root,root,755)
%{_bindir}/pcre-config
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_man3dir}/*
%{_includedir}/*
%{_libdir}/pkgconfig/libpcre.pc

%files -n pcregrep
%defattr(644,root,root,755)
%{_bindir}/pcregrep
%{_man1dir}/pcregrep.*

%changelog
