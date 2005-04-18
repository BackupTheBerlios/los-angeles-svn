Summary:	System for layout and rendering of internationalized text
Name:		pango
Version:	1.6.0
Release:	los1
License:	LGPL v2
Group:		X11/Libraries
Source0:	pango-%{version}.tar.bz2
URL:		http://www.pango.org/
#BuildRequires:	XFree86-devel
#BuildRequires:	docbook-dtd412-xml
#BuildRequires:	freetype-devel	>= %{req_ver_freetype}
BuildRequires:	glib-dev
#BuildRequires:	gtk-doc		>= 0.9-4
#BuildRequires:	pkgconfig
#BuildRequires:	xft-devel	>= 2.1.2
#Requires:	freetype	>= 2.1.7
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
System for layout and rendering of internationalized text.

%package dev
Summary:	System for layout and rendering of internationalized text
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Requires:	XFree86-devel
#Requires:	xft-devel
#Requires:	freetype-devel	>= %{req_ver_freetype}
Requires:	glib-dev

%description dev
Developer files for pango.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-fribidi \
	--with-html-dir=%{_docdir}/gtk-doc/html
%{__make}

%install
%{__make} DESTDIR=$RPM_BUILD_ROOT install \
	HTML_DIR=%{_docdir}/gtk-doc/html

%clean

%post
/sbin/ldconfig
umask 022
%{_bindir}/pango-querymodules > %{_sysconfdir}/pango/pango.modules

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README examples/HELLO.utf8
%dir %{_sysconfdir}/pango
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pango/pangox.aliases
#%ghost %{_sysconfdir}/pango/pango.modules
%{_bindir}/pango-querymodules
%{_libdir}/lib*.so.*
%dir %{_libdir}/pango
%dir %{_libdir}/pango/*
%dir %{_libdir}/pango/*/modules
%attr(755,root,root) %{_libdir}/pango/*/modules/*.so
%{_libdir}/pango/*/modules/*.la
%doc %{_man1dir}/*

%files dev
%defattr(644,root,root,755)
%doc ChangeLog TODO
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*
%doc %{_docdir}/gtk-doc/html/pango

%changelog
