# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

Name: task-core
Version: 1
Release: los6
Summary: Metapackage for minimal environment.

License: Public Domain

Group: Tasks

#Requires: alternatives # todo
Requires: apt
#Requires: basesystem # todo
Requires: bash
Requires: bzip2
#Requires: chkconfig # todo
Requires: lost_stuff
#Requires: kbd
#Requires: console-tools
#Requires: console-tools-fonts
#Requires: console-tools-keymaps
Requires: coreutils
Requires: cracklib
Requires: ed
#Requires: etcskel # todo
Requires: filesystem
Requires: findutils
Requires: gawk
Requires: gettext
#Requires: glibc-base # todo
Requires: grep
Requires: gzip
#Requires: info # FIXME
Requires: texinfo
#Requires: libslang1
Requires: libz
Requires: logrotate
Requires: mktemp
Requires: module-init-tools
Requires: libncurses
Requires: terminfo
#Requires: Linux-PAM # FIXME
#Requires: passwd
Requires: procps
Requires: psmisc
#Requires: rootfiles
Requires: rpm
Requires: sed
#Requires: setup
#Requires: shadow-utils
#Requires: sysklogd
#Requires: syslog-daemon-any
Requires: tar
Requires: util-linux
Requires: gnupg
#Requires: sysvinit # FIXME
Requires: udev
Requires: words
Requires: libreadline5
Requires: fix-info-dir

BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildArch: noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for a minimal work environment. The main use is for creating an
environment inside chroot.

%files

%changelog
* Fri Mar 11 2005 Igor Zubkov <icesik@mail.ru> 1-los4
- add fix-info-dir to requires.

* Mon Jan 10 2005 Igor Zubkov <icesik@mail.ru> 1-los2
- s/zlib/libz/.

* Wed Nov 17 2004 Igor Zubkov <icesik@mail.ru> 1-los1
- Initial build for Los Angeles GNU/Linux.
