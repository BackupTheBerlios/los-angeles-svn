%define sum		Startup programs.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		sysvinit
%define ver		2.85
%define rel		los5

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}.lsm
Patch0:		sysvinit-2.85-los1.patch
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The Sysvinit package contains programs to control the startup, running
and shutdown of all other programs.

%prep
%setup -q
%patch0 -p1

%build
cp src/init.c{,.backup}
sed 's/Sending processes/Sending processes started by init/g' \
	src/init.c.backup > src/init.c

%{__make} -C src %{_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}/sbin/
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,2,3,4,5,6,7,8}/
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/

%{__make} -C src ROOT=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README COPYRIGHT doc
/sbin/*
%{_bindir}/*
%{_includedir}/*
%doc %{_mandir}/man[158]/*

%changelog
* Fri Jan 28 2005 Igor Zubkov <icesik@mail.ru> 2.85-los5
- move file /etc/inittab to base-scripts.

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 2.85-los4
- s/packager/maintainer.
- remove Vendor field.
- change Group to System/Base.
- add russian group description.

* Tue Dec 14 2004 Igor Zubkov <icesik@mail.ru> 2.85-los3
- clean up.

* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 2.85-los1
- update to 2.85

* Wed May 19 2004 Igor Zubkov <icesik@mail.ru> 2.84-los1
- Initial build for Los Angeles GNU/Linux.
