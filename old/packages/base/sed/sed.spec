# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The Stream Editor ... Or Search and Edit.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		sed
%define ver		4.1.4
%define rel		los2

%define _exec_prefix	/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Group(ru_RU.KOI8-R):	Система/База
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
sed  is a stream editor. A stream editor is used to perform basic text
transformations on an input stream (a file or input from a pipeline).

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_datadir}/doc/sed.html

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING COPYING.DOC ChangeLog NEWS README README.boot
%doc README-alpha THANKS
%{_bindir}/sed
%doc %{_infodir}/*
%doc %{_man1dir}/*

%changelog
* Thu Mar 31 2005 Igor Zubkov <icesik@mail.ru> 4.1.4-los2
- move sed from /usr/bin to /bin for fhs compatible.

* Thu Mar 24 2005 Igor Zubkov <icesik@mail.ru> 4.1.4-los1
- update to 4.1.4.

* Wed Jan 19 2005 Igor Zubkov <icesik@mail.ru> 4.0.9-los1
- update to 4.0.9.

* Mon Nov 08 2004 Igor Zubkov <icesik@mail.ru> 4.0.5-los1
- Initial build for Los Angeles GNU/Linux.
