Summary:	XSLT processor
Summary(pl):	Procesor XSLT
Summary(pt_BR):	Biblioteca que disponibiliza o sistema XSLT do Gnome
Name:		libxslt
Version:	1.1.12
Release:	4
License:	MIT
Group:		Libraries
Source0:	libxslt-%{version}.tar.bz2
URL:		http://xmlsoft.org/XSLT/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libxml2-dev
Requires:	libxml2

%description
Library for XSLT processing.

%package dev
Summary:	Header files for libxslt
Group:		Development/Libraries
Requires:	%{name}	= %{version}-%{release}

%description dev
Header files for libxslt - XSLT processor.

%package progs
Summary:	XSLT processor
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description progs
XSLT processor.

%prep
%setup -q

%build
%configure \
	--disable-static
#	--with-crypto
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Copyright FEATURES NEWS README TODO
%{_libdir}/*.so.*

%files dev
%defattr(644,root,root,755)
%doc doc/{*.{gif,html},html}
%{_bindir}/xslt-config
%{_libdir}/*.so
%{_libdir}/lib*.la
%{_libdir}/*.sh
%{_includedir}/libxslt
%{_includedir}/libexslt
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_man3dir}/*

%files progs
%defattr(644,root,root,755)
%{_bindir}/xsltproc
%{_man1dir}/*

%changelog
