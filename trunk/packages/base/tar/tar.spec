# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		A GNU file archiving program.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		tar
%define ver		1.15.1
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Archiving
Group(ru_RU.KOI8-R):	Архиваторы
Source0:	%{name}-1.15.1.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags}
#%{__make} check || exit 1

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

mv ${RPM_BUILD_ROOT}%{_libexecdir}/rmt ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}%{_bindir}/tar ${RPM_BUILD_ROOT}/bin/

rm -rf ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog ChangeLog.1 NEWS PORTS README THANKS TODO
/bin/tar
%{_bindir}/rmt
%doc %{_infodir}/*

%changelog
* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 1.15.1-los1
- update to 1.15.1
- remove Vendor field.
- add russian group description.

* Mon Nov 08 2004 Igor Zubkov <icesik@mail.ru> 1.14-los1
- update to 1.14

* Sat May 08 2004 Igor Zubkov <icesik@mail.ru> 1.13.92-los1
- Initial build for Los Angeles GNU/Linux.
