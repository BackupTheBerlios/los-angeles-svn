Summary:	Little CMS - a library to transform between colour profiles
Summary(ru):	Little cms - система управления цветом
Name:		lcms
Version:	1.14
Release:	los1
License:	MIT
Group:		Libraries
Source0:	http://prdownloads.sf.net/lcms/lcms-%{version}.tar.gz
#Source1:	http://www.littlecms.com/profiles.zip
URL:		http://www.littlecms.com/
BuildRequires:	libjpeg-dev
BuildRequires:	libtiff-dev
BuildRequires:	libz-dev
Requires:	liblcms = %{version}-%{release}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Little CMS is a color management library. Implements fast transforms
between ICC profiles.

This package contains Little CMS tools.

%description -l ru
Little cms - библиотека системы управления цветом. Реализует быстрые
преобразования между профилями ICC.

%package -n liblcms
Summary:	Little CMS library - library to transform between colour profiles
Summary(ru):	Little cms - система управления цветом
Group:		Libraries

%description -n liblcms
Little CMS library.

%description -n liblcms -l ru
Little cms - библиотека системы управления цветом. Реализует быстрые
преобразования между профилями ICC.

%package -n liblcms-dev
Summary:	Little CMS - header files and developer's documentation
Summary(ru):	Файлы для разработки с LCMS
Group:		Development/Libraries
Requires:	liblcms = %{version}-%{release}

%description -n liblcms-dev
Header files needed to compile programs with liblcms and some
documentation useful for programmers.

%description -n liblcms-dev -l ru
Этот пакет необходим только для разработки и компиляции программ,
использующих библиотеку LCMS.

%prep
%setup  -q

%build
%configure
%{__make} %{_smp_mflags}

%install
#mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/lcms/

%{__make} DESTDIR=${RPM_BUILD_ROOT} install

#unzip %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/lcms

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post   -n liblcms -p /sbin/ldconfig
%postun -n liblcms -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_man1dir}/*

%files -n liblcms
%defattr(-,root,root)
%doc AUTHORS NEWS README*
%{_libdir}/lib*.so.*
#%{_datadir}/lcms

%files -n liblcms-dev
%defattr(-,root,root)
%doc doc/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
