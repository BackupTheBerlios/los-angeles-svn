# TODO: --enable-video-directfb
#	--enable-video-vgl
#	--enable-video-aalib
#	--enable-video-svga
#	--enable-nas
#	remove -march=pentium chto-to-tam... ;-)

Summary:	Simple DirectMedia Layer
Name:		SDL
Version:	1.2.8
Release:	los1
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}.tar.gz.sig
URL:		http://www.libsdl.org/
Copyright:	LGPL
Group:		System Environment/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	nasm
BuildRequires:	alsa-lib-dev
BuildRequires:	alsa-lib
BuildRequires:	arts-dev
Requires:	arts
BuildRequires:	esound-dev
Requires:	esound
#BuildRequires:	nas
BuildRequires:	xorg-dev

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package dev
Summary:	Libraries, includes and more to develop SDL applications.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.

%prep
%setup -q 

%build
%configure \
	--disable-debug \
	--enable-audio \
	--enable-video \
	--enable-events \
	--enable-joystick \
	--enable-cdrom \
	--enable-threads \
	--enable-timers \
	--enable-endian \
	--enable-file \
	--enable-cpuinfo \
	--enable-oss \
	--enable-alsa \
	--enable-alsa-shared \
	--enable-esd \
	--enable-esd-shared \
	--enable-arts \
	--enable-arts-shared \
	--enable-diskaudio \
	--enable-mintaudio \
	--enable-nasm \
	--enable-video-x11 \
	--enable-video-x11-vm \
	--enable-dga \
	--enable-video-x11-dgamouse \
	--enable-video-x11-xv \
	--enable-video-x11-xinerama \
	--enable-video-x11-xme \
	--enable-video-dga \
	--enable-video-fbcon \
	--enable-video-ggi \
	--enable-video-dummy \
	--enable-video-opengl \
	--enable-sdl-dlopen
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%files
%defattr(-,root,root)
%doc README-SDL.txt COPYING CREDITS BUGS
%{_libdir}/*.so.*

%files dev
%defattr(-,root,root)
%doc README.* README WhatsNew docs.html
%doc docs/index.html docs/html
%{_bindir}/sdl-config
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/SDL/
%doc %{_man3dir}/*
%{_datadir}/aclocal/*

%changelog
