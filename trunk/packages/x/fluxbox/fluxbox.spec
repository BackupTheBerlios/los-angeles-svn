%define sum		fluxbox
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		fluxbox
%define ver		0.9.12
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		WM
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	task-c++-devel

%description

%prep
%setup -q

%build
%configure \
	--enable-nls \
	--enable-xinerama
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc doc/Coding_style data/README.menu data/README.style
%{_bindir}/*
%{_datadir}/fluxbox/
%doc %{_man1dir}/*

%changelog
* Thu Apr 07 2005 Igor Zubkov <icesik@mail.ru> 0.9.12-los1
- Initial build for Los Angeles GNU/Linux.
