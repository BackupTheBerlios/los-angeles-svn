Summary:	Library of graphics routines used by libgnomecanvas
Name:		libart_lgpl
Version:	2.3.16
Release:	los1
License:	LGPL v2
Group:		X11/Libraries
Source0:	libart_lgpl-%{version}.tar.bz2
URL:		http://www.gnome.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Graphics routines used by the GnomeCanvas widget and some other
applications. libart renders vector paths and the like.

%package dev
Summary:	Headers for libart_lgpl
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
Header files for libart_lgpl.

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%install
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files dev
%defattr(644,root,root,755)
%{_bindir}/libart2-config
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
