# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Network exploration tool and security scanner.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		nmap
%define ver		3.81
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Security
Source0:	http://www.insecure.org/nmap/dist/%{name}-%{version}.tgz
URL:		http://www.insecure.org/nmap/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Nmap is a utility for network exploration or security auditing. It
supports ping scanning (determine which hosts are up), many port
scanning techniques, version detection (determine service protocols
and application versions listening behind ports), and TCP/IP
fingerprinting (remote host OS or device identification). Nmap also
offers flexible target and port specification, decoy/stealth scanning,
sunRPC scanning, and more. Most Unix and Windows platforms are
supported in both GUI and commandline modes. Several popular handheld
devices are also supported, including the Sharp Zaurus and the iPAQ.

%if 0
%package frontend
Summary: Gtk+ frontend for nmap.
Group: Security
Requires: %{name} = %{version}-%{release}
Requires: gtk+
BuildRequires: gtk+-dev

%description frontend
This package includes nmapfe, a Gtk+ frontend for nmap. The nmap package must
be installed before installing nmap-frontend.
%endif

%prep
%setup -q

%build
%configure --without-openssl
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING COPYING.OpenSSL HACKING
%doc docs/README docs/nmap-fingerprinting-article.txt
%doc docs/nmap.deprecated.txt docs/nmap.usage.txt docs/nmap_doc.html
%doc docs/nmap_manpage.html docs/nmap_manpage-es.html
%doc docs/nmap_manpage-fr.html docs/nmap_manpage-lt.html 
%doc docs/nmap_manpage-it.html
%doc docs/nmap_manpage-ru.html
%{_bindir}/nmap
%{_datadir}/nmap/
%doc %{_man1dir}/nmap.*

%if 0
%files frontend
%defattr(-,root,root)
%{_bindir}/nmapfe
%{_bindir}/xnmap
%{_datadir}/applications/nmapfe.desktop
%doc %{_man1dir}/xnmap.*
%doc %{_man1dir}/nmapfe.*
%endif

%changelog
* Tue Feb 08 2005 Igor Zubkov <icesik@mail.ru> 3.81-los1
- Initial build for Los Angeles GNU/Linux.
