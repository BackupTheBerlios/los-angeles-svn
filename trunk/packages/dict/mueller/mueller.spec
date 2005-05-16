Summary:	Mueller Dictionary (7 Edition).
Name:		mueller
Version:	7
Release:	los1
License:	GPL
Group:		Dicts
Source0:	Mueller7GPL.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildArch:	noarch

%description

%prep
%setup -q -n usr

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/dict/
mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}/
cd local/share/dict/
cp * ${RPM_BUILD_ROOT}%{_datadir}/dict/
cd ../mova/
cp * ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}/

%clean

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}-%{version}/
%{_datadir}/dict/*

%changelog
