Name: allin1
Summary: The all-in-one monitoring dockapplet
Version: 0.4.2
Release: los1
Source0: %{name}-%{version}.tar.bz2
Patch0: %{name}-%{version}-los-build.patch
URL: http://digilander.libero.it/tailchaser/en_linux_allin1.html
Group:  User Interface/Desktops
Copyright: GPL
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Allin1 is a monitoring dockapplet that displays RAM and SWAP space 
usage with colorful histogram, the CPU load with moving graph, 
power and battery status for notebooks, Ethernet and PPP traffic 
load and finally used space in up to three file systems. It was 
designed for FluxBox window manager, but is useful with any other 
window manager.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
%{__make} DEST_PATH=${RPM_BUILD_ROOT}%{_prefix} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc BUGS COPYING ChangeLog INSTALL README README.it TODO
%{_bindir}/allin1
%{_man1dir}/*
%{_datadir}/allin1/*

%changelog
