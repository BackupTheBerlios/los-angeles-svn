Summary: Advanced Linux Sound Architecture (ALSA) - Library
Name: alsa-lib
Version: 1.0.8
Release: los1
License: LGPL
Group: System/Libraries
Source: ftp://ftp.alsa-project.org/pub/lib/alsa-lib-%{version}.tar.bz2
URL: http://www.alsa-project.org
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Advanced Linux Sound Architecture (ALSA) - Library

%package dev
Summary: ALSA Libraries Development Files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description dev
Development files for building applications which use the ALSA libraries.

%prep
%setup -q

%build
%configure
%{__make}

%install
%makeinstall

%files
%defattr(-, root, root)
%doc doc/*.txt
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/alsa

%files dev
%defattr(-,root,root)
%{_includedir}/alsa
%{_includedir}/sys/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/*

%changelog
