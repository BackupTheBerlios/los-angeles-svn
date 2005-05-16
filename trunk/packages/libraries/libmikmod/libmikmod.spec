Summary:	libmikmod - a portable sound library for Unix
Name:		libmikmod
Version:	3.1.11
Release:	los1
License:	LGPL v2
Group:		Libraries
Source0:	http://mikmod.raphnet.net/files/libmikmod-%{version}.tar.gz
URL:		http://mikmod.raphnet.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	esound-dev
BuildRequires:	audiofile-dev
BuildRequires:	alsa-lib-dev

%description
Libmikmod is a portable sound library, capable of playing samples as
well as module files, originally written by Jean-Paul Mikkers (MikMak)
for DOS. It has subsequently been hacked by many hands and now runs on
many Unix flavours.

It uses the OSS /dev/dsp driver including in all recent kernels for
output, as well as ALSA and EsounD, and will also write WAV files.

Supported file formats include mod, stm, s3m, mtm, xm, and it. Full
source included, use of this library for music/sound effects in your
own programs is encouraged !

%package dev
Summary:	Libraries and include files to develop libmikmod applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
Libraries and include files to develop libmikmod applications.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-alsa \
	--enable-esd \
	--enable-oss
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%clean

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post dev
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun dev
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(-,root,root)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files dev
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/libmikmod-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%doc %{_man1dir}/*
%doc %{_infodir}/*
%{_includedir}/mikmod.h
%{_datadir}/aclocal/libmikmod.m4

%changelog
