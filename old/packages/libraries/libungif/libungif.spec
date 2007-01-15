# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		GIF-manipulation library.
%define sum_ru		Библиотека для работы с GIF-файлами.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		libungif
%define ver		4.1.3
%define rel		los1
%define url		http://sf.net/projects/libungif/

Summary:	%{sum}
Summary(ru_RU.KOI8-R):	%{sum_ru}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	MIT
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-%{version}.tar.bz2.sign
URL:		http://www.kernel.org/pub/linux/libs/pam/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GIF loading and saving shared library. (Saving uses an uncompressed
GIF algorithm that does not use LZW compression.)

%description -l ru_RU.KOI8-R
Библиотека для загрузки и сохранения GIF-файлов. (Сохранение
использует некомпрессированный GIF-алгоритм, не использующий
компрессию LZW).

%package dev
Summary:	GIF-manipulation library header files and documentation.
Summary(ru):	Хедеры, библиотеки и документация GIF-библиотеки.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
Libraries and headers needed for developing programs that use libungif
to load and save GIF image files.

%description dev -l ru_RU.KOI8-R
Хедеры и библиотеки, необходимые для разработки программ, использующих
libungif для загрузки и сохранения изображений в формате GIF.

%package progs
Summary:	Programs for converting and transforming GIF images.
Summary(ru):	Программы для конвертирования и обработки GIF-файлов.
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
This package contains various programs for manipulating GIF image
files.

%description progs -l ru_RU.KOI8-R
Этот пакет содержит различные программы для обработки GIF-файлов.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO UNCOMPRESSED_GIF
%{_libdir}/lib*.so.*

%files dev
%defattr(-,root,root)
%doc doc/*.{txt,png} doc/{gif_lib,index,liberror}.html
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/*.h

%files progs
%defattr(-,root,root)
%doc doc/gif2* doc/gif[a-z]* doc/*2gif*
%{_bindir}/*

%changelog
* Mon Mar 21 2005 Igor Zubkov <icesik@mail.ru> 4.1.3-los1
- Initial build for Los Angeles GNU/Linux.
