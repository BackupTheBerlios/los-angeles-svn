# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define name		syslog-ng
%define ver		1.6.6
%define rel		los3
%define libolver	0.3.9

%define _sbindir	/sbin

Summary:           Syslog replacement daemon
Name:              %{name}
Version:           %{ver}
Release:           %{rel}
Group:             System/Kernel and hardware
License:           GPL
Url:               http://www.balabit.com/products/syslog_ng/
Source0:           %{name}-%{version}.tar.gz
Source1:           %{name}-%{version}.tar.gz.asc
Buildroot:         %{_tmppath}/%{name}-buildroot

Requires:	libol >= %{libolver}
BuildRequires:	libol-dev >= %{libolver}
BuildRequires:	which

Provides:	syslog-daemon-any

Obsoletes:      sysklogd metalog

%description
syslog-ng, as the name shows, is a syslogd replacement, but with new 
functionality for the new generation. The original syslogd allows 
messages only to be sorted based on priority/facility pairs; syslog-ng 
adds the possibility to filter based on message contents using regular 
expressions. The new configuration scheme is intuitive and powerful. 
Forwarding logs over TCP and remembering all forwarding hops makes it 
ideal for firewalled environments.

%prep
%setup -q

%build
%configure
# --enable-tcp-wrapper
%{__make}

%install
make DESTDIR=%{buildroot} mandir=%{_mandir} install-strip

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog INSTALL NEWS PORTS
%doc doc/sgml/syslog-ng.txt
%doc doc/*.demo doc/*.sample doc/*.solaris
%{_sbindir}/syslog-ng
%doc %{_man5dir}/*
%doc %{_man8dir}/*

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%changelog
* Sun Feb 06 2005 Igor Zubkov <icesik@mail.ru> 1.6.6-los3
- Initial build for Los Angeles GNU/Linux.
