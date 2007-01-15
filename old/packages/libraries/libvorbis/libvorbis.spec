Summary:	The Vorbis General Audio Compression Codec
Name:		libvorbis
Version:	1.1.0
Release:	los1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.gz
BuildRequires:	libogg-dev
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

%package dev
Summary:	Development files for OGG Vorbis library
Group:		Development/Libraries
Requires:	%{name}		= %{version}-%{release}
Requires:	libogg-dev

%description dev
The libvorbis-dev package contains the header files and
documentation needed to develop applications with libvorbis.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-shared
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files dev
%defattr(644,root,root,755)
%doc todo.txt
%doc doc/*.html
%doc doc/*.png
%doc doc/*.txt
%doc doc/vorbisfile
%doc doc/vorbisenc
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/vorbis/
%{_libdir}/pkgconfig/
%{_datadir}/aclocal/

%changelog
