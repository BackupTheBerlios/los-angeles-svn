# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		The GNU Internationalization (NLS) system
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		gettext
%define ver		0.14.1
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		base
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	gettext-runtime

%description
The Gettext package is used for internationalization and localization.
Programs  can  be  compiled  with  Native Language Support (NLS) which
enable them to output messages in the user's native language.

%package runtime
Summary: gettext-runtime
License: LGPL
Group: base

%description runtime
gettext-runtime

%package tools
Summary: gettext-tools
License: GPL
Group: development
Requires: %{name} = %{version}-%{release}

%description tools
gettext-tools

%package doc
Summary: gettext-doc
License: GPL
Group: doc
#Requires: %{name} = %{version}-%{release}

%description doc
gettext-doc

%prep
%setup -q

%build
cd gettext-runtime/
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1
cd ../gettext-tools/
%configure
%{__make} %{_smp_mflags}
%{__make} check || exit 1

%install
cd gettext-runtime/
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
cd ../gettext-tools/
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

#cd ${RPM_BUILD_ROOT}/usr/doc
#mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/gettext/
#mv gettext/ ${RPM_BUILD_ROOT}%{_docdir}/gettext/
#cd ..
#rm -rf doc

%post -n gettext-runtime -p /sbin/ldconfig
%postun -n gettext-runtime -p /sbin/ldconfig

%post -n gettext-tools -p /sbin/ldconfig
%postun -n gettext-tools -p /sbin/ldconfig

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog ChangeLog.0 NEWS PACKAGING README README.mingw
%doc README.vms README.woe32 THANKS

%files runtime
%defattr(-,root,root)
%doc gettext-runtime/AUTHORS
%doc gettext-runtime/BUGS
%doc gettext-runtime/ChangeLog
%doc gettext-runtime/NEWS
%doc gettext-runtime/README
%doc gettext-runtime/README.woe32
%{_bindir}/envsubst
%{_bindir}/ngettext
%{_bindir}/gettext.sh
%{_bindir}/gettext
%{_libdir}/libasprintf.a
%{_libdir}/libasprintf.la
%{_libdir}/libasprintf.so
%{_libdir}/libasprintf.so.*
%doc %{_datadir}/gettext/ABOUT-NLS
%{_datadir}/locale/*/*/gettext-runtime.mo
%doc %{_datadir}/doc/libasprintf/autosprintf.html
%dir %{_datadir}/doc/gettext/
%{_includedir}/autosprintf.h
%doc %{_infodir}/autosprintf.info*
%doc %{_mandir}/man1/envsubst.1*
%doc %{_mandir}/man1/ngettext.1*
%doc %{_mandir}/man1/gettext.1*
%doc %{_mandir}/man3/bindtextdomain.3*
%doc %{_mandir}/man3/ngettext.3*
%doc %{_mandir}/man3/dcngettext.3*
%doc %{_mandir}/man3/bind_textdomain_codeset.3*
%doc %{_mandir}/man3/dngettext.3*
%doc %{_mandir}/man3/textdomain.3*
%doc %{_mandir}/man3/dcgettext.3*
%doc %{_mandir}/man3/gettext.3*
%doc %{_mandir}/man3/dgettext.3*

%files tools
%defattr(-,root,root)
%doc gettext-tools/ChangeLog
%doc gettext-tools/README.woe32
%doc gettext-tools/TODO
%{_bindir}/autopoint
%{_bindir}/gettextize
%{_bindir}/msgattrib
%{_bindir}/msgcat
%{_bindir}/msgcmp
%{_bindir}/msgcomm
%{_bindir}/msgconv
%{_bindir}/msgen
%{_bindir}/msgexec
%{_bindir}/msgfilter
%{_bindir}/msgfmt
%{_bindir}/msggrep
%{_bindir}/msginit
%{_bindir}/msgmerge
%{_bindir}/msgunfmt
%{_bindir}/msguniq
%{_bindir}/xgettext
%{_includedir}/gettext-po.h
%doc %{_infodir}/gettext.info*
%{_libdir}/libgettextlib-0.14.1.so
%{_libdir}/libgettextlib.la
%{_libdir}/libgettextlib.so
%{_libdir}/libgettextpo.a
%{_libdir}/libgettextpo.la
%{_libdir}/libgettextpo.so
%{_libdir}/libgettextpo.so.*
%{_libdir}/libgettextsrc-0.14.1.so
%{_libdir}/libgettextsrc.la
%{_libdir}/libgettextsrc.so
%{_libdir}/preloadable_libintl.so
%{_libdir}/gettext/*
%{_datadir}/aclocal/
%{_datadir}/gettext/
%{_datadir}/locale/*/*/gettext-tools.mo
%doc %{_mandir}/man1/autopoint.1*
%doc %{_mandir}/man1/gettextize.1*
%doc %{_mandir}/man1/msgattrib.1*
%doc %{_mandir}/man1/msgcat.1*
%doc %{_mandir}/man1/msgcmp.1*
%doc %{_mandir}/man1/msgcomm.1*
%doc %{_mandir}/man1/msgconv.1*
%doc %{_mandir}/man1/msgen.1*
%doc %{_mandir}/man1/msgexec.1*
%doc %{_mandir}/man1/msgfilter.1*
%doc %{_mandir}/man1/msgfmt.1*
%doc %{_mandir}/man1/msggrep.1*
%doc %{_mandir}/man1/msginit.1*
%doc %{_mandir}/man1/msgmerge.1*
%doc %{_mandir}/man1/msgunfmt.1*
%doc %{_mandir}/man1/msguniq.1*
%doc %{_mandir}/man1/xgettext.1*

%files doc
%defattr(-,root,root)
%doc %{_datadir}/doc/libasprintf/
%doc %{_datadir}/doc/gettext/

%changelog
* Tue Nov 23 2004 Igor Zubkov <icesik@mail.ru> 0.14.1-los1
- update to 0.14.1

* Mon Nov 22 2004 Igor Zubkov <icesik@mail.ru> 0.11.5-los1
- Initial build for Los Angeles GNU/Linux.
