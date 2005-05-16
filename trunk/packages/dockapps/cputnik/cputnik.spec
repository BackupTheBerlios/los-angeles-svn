# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		cputnik
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		cputnik
%define ver		0.1.0
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{ver}.tar.gz
Patch0:		cputnik-0.1.0-los-build.patch
License:	GPL v2
Group:		X
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
cputnik

%prep
%setup -q
%patch0 -p1

%build
%{__make} %{_smp_mflags} CC=%{__cc}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
cp cputnik ${RPM_BUILD_ROOT}%{_bindir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/cputnik

%changelog
* Wed May 19 2004 Igor Zubkov <icesik@mail.ru> 0.1.0-los1
- Initial build for Los Angeles GNU/Linux.
