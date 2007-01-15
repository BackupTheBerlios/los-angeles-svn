Summary:	MPEG audio decoder
Name:		libmad
Version:	0.15.1b
Release:	los1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.mars.org/pub/mpeg/libmad-%{version}.tar.gz
URL:		http://www.mars.org/home/rob/proj/mpeg/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libz-dev

#BuildRequires:	esound-devel
#BuildRequires:	libao-devel

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II
and Layer III a.k.a. MP3) are fully implemented.

%package dev
Summary:	Header files for libmad
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
Header files for libmad.

%prep
%setup -q

%build
%configure \
	--enable-static \
	--disable-debugging \
	--enable-shared
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean

%files
%defattr(-,root,root)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/lib*.so.*

%files dev
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/*.h
#%{_libdir}/pkgconfig/*

%changelog
