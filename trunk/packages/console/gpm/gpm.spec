%define sum		gpm is general purpose mouse daemon.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		gpm
%define ver		1.20.1
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	libncurses-dev
Requires:	libncurses

%description
The gpm (general purpose mouse) daemon tries to be a useful mouse
server for applications running on the Linux console.  Its roots are
in the "selection" package, by Andrew Haylett, and the original code
comes from selection itself. This package is intended as a replacement
for "selection", to provide additional facilities.  From 0.18 onward
gpm supports xterm as well, so you can run mouse-sensitive
applications under X, and you can easily write curses applications
which support the mouse on both the Linux console and xterm. The xterm
code is portable to any U*x flavour (look at sample/README).

%package dev
Summary: Development files for gpm.
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description dev
Development files for gpm.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}

%install
%makeinstall

cd ${RPM_BUILD_ROOT}%{_libdir}/
chmod +x *.so.*

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc BUGS COPYING Changelog Changes MANIFEST README TODO
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*.so.*
%doc %{_infodir}/*
%doc %{_man1dir}/*
%doc %{_man7dir}/*
%doc %{_man8dir}/*

%files dev
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Thu Apr 07 2005 Igor Zubkov <icesik@mail.ru> 1.20.1-los1
- Initial build for Los Angeles GNU/Linux.
