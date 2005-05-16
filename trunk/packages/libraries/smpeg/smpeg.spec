Summary:	smpeg
Name:		smpeg
Version:	20050502
Release:	los1
Source0:	%{name}-cvs.tar.bz2
Copyright:	LGPL v2
Group:		System Environment/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
smpeg

%package dev
Summary: smpeg dev
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description dev
smpeg dev.

%prep
%setup -q -n %{name}

%build
export LDFLAGS="-Wl,-rpath,/usr/X11R6/lib"
%configure
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%files
%defattr(-,root,root)
%doc BUGS CHANGES COPYING README README.SDL_mixer TODO
%{_bindir}/glmovie
%{_bindir}/plaympeg
%{_libdir}/*.so.*
%doc %{_man1dir}/*

%files dev
%defattr(-,root,root)
%{_bindir}/smpeg-config
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/smpeg/
%{_datadir}/aclocal/smpeg.m4

%changelog
