# TODO: --disable-broken-oss ???

Summary:	Cross Platform Audio Output Library
Name:		libao
Version:	0.8.5
Release:	los1
License:	GPL v2
Group:		Libraries
Source0:	libao-%{version}.tar.gz
URL:		http://www.xiph.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	alsa-lib-dev
BuildRequires:	arts-dev
#BuildRequires:	nas-dev
#Requires:	nas
BuildRequires:	esound-dev
Requires:	esound

%description
Libao is a cross-platform audio library that allows programs to output
audio using a simple API on a wide variety of platforms. It currently
supports: Null output, WAV files, OSS (Open Sound System), ESD (ESounD
or Enlighten Sound Daemon), ALSA (Advanced Linux Sound Architecture),
Solaris (untested), IRIX (untested)

%package dev
Summary:	Cross Platform Audio Output Library Development
Group:		Development/Libraries
Requires:	libao = %{version}-%{release}

%description dev
The libao-dev package contains the header files and documentation
needed to develop applications with libao.

%package arts
Summary:	Arts plugin for libao
Group:		Libraries
Requires:	libao = %{version}-%{release}
Requires:	arts

%description arts
Arts plugin for libao.

%package esd
Summary:	ESD plugin for libao
Group:		Libraries
Requires:	libao = %{version}-%{release}
Requires:	esound

%description esd
ESD plugin for libao.

%package alsa
Summary:	ALSA plugin for libao
Group:		Libraries
Requires:	libao = %{version}-%{release}

%description alsa
ALSA plugin for libao.

#%package nas
#Summary:	NAS plugin for libao
#Group:		Libraries
#Requires:	libao = %{version}-%{release}
#
#%description nas
#NAS plugin for libao.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-alsa09 \
	--enable-arts \
	--disable-nas \
	--enable-shared

%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES README TODO
%{_libdir}/libao.so.*
%{_libdir}/ao/plugins-2/liboss.so
%{_libdir}/ao/plugins-2/liboss.la
%doc %{_man5dir}/*

%files dev
%defattr(-,root,root)
%doc doc/*{html,css}
%{_libdir}/libao.so
%{_libdir}/libao.la
%{_includedir}/ao/
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/*

%files arts
%defattr(-,root,root)
%{_libdir}/ao/plugins-2/libarts.so
%{_libdir}/ao/plugins-2/libarts.la

%files esd
%defattr(-,root,root)
%{_libdir}/ao/plugins-2/libesd.so
%{_libdir}/ao/plugins-2/libesd.la

%files alsa
%defattr(-,root,root)
%{_libdir}/ao/plugins-2/libalsa09.so
%{_libdir}/ao/plugins-2/libalsa09.la

#%files nas
#%defattr(-,root,root)
#%{_libdir}/ao/plugins-2/libnas.so
#%{_libdir}/ao/plugins-2/libnas.la

%changelog
