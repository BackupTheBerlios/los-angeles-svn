Summary:	The RAR Archiver
Name:		rar
Version:	3.2.0
Release:	los1
License:	Shareware
Group:		Applications/Archiving
Source0:	%{name}linux-%{version}.tar.gz
URL:		http://www.rarlab.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
RAR is a powerful tool which allows you to manage and control archive
files. The archive is usually a regular file, which name has a ".rar"
suffix.

%prep
%setup -q -n rar

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/rar/

#install *.sfx ${RPM_BUILD_ROOT}%{_libdir}/rar/
cp *.lst ${RPM_BUILD_ROOT}%{_libdir}/rar/
cp rar_static ${RPM_BUILD_ROOT}%{_bindir}/rar

%clean

%files
%defattr(-,root,root)
%doc *.{txt,diz}
%{_bindir}/rar
%{_libdir}/rar

%changelog
