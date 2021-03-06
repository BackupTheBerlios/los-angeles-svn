Summary:	Useful routines for 'C' programming
Name:		glib
Version:	2.4.8
Release:	los1
License:	LGPL v2
Group:		Libraries
Source0:	glib-%{version}.tar.bz2
URL:		http://www.gtk.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLIB
includes also generally useful data structures used by GIMP and many
other.

%package dev
Summary:	Glib heades files, documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dev
Header files for the support library for the GIMP's X libraries, which
are available as public libraries. GLIB includes generally useful data
structures.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-html-path=%{_docdir}/gtk-doc/html

%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install \
	HTML_DIR=%{_defaultdocdir}/gtk-doc/html

%find_lang glib20

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f glib20.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS ChangeLog
%{_libdir}/lib*.so.*

%files dev
%defattr(644,root,root,755)
%{_bindir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_libdir}/glib-2.0/
%{_libdir}/pkgconfig/*
%{_datadir}/glib-2.0/
%{_datadir}/aclocal/*
%doc %{_man1dir}/*
%doc %{_docdir}/gtk-doc/

%changelog
