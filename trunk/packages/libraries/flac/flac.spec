# TODO: xmms-input-plugin ?

Summary:	Free Lossless Audio Codec
Name:		flac
Version:	1.1.2
Release:	los1
License:	GPL v2/LGPL v2
Group:		Libraries
Source0:	http://prdownloads.sf.net/flac/flac-%{version}.tar.gz
URL:		http://flac.sf.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libogg-dev
BuildRequires:	task-c++-devel
BuildRequires:	nasm
#BuildRequires:	xmms-devel
#BuildRequires:	id3lib-devel

#define		_xmms_input_path	#(xmms-config --input-plugin-dir)

%description
FLAC is an Open Source lossless audio codec developed by Josh Coalson.

%package dev
Summary:	FLAC - development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-dev
#Requires:	libstdc++-devel

%description dev
The package contains the development header files for flac.

#%package -n xmms-input-flac
#Summary: 	Free Lossless Audio Codec - XMMS plugin
#License:	LGPL v2
#Group:		Libraries
#Requires:	%{name} = %{version}-%{release}
#Requires:	xmms
#
#%description -n xmms-input-flac
#FLAC input plugin for XMMS.

%prep
%setup -q

%build
%configure \
	--disable-static
#	%{?_with_xmms:--with-id3lib=%{_prefix}} \
#	--with-ogg=%{_prefix}
%{__make}
#make check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc doc/html/*.html
%doc AUTHORS COPYING.FDL COPYING.GPL COPYING.LGPL COPYING.Xiph README
%{_bindir}/*
%{_libdir}/*.so.*
%doc %{_man1dir}/*

%files dev
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/
%{_datadir}/aclocal/*

#%files -n xmms-input-flac
#%defattr(-,root,root)
#%{_xmms_input_path}/*.so
#%{_xmms_input_path}/*.la

%changelog
