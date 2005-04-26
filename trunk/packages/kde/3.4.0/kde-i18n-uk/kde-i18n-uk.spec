# $Id$
# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		KDE i18n Ukraine Language Pack
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		kde-i18n-uk
%define ver		3.4.0
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		KDE
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	noarch

%description
KDE i18n ukraine language pack.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_datadir}/

%changelog
* Sat Apr 23 2005 Igor Zubkov <icesik@mail.ru> 3.4.0-los1
- Initial build for Los Angeles GNU/Linux.
