# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

Name: task-base
Version: 1
Release: los4
Summary: Metapackage for basic environment.
License: GPL
Group: Tasks

Requires: task-core
Requires: grub
#Requires: memtest86
#Requires: ash
#Requires: initscripts
#Requires: bootsplash
Requires: hdparm
#Requires: hotplug
Requires: e2fsprogs
Requires: sysvinit 
#Requires: mkinitrd
#Requires: authconfig
#Requires: dhcpcd 
Requires: eject
#Requires: pciutils 
#Requires: mount # FIXME это уже есть в util-linux!
Requires: less
Requires: grep
#Requires: pam # FIXME
Requires: Linux-PAM
#Requires: netconfig
#Requires: mouseconfig
#Requires: crontabs
#Requires: slocate
#Requires: vixie-cron
Requires: cron-daemon-any
#Requires: anacron
Requires: shadow
Requires: syslog-daemon-any

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for a minimal work environment. The main use is for creating
minimal bootable system. 

%files

%changelog
* Fri Dec 17 2004 Igor Zubkov <icesik@mail.ru> 1-los2
- add shadow to Requires.

* Sun Nov 28 2004 Igor Zubkov <icesik@mail.ru> 1-los1
- Initial build for Los Angeles GNU/Linux.
