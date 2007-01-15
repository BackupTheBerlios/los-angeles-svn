Summary:	libXML library
Name:		libxml2
Version:	2.6.17
Release:	los1
License:	MIT
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libxml2/2.6/libxml2-%{version}.tar.bz2
URL:		http://xmlsoft.org/
BuildRequires:	libreadline5-dev
BuildRequires:	libz-dev
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%define _examplesdir	/usr/src/examples/

%description
This library allows you to manipulate XML files.

%package dev
Summary:	Header files etc to develop libxml2 applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libz-dev

%description dev
Header files etc you can use to develop libxml2 applications.

%package progs
Summary:	XML files parser
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}

%description progs
XML files parser.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-iso8859x=no
%{__make}

%install
mkdir -p $RPM_BUILD_ROOT%{_examplesdir}/%{name}-devel-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	EXAMPLE_DIR=%{_examplesdir}/python-%{name}-%{version}

# install catalog file
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xml
LD_LIBRARY_PATH=.libs ./xmlcatalog --create \
	> $RPM_BUILD_ROOT%{_sysconfdir}/xml/catalog

mv -f $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-%{version}/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-devel-%{version}
mkdir -p html
mv -f $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-%{version}/html/html/* html 
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-%{version}

%clean

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_libdir}/lib*.so.*
%{_mandir}/man3/*

%dir %{_sysconfdir}/xml
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xml/catalog

%files dev
%defattr(644,root,root,755)
%doc html
%doc AUTHORS ChangeLog NEWS README TODO
%{_examplesdir}/%{name}-devel-%{version}
%{_bindir}/xml2-config
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/xml2Conf.sh
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*.m4
%{_includedir}/libxml2
%{_man1dir}/xml2-config.*

%files progs
%defattr(644,root,root,755)
%{_bindir}/xmlcatalog
%{_bindir}/xmllint
%{_man1dir}/xmlcatalog.*
%{_man1dir}/xmllint.*

%changelog
