Summary:	A couple of command line utilities for working with desktop entries
Name:		desktop-file-utils
Version:	0.10
Release:	los1
License:	GPL v2
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.freedesktop.org/software/desktop-file-utils/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	glib-dev
BuildRequires:	pkgconfig
BuildRequires:	libpopt-dev

%description
desktop-file-utils contains a couple of command line utilities for
working with desktop entries.

%prep
%setup -q

%build
%configure
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*

%changelog
