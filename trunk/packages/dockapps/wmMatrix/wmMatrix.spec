# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		wmMatrix
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		wmMatrix
%define ver		0.2
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{ver}.tar.gz
Patch0:		wmMatrix-0.2-los-build.patch
License:	GPL v2
Group:		X
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
wmmemload

%prep
%setup -q
%patch0 -p1

%build
%{__make} clean
%{__make} %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
install -c -s -m 0755 wmMatrix ${RPM_BUILD_ROOT}%{_bindir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%{_bindir}/wmMatrix

%changelog
* Wed May 19 2004 Igor Zubkov <icesik@mail.ru> 0.2-los1
- Initial build for Los Angeles GNU/Linux.
