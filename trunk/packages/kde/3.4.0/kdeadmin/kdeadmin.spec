%define sum		KDE Administration tools metapackage.
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		kdeadmin
%define ver		3.4.0
%define rel		los1.1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		KDE
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Requires:	kcron
Requires:	kdat
Requires:	kpackage
Requires:	ksysv
Requires:	kuser
Requires:	secpolicy
Requires:	kde-kfile-deb
Requires:	kde-kfile-rpm

#BuildRequires:	lilo

%description
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This package depends on the KDE Administration tools packages.

%package -n kcron
Summary: KDE Crontab editor.
Group: KDE
License: GPL

%description -n kcron
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

Crontab editor for KDE.

This package is part of the official KDE admin module.

%package -n kdat
Summary: KDE tape backup tool.
Group: KDE
License: GPL

%description -n kdat
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

Tape backup tool for KDE.

This package is part of the official KDE admin module.

%package -n kpackage
Summary: KDE Software package tool.
Group: KDE
License: GPL

%description -n kpackage
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This is a frontend to both .rpm and .deb package formats.  It allows you
to view currently installed packages, browse available packages, and
install/remove them.

This package is part of the official KDE admin module.

%package -n ksysv
Summary: KDE SysV-style init configuration editor.
Group: KDE
License: GPL

%description -n ksysv
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This program allows you to edit your start and stop scripts using a
drag and drop GUI.

This package is part of the official KDE admin module.

%package -n kuser
Summary: KDE user/group administration tool.
Group: KDE
License: GPL

%description -n kuser
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

A user/group administration tool for KDE.

This package is part of the official KDE admin module.

%package -n secpolicy
Summary: KDE PAM security policy configuration tool.
Group: KDE
License: BSD-like

%description -n secpolicy
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This tool allows you to manipulate the PAM configuration files for each
"service" you have created to use PAM.

This package is part of the official KDE admin module.

%package -n kde-kfile-deb
Summary: kde-kfile-deb
Group: KDE
License: GPL

%description -n kde-kfile-deb
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

File dialog plugin for deb package files.

This package is part of the official KDE admin module.

%package -n kde-kfile-rpm
Summary: kde-kfile-rpm
Group: KDE
License: GPL

%description -n kde-kfile-rpm
KDE is a powerful Open Source graphical desktop environment
for Unix workstations. It combines ease of use, contemporary
functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

File dialog plugin for rpm package files.

This package is part of the official KDE admin module.

#TODO:
#%package -n kde-kcm-lilo
#Summary: KDE Frontend for lilo configuration.
#Group: KDE
#Requires: lilo
#License: GPL
#
#%description -n kde-kcm-lilo
#KDE is a powerful Open Source graphical desktop environment
#for Unix workstations. It combines ease of use, contemporary
#functionality, and outstanding graphical design with the
#technological superiority of the Unix operating system.
#
#lilo-config is a KDE based frontend to the lilo boot manager configuration.
#It runs out of the KDE Control Center.
#
#This package is part of the official KDE admin module.

%prep
#setup -q

%build
#configure \
#	--disable-debug \
#	--enable-final \
#	--enable-pch
#{__make} %{_smp_mflags}

%install
#{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
#rm -rf %{buildroot}
#rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)

%files -n kcron
%defattr(-,root,root)
%{_bindir}/kcron
%{_datadir}/applications/kde/kcron.desktop
%{_datadir}/apps/kcron/
%lang(en) %{_datadir}/doc/HTML/en/kcron/
%{_datadir}/icons/*/*/apps/kcron.png

%files -n kdat
%defattr(-,root,root)
%{_bindir}/kdat
%{_datadir}/applications/kde/kdat.desktop
%{_datadir}/apps/kdat/
%lang(en) %{_datadir}/doc/HTML/en/kdat/
%{_datadir}/icons/*/*/apps/kdat.png

%files -n kpackage
%defattr(-,root,root)
%{_bindir}/kpackage
%{_datadir}/applications/kde/kpackage.desktop
%{_datadir}/apps/kpackage/
%lang(en) %{_datadir}/doc/HTML/en/kpackage/
%{_datadir}/icons/*/*/apps/kpackage.png
%{_datadir}/mimelnk/application/x-debian-package.desktop

%files -n ksysv
%defattr(-,root,root)
%{_bindir}/ksysv
%{_datadir}/applications/kde/ksysv.desktop
%{_datadir}/apps/ksysv/
%lang(en) %{_datadir}/doc/HTML/en/ksysv/
%{_datadir}/icons/*/*/apps/ksysv.png
%{_datadir}/icons/crystalsvg/16x16/actions/toggle_log.png
%{_datadir}/mimelnk/application/x-ksysv.desktop
%{_datadir}/mimelnk/text/x-ksysv-log.desktop

%files -n kuser
%defattr(-,root,root)
%{_bindir}/kuser
%{_datadir}/applications/kde/kuser.desktop
%{_datadir}/apps/kuser/
%{_datadir}/config.kcfg/kuser.kcfg
%lang(en) %{_datadir}/doc/HTML/en/kuser/*
%{_datadir}/icons/*/*/apps/kuser.png

%files -n secpolicy
%defattr(-,root,root)
%{_bindir}/secpolicy

%files -n kde-kfile-deb
%defattr(-,root,root)
%{_libdir}/kde3/kfile_deb.*
%{_datadir}/services/kfile_deb.desktop

%files -n kde-kfile-rpm
%defattr(-,root,root)
%{_libdir}/kde3/kfile_rpm.*
%{_datadir}/services/kfile_rpm.desktop

#%files -n kde-kcm-lilo
#%defattr(-,root,root)
#%{_libdir}/kde3/kcm_lilo.*
#%{_datadir}/applications/kde/lilo.desktop

%changelog
* Sun Apr 24 2005 Igor Zubkov <icesik@mail.ru> 3.4.0-los1
- Initial build for Los Angeles GNU/Linux.
