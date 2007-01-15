# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

%define sum		CVS is a version control system.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		cvs
%define ver		1.11.17
%define rel		los1
%define url		http://cvshome.org

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Development/CVS
Source0:	ftp://ftp.cvshome.com/pub/%{name}-%{version}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{ver}-los-system-zlib.patch
Patch1:		%{name}-%{ver}-los-csh-path.patch
URL:		%{url}
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	libz
BuildRequires:	libz-dev
BuildRequires:	editor
Requires:	editor

%description
CVS is a version control system, which allows you to keep old versions
of files (usually source code), keep a log of who, when, and why
changes occurred, etc., like RCS or SCCS.  It handles multiple
developers, multiple directories, triggers to enable/log/control
various operations, and can work over a wide area network.  The
following tasks are not included; they can be done in conjunction with
CVS but will tend to require some script-writing and software other
than CVS: bug-tracking, build management (that is, make and make-like
tools), and automated testing.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --without-gssapi
%{__make} %{_smp_mflags}
#make check

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%post
/usr/bin/install-info /%{_infodir}/cvs.info.gz /%{_infodir}/dir
/usr/bin/install-info /%{_infodir}/cvsclient.info.gz /%{_infodir}/dir 

%preun
if [ $1 = 0 ]; then
# uninstall the info reference in the dir file
/usr/bin/install-info --delete /%{_infodir}/cvs.info.gz /%{_infodir}/dir
/usr/bin/install-info --delete /%{_infodir}/cvsclient.info.gz /%{_infodir}/dir
fi

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog ChangeLog.zoo DEVEL-CVS FAQ HACKING 
%doc INSTALL MINOR-BUGS NEWS PROJECTS README README.VMS TESTS TODO
%doc cvs-format.el
%{_bindir}/*
%doc %{_man1dir}/*
%doc %{_man5dir}/*
%doc %{_man8dir}/*
%doc %{_infodir}/*
%{_datadir}/cvs/contrib/*

%changelog
* Sat Feb 05 2005 Igor Zubkov <icesik@mail.ru> 1.11.17-los1
- Initial build for Los Angeles GNU/Linux.
