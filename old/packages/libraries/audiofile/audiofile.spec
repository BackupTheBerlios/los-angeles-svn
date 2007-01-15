Summary: A library to handle various audio file formats.
Name: audiofile
Version: 0.2.6
Release: los1
Copyright: LGPL
Group: Libraries/Sound
Source: %{name}-%{version}.tar.gz
URL: http://www.68k.org/~michael/audiofile/
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
The Audio File Library provides an elegant API for accessing a variety
of audio file formats, such as AIFF/AIFF-C, WAVE, and NeXT/Sun
.snd/.au, in a manner independent of file and data formats.

%package dev
Summary: Library, headers, etc. to develop with the Audio File Library.
Group: Libraries

%description dev
Library, header files, etc. for developing applications with the Audio
File Library.

%prep
%setup -q

%build
%configure
%{__make}
%{__make} check

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%files
%defattr(-, root, root)
%doc ACKNOWLEDGEMENTS AUTHORS COPYING COPYING.GPL ChangeLog NEWS NOTES README
%{_bindir}/*
%{_libdir}/*.so.*

%files dev
%defattr(-, root, root)
%doc TODO
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/aclocal/*

%changelog
