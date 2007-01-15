Summary:	The Gimp Toolkit
Name:		gtk+
Version:	2.6.7
Release:	los1.1
License:	LGPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.gtk.org/pub/gtk/v2.6/gtk+-%{version}.tar.bz2
Source1:	ftp://ftp.gtk.org/pub/gtk/v2.6/gtk+-%{version}.tar.bz2.md5
URL:		http://www.gtk.org/
BuildRequires:	atk-dev
BuildRequires:	glib-dev
BuildRequires:	libjpeg-dev
BuildRequires:	libpng-dev
BuildRequires:	libtiff-dev
BuildRequires:	pango-dev
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GTK+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System System. It is
designed to be small, efficient, and flexible. GTK+ is written in C
with a very object-oriented approach. Gdk (part of GTK+) is a drawing
toolkit which provides a thin layer over Xlib to help automate things
like dealing with different color depths, and Gtk is a widget set for
creating user interfaces.

%package dev
Summary:	GTK+ header files and development documentation
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	atk-dev
Requires:	glib-dev
Requires:	pango-dev

%description dev
Header files and development documentation for the GTK+ libraries.

%prep
%setup -q

%build
export LDFLAGS="-Wl,-rpath,/usr/X11R6/lib"
%configure \
	--disable-static \
	--with-html-path=%{_docdir}/gtk-doc/html
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install \
	HTML_DIR=%{_docdir}/gtk-doc/html

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/gtk-2.0/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post
umask 022
/sbin/ldconfig
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS* README* INSTALL 
%{_sysconfdir}/gtk-2.0/
%{_bindir}/gdk-pixbuf-query-loaders
%{_bindir}/gtk-demo
%{_bindir}/gtk-query*
%{_bindir}/gtk-update-icon-cache
%{_libdir}/lib*.so.*
%{_libdir}/gtk-*/*/*/*.so
%{_datadir}/gtk-*
%{_datadir}/locale/
%{_datadir}/themes/

%files dev
%defattr(-,root,root)
%doc ChangeLog* HACKING
%{_bindir}/*csource
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/gtk-*/*/*/*.la
%{_includedir}/*
%{_datadir}/aclocal/*.m4
%{_libdir}/gtk-*/include
%{_libdir}/pkgconfig/*.pc
%{_man1dir}/*
%doc %{_docdir}/gtk-doc/html/*

%changelog
* Wed Apr 27 2005 Igor Zubkov <icesik@mail.ru> 2.6.7-los1
- Initial build for Los Angeles GNU/Linux.
