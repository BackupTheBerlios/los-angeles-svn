Summary:	A library of functions for manipulating MNG format files
Summary(ru):	Библиотека функций для работы с файлами в формате MNG
Name:		libmng
Version:	1.0.8
Release:	los1
License:	BSD-like
Group:		Libraries
Source0:	http://prdownloads.sf.net/libmng/libmng-%{version}.tar.gz
Patch0:		libmng-1.0.8-los-autotools.patch.bz2
URL:		http://www.libmng.com/
BuildRequires:	libjpeg-dev
BuildRequires:	liblcms-dev
BuildRequires:	libz-dev
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
libmng - library for reading, writing, displaying and examing
Multiple-Image Network Graphics. MNG is the animation extension to the
popular PNG image-format.

%description -l ru
libmng - библиотека для чтения, записи, отображения и изучения
Multiple-Image Network Graphics. MNG - это анимационное расширение для
популярного формата изображений PNG.

%package dev
Summary:	Development tools for programs to manipulate MNG format files
Summary(ru):	Средства разработки для программ, работающих с файлами в формате MNG
Group:		Development/Libraries
Requires:	libjpeg-dev
Requires:	liblcms-dev
Requires:	%{name} = %{version}-%{release}
Requires:	libz-dev

%description dev
The libmng-devel package contains the header files necessary for
developing programs using the MNG (Multiple-Image Network Graphics)
library.

If you want to develop programs which will manipulate MNG image format
files, you should install libmng-devel. You'll also need to install
the libmng package.

%description dev -l ru
Пакет libmng-devel содержит хедеры и библиотеки разработчика,
необходимые для разработки программ, использующих библиотеку MNG
(Multiple-Image Network Graphics).

%prep
%setup -q
%patch0 -p1

chmod +x configure

%build
%configure \
	--enable-static \
	--enable-shared \
	--with-zlib \
	--with-jpeg
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

mkdir -p ${RPM_BUILD_ROOT}%{_man3dir}/
mkdir -p ${RPM_BUILD_ROOT}%{_man5dir}/

install doc/man/*3 ${RPM_BUILD_ROOT}%{_man3dir}/
install doc/man/*5 ${RPM_BUILD_ROOT}%{_man5dir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/lib*.so.*
%{_man5dir}/*

%files dev
%defattr(-,root,root)
%doc CHANGES README* doc/{doc.readme,libmng.txt}
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_man3dir}/*

%changelog
