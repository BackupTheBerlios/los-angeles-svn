Summary: Simple DirectMedia Layer - Sample Image Loading Library
Name: SDL_image
Version: 1.2.4
Release: los1
Source0: %{name}-%{version}.tar.gz
Copyright: LGPL v2
Group: System Environment/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	SDL-dev
BuildRequires:	libjpeg-dev
BuildRequires:	libpng-dev
BuildRequires:	libtiff-dev
BuildRequires:	libz-dev

%description
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PPM, PCX, GIF, JPEG, PNG, and TIFF formats.

%package dev
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: SDL-dev

%description dev
This is a simple library to load images of various formats as SDL surfaces.
This library supports BMP, PPM, PCX, GIF, JPEG, PNG, and TIFF formats.

%prep
%setup -q

%build
export LDFLAGS="-Wl,-rpath,/usr/X11R6/lib"
%configure \
	--enable-tif \
	--enable-xcf
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{_libdir}/*.so.*

%files dev
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/SDL/

%changelog
