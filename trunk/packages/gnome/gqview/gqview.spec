Summary:	graphics file browser utility
Name:		gqview
Version:	2.0.0
Release:	los1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://prdownloads.sourceforge.net/gqview/gqview-%{version}.tar.gz
URL:		http://gqview.sf.net/
BuildRequires:	gtk+-dev
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GQview is a browser for graphics files.
Offering single click viewing of your graphics files.
Includes thumbnail view, zoom and filtering features.
And external editor support.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_docdir}/
%{_bindir}/*
%{_datadir}/applications/gqview.desktop
%{_datadir}/pixmaps/gqview.png
%doc %{_man1dir}/*

%changelog
* Wed Apr 27 2005 Igor Zubkov <icesik@mail.ru> 2.0.0-los1
- Initial build for Los Angeles GNU/Linux.
