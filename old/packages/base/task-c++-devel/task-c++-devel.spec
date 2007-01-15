# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

Name: task-c++-devel
Version: 1
Release: los2
Summary: Metapackage for C++ development
License: GPL
Group: Tasks

PreReq: task-c-devel

Requires: libstdc++3.4-dev
Requires: g++3.4

BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildArch: noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for a complete environment for development of programs in
the C++ programming language.
It itself includes no software, only dependencies on software.

%files

%changelog
* Thu Mar 31 2005 Igor Zubkov <icesik@mail.ru> 1-los2
- update to g++3.4 and libstdc++3.4-dev.

* Fri Jan 14 2005 Igor Zubkov <icesik@mail.ru> 1-los1
- Initial build for Los Angeles GNU/Linux.
