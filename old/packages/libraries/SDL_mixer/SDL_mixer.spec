Summary: Simple DirectMedia Layer - Sample Mixer Library
Name: SDL_mixer
Version: 1.2.6
Release: los1
Source0: %{name}-%{version}.tar.gz
Copyright: LGPL
Group: System Environment/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	smpeg-dev

%description
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%package dev
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description dev
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%prep
%setup -q

%build
export LDFLAGS="-Wl,-rpath,/usr/X11R6/lib"
%configure
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
%{_includedir}/SDL/SDL_mixer.h

%changelog
