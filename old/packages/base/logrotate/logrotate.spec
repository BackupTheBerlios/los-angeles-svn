# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Rotates, compresses, removes and mails system log files.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		logrotate
%define ver		3.6.5
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		System/Base
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libpopt
BuildRequires:	libpopt-dev

%description
The logrotate utility is designed to simplify the administration of
log files on a system which generates a lot of log files.  Logrotate
allows for the automatic rotation compression, removal and mailing of
log files.  Logrotate can be set to handle a log file daily, weekly,
monthly or when the log file gets to a certain size.  Normally,
logrotate runs as a daily cron job.

Install the logrotate package if you need a utility to deal with the
log files on your system.

%prep
%setup -q

%build
%{__make} RPM_OPT_FLAGS="${RPM_OPT_FLAGS}" %{_smp_mflags} CC=%{__cc}

%install
%{__make} PREFIX=${RPM_BUILD_ROOT} MANDIR=%{_mandir} install

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily
mkdir -p ${RPM_BUILD_ROOT}/var/lib

install -m 644 examples/logrotate-default ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.conf
install -m 755 examples/logrotate.cron ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/logrotate
touch ${RPM_BUILD_ROOT}/var/lib/logrotate.status


%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc CHANGES
%attr(0755, root, root) %{_sbindir}/logrotate
%attr(0644, root, root) %{_mandir}/man8/logrotate.8*
%attr(0755, root, root) %{_sysconfdir}/cron.daily/logrotate
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/logrotate.conf
%attr(0755, root, root) %dir %{_sysconfdir}/logrotate.d
%attr(0644, root, root) %verify(not size md5 mtime) %config(noreplace) /var/lib/logrotate.status

%changelog
* Tue Nov 09 2004 Igor Zubkov <icesik@mail.ru> 3.6.5-los1
- Initial build for Los Angeles GNU/Linux.
