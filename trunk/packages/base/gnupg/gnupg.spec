# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU Privacy Guard.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		gnupg
%define ver		1.2.5
%define rel		los1
%define url		http://www.gnupg.org/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Security
Source0:	ftp://ftp.gnupg.org/GnuPG/%{name}/%{name}-%{ver}.tar.bz2
Source1:	pgp2gnupg.html
Patch0:		gnupg-1.2.5-los1.patch.bz2
Patch1:		gnupg-1.2.5-los2.patch
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
GnuPG is GNU's tool for secure communication and data storage.
It can be used to encrypt data and to create digital signatures.
It includes an advanced key management facility and is compliant
with the proposed OpenPGP Internet standard as described in RFC2440.

Because GnuPG does not use use any patented algorithm it cannot be
compatible with PGP2 versions.  PGP 2.x uses IDEA (which is patented
worldwide).

The default algorithms are DSA and ElGamal, but RSA is also
supported.  ElGamal for signing is available, but because of the
larger size of such signatures it is deprecated (Please note that
the GnuPG implementation of ElGamal signatures is *not* insecure).
Symmetric algorithms are: AES, 3DES, Blowfish, CAST5 and Twofish.
Digest algorithms available are MD5, RIPEMD160 and SHA1.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

install -p -m644 %{SOURCE1} doc

%build
%configure
%{__make} %{_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS NEWS PROJECTS README THANKS TODO
%doc doc/{DETAILS,FAQ,HACKING,OpenPGP,*.html,samplekeys.asc}
%doc tools/convert-from-106
%{_bindir}/*
%doc %{_infodir}/*
%doc %{_man1dir}/*
%doc %{_man7dir}/*
%{_datadir}/gnupg/

%changelog
* Thu Dec 16 2004 Igor Zubkov <icesik@mail.ru> 1.2.5-los1
- Initial build for Los Angeles GNU/Linux.
