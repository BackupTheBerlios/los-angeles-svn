Summary:	An open-source, patent-free speech codec
Name:		speex
Version:	1.0.4
Release:	los1
Copyright:	BSD
Group:		Application/Devel
Source:		http://www.speex.org/download/%{name}-%{version}.tar.gz
URL:		http://www.speex.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package dev
Summary:	Speex development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
Speex development files.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--enable-static
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING AUTHORS ChangeLog NEWS README
%doc doc/manual.pdf
%{_bindir}/*
%{_libdir}/*.so*
%{_man1dir}/*

%files dev
%defattr(-,root,root)
%{_libdir}/*.la
%{_includedir}/speex*.h
%{_includedir}/speex/speex*.h
%{_datadir}/aclocal/speex.m4
%{_libdir}/pkgconfig/speex.pc
%{_libdir}/*.a

%changelog
