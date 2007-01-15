Summary:	ATK - Accessibility Toolkit
Name:		atk
Version:	1.8.0
Release:	los1
License:	LGPL v2
Group:		X11/Libraries
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	glib-dev
#BuildRequires:	gtk-doc		>= 1.0
#BuildRequires:	pkgconfig
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
as tools such as screen readers and magnifiers, and alternative input
devices.

%package dev
Summary:	ATK - header and development documentation
Group:		X11/Development/Libraries
Requires:	%{name}	= %{version}-%{release}
Requires:	glib-dev

%description dev
ATK - header and development documentation.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-shared \
	--with-html-dir=%{_docdir}/gtk-doc/html
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%find_lang atk10

%clean

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f atk10.lang
%defattr(644,root,root,755)
%{_libdir}/lib*.so.*

%files dev
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/atk*
%{_libdir}/pkgconfig/*
%doc %{_docdir}/gtk-doc/html/atk

%changelog
