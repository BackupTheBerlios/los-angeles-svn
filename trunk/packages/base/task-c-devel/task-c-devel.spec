# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

Name: task-c-devel
Version: 1
Release: los3
License: Public Domain
Summary: Metapackage for C development

Group: Tasks

Requires: binutils
Requires: bison
Requires: cpp3.3
Requires: diffutils
Requires: flex
Requires: gcc3.3
Requires: glibc-dev
Requires: libtool
Requires: m4
Requires: make
Requires: patch
Requires: texinfo
Requires: gettext
Requires: gettext-tools
#Requires: glibc-kernheaders
Requires: linux-libc-headers

BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildArch: noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for a complete environment for development of programs in
the C programming language.
It itself includes no software, only dependencies on software.

%files

%changelog
* Wed Jan 19 2005 Igor Zubkov <icesik@mail.ru> 1-los3
- remove glibc-kernheaders from Requires.

* Fri Dec 10 2004 Igor Zubkov <icesik@mail.ru> 1-los2
- add linux-libc-headers to Requires.

* Wed Dec 08 2004 Igor Zubkov <icesik@mail.ru> 1-los1
- Initial build for Los Angeles GNU/Linux.
