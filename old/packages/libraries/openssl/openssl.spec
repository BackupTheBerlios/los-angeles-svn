# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Secure Sockets Layer and cryptography libraries and tools.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		openssl
%define ver		0.9.7
%define rel		los1.e
%define url		http://www.openssl.org/

%define openssldir	/var/ssl

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	Freely distributable
Group:		System/Libraries
Source0:	ftp://ftp.openssl.org/source/%{name}-%{version}e.tar.gz
Source1:	%{name}-%{ver}e.tar.gz.asc
Source2:	%{name}-%{ver}e.tar.gz.md5
Url:		%{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
protocols as well as a full-strength general purpose cryptography library.
The project is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL tookit and its related
documentation. 

OpenSSL is based on the excellent SSLeay library developed from Eric A.
Young and Tim J. Hudson.  The OpenSSL toolkit is licensed under an
Apache-style licence, which basically means that you are free to get and
use it for commercial and non-commercial purposes. 

This package contains the base OpenSSL cryptography and SSL/TLS 
libraries and tools.

%package dev
Summary: Secure Sockets Layer and cryptography static libraries and headers
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description dev
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
protocols as well as a full-strength general purpose cryptography library.
The project is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL tookit and its related
documentation. 

OpenSSL is based on the excellent SSLeay library developed from Eric A.
Young and Tim J. Hudson.  The OpenSSL toolkit is licensed under an
Apache-style licence, which basically means that you are free to get and
use it for commercial and non-commercial purposes. 

This package contains the the OpenSSL cryptography and SSL/TLS 
static libraries and header files required when developing applications.

%package doc
Summary: OpenSSL miscellaneous files
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
protocols as well as a full-strength general purpose cryptography library.
The project is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL tookit and its related
documentation. 

OpenSSL is based on the excellent SSLeay library developed from Eric A.
Young and Tim J. Hudson.  The OpenSSL toolkit is licensed under an
Apache-style licence, which basically means that you are free to get and
use it for commercial and non-commercial purposes. 

This package contains the the OpenSSL cryptography and SSL/TLS extra
documentation and POD files from which the man pages were produced.

%prep
%setup -q -n openssl-0.9.7e

%build 

%define CONFIG_FLAGS -DSSL_ALLOW_ADH --prefix=/usr --openssldir=%{openssldir}

perl util/perlpath.pl /usr/bin/perl

%ifarch i386 i486 i586 i686
./Configure %{CONFIG_FLAGS} linux-elf shared
%else
echo "Target unsupported!"
exit -1
%endif
LD_LIBRARY_PATH=`pwd` make
LD_LIBRARY_PATH=`pwd` make rehash
LD_LIBRARY_PATH=`pwd` make test

%install
make MANDIR=%{_mandir} MANSUFFIX=ssl INSTALL_PREFIX=${RPM_BUILD_ROOT} install

# Make backwards-compatibility symlink to ssleay
ln -sf /usr/bin/openssl ${RPM_BUILD_ROOT}/usr/bin/ssleay

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}e

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%defattr(0644,root,root,0755)
%doc CHANGES CHANGES.SSLeay LICENSE NEWS README
%attr(0755,root,root) /usr/bin/*
%attr(0755,root,root) /usr/lib/*.so*
%attr(0755,root,root) %{openssldir}/misc/*
%attr(0644,root,root) %{_mandir}/man[157]/*
%config %attr(0644,root,root) %{openssldir}/openssl.cnf 
%dir %attr(0755,root,root) %{openssldir}/certs
#%dir %attr(0755,root,root) %{openssldir}/lib
%dir %attr(0755,root,root) %{openssldir}/misc
%dir %attr(0750,root,root) %{openssldir}/private

%files dev
%defattr(0644,root,root,0755)
%doc CHANGES CHANGES.SSLeay LICENSE NEWS README
%attr(0644,root,root) /usr/lib/*.a
%attr(0644,root,root) /usr/lib/pkgconfig/openssl.pc
%attr(0644,root,root) /usr/include/openssl/*
%doc %{_man3dir}/*

%files doc
%defattr(0644,root,root,0755)
%doc CHANGES CHANGES.SSLeay LICENSE NEWS README
%doc doc

%changelog
* Thu Feb 10 2005 Igor Zubkov <icesik@mail.ru> 0.9.7-los1.e
- Initial build for Los Angeles GNU/Linux.
