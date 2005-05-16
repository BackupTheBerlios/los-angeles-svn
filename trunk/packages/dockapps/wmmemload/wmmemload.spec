# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		wmmemload
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		wmmemload
%define ver		0.1.6
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{ver}.tar.gz
License:	GPL v2
Group:		X
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
wmmemload

%prep
%setup -q

%build
export LDFLAGS="-Wl,-rpath,/usr/X11R6/lib"
%configure
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog THANKS
%{_bindir}/wmmemload
%{_man1dir}/*

%changelog
* Wed May 19 2004 Igor Zubkov <icesik@mail.ru> 0.1.6-los1
- Initial build for Los Angeles GNU/Linux.
