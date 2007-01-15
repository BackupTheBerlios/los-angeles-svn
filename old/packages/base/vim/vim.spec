# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		Vim is an almost compatible version of the UNIX editor Vi.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		vim
%define ver		6.3.068
%define rel		los1
%define url		http://www.vim.org/

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	Charityware/GPL
Group:		System/Base
Source0:	ftp://ftp.vim.org/pub/vim/unix/vim-6.3.tar.bz2
Source1:	vim-6.3-lang.tar.gz
Patch1:		6.3.001
Patch2:		6.3.002
Patch3:		6.3.003
Patch4:		6.3.004
Patch5:		6.3.005
Patch6:		6.3.006
Patch7:		6.3.007
Patch8:		6.3.008
Patch9:		6.3.009
Patch10:	6.3.010
Patch11:	6.3.011
Patch12:	6.3.012
Patch13:	6.3.013
Patch14:	6.3.014
Patch15:	6.3.015
Patch16:	6.3.016
Patch17:	6.3.017
Patch18:	6.3.018
Patch19:	6.3.019
Patch20:	6.3.020
Patch21:	6.3.021
Patch22:	6.3.022
Patch23:	6.3.023
Patch24:	6.3.024
Patch25:	6.3.025
Patch26:	6.3.026
Patch27:	6.3.027
Patch28:	6.3.028
Patch29:	6.3.029
Patch30:	6.3.030
Patch31:	6.3.031
Patch32:	6.3.032
Patch33:	6.3.033
Patch34:	6.3.034
Patch36:	6.3.036
Patch37:	6.3.037
Patch39:	6.3.039
Patch40:	6.3.040
Patch42:	6.3.042
Patch43:	6.3.043
Patch45:	6.3.045
Patch46:	6.3.046
Patch47:	6.3.047
Patch48:	6.3.048
Patch49:	6.3.049
Patch50:	6.3.050
Patch51:	6.3.051
Patch52:	6.3.052
Patch53:	6.3.053
Patch54:	6.3.054
Patch55:	6.3.055
Patch56:	6.3.056
Patch57:	6.3.057
Patch58:	6.3.058
Patch59:	6.3.059
Patch60:	6.3.060
Patch61:	6.3.061
Patch62:	6.3.062
Patch63:	6.3.063
Patch64:	6.3.064
Patch65:	6.3.065
Patch66:	6.3.066
Patch67:	6.3.067
Patch68:	6.3.068
URL:            %{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Provides:	editor

BuildRequires:	libncurses-dev
Requires:	libncurses

#BuildRequires:	gpm-dev
#Requires:	gpm

%description
Vim is an almost compatible version of the UNIX editor Vi.  Many new features
have been added: multi-level undo, syntax highlighting, command line history,
on-line help, filename completion, block operations, etc.  There is also a
Graphical User Interface (GUI) available.  See "runtime/doc/vi_diff.txt" for
differences with Vi.

This editor is very useful for editing programs and other plain ASCII files.
All commands are given with normal keyboard characters, so those who can type
with ten fingers can work very fast.  Additionally, function keys can be
defined by the user, and the mouse can be used.

Vim currently runs under Amiga DOS, MS-DOS, MS-Windows 95/98/Me/NT/2000/XP,
Atari MiNT, Macintosh, BeOS, VMS, RISC OS, OS/2 and almost all flavours of
UNIX.  Porting to other systems should not be very difficult.

%prep
%setup -q -n %{name}63

cd ${RPM_BUILD_DIR}/

cp %{SOURCE1} .
tar xf %{SOURCE1}

cd vim63/

%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%patch17 -p0
%patch18 -p0
%patch19 -p0
%patch20 -p0
%patch21 -p0
#%patch22 -p0
%patch23 -p0
%patch24 -p0
#%patch25 -p0
%patch26 -p0
%patch27 -p0
%patch28 -p0
%patch29 -p0
%patch30 -p0
%patch31 -p0
%patch32 -p0
%patch33 -p0
%patch34 -p0
%patch36 -p0
%patch37 -p0
%patch39 -p0
%patch40 -p0
%patch42 -p0
%patch43 -p0
%patch45 -p0
%patch46 -p0
#%patch47 -p0
#%patch48 -p0
%patch49 -p0
%patch50 -p0
%patch51 -p0
#%patch52 -p0
%patch53 -p0
%patch54 -p0
%patch55 -p0
%patch56 -p0
%patch57 -p0
%patch58 -p0
%patch59 -p0
%patch60 -p0
%patch61 -p0
%patch62 -p0
%patch63 -p0
%patch64 -p0
%patch65 -p0
%patch66 -p0
%patch67 -p0
%patch68 -p0

%build
%configure --enable-gui=no --without-x
%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
cd ${RPM_BUILD_ROOT}%{_datadir}/vim/vim63/tools/
gzip -9 *

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/vim63
rm -f  %{_builddir}/vim-6.3-lang.tar.gz

%files
%defattr(-,root,root)
%{_bindir}/*
%doc %{_man1dir}/*
%{_datadir}/vim/vim63/

%changelog
* Mon Apr 04 2005 Igor Zubkov <icesik@mail.ru> 6.3.068-los1
- update to 6.3.068.

* Sun Mar 27 2005 Igor Zubkov <icesik@mail.ru> 6.3.045-los2
- remove some deps.
- clean up spec.

* Sun Jan 09 2005 Igor Zubkov <icesik@mail.ru> 6.3.045-los1
- security fix upload.
- update to 6.3.045
- remove Vendor field.
- clean up spec file.
- remove Depends on gpm and gpm-dev.

* Mon Oct 25 2004 Igor Zubkov <icesik@mail.ru> 6.3.031-los1
- update to 6.3.31

* Thu Jun 17 2004 Igor Zubkov <icesik@mail.ru> 6.3.006-los1
- Initial build for Los Angeles GNU/Linux.
