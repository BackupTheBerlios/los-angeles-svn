Summary:	A user-friendly file manager and visual shell
Summary(ru):	Диспетчер файлов Midnight Commander
Name:		mc
Version:	4.6.0
Release:	los1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.ibiblio.org/pub/Linux/utils/file/managers/mc/mc-%{version}.tar.gz
URL:		http://www.ibiblio.org/mc/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability to
ftp, view tar, zip files, and poke into RPMs for specific files. :-)

%prep
%setup -q

%build
%configure \
	--enable-charset

%{__make} %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

mkdir -p ${RPM_BUILD_ROOT}/etc/profile.d

install lib/{mc.sh,mc.csh} ${RPM_BUILD_ROOT}/etc/profile.d

%find_lang %{name}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog FAQ INSTALL MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/mc*
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/profile.d/*
%attr(755,root,root) %{_libdir}/mc/cons.saver
%dir %{_libdir}/mc

%dir %{_datadir}/mc

%{_datadir}/mc/bin
%{_datadir}/mc/syntax

%{_datadir}/mc/mc.ext
%{_datadir}/mc/cedit*
%{_datadir}/mc/edit.*
%{_datadir}/mc/mc.hlp
%lang(hu) %{_datadir}/mc/mc.hlp.hu
%lang(es) %{_datadir}/mc/mc.hlp.es
%lang(it) %{_datadir}/mc/mc.hlp.it
%lang(pl) %{_datadir}/mc/mc.hlp.pl
%lang(ru) %{_datadir}/mc/mc.hlp.ru
%{_datadir}/mc/mc.lib
%{_datadir}/mc/mc.menu
%{_datadir}/mc/mc.hint
%lang(cs) %{_datadir}/mc/mc.hint.cs
%lang(es) %{_datadir}/mc/mc.hint.es
%lang(hu) %{_datadir}/mc/mc.hint.hu
%lang(it) %{_datadir}/mc/mc.hint.it
%lang(nl) %{_datadir}/mc/mc.hint.nl
%lang(pl) %{_datadir}/mc/mc.hint.pl
%lang(ru) %{_datadir}/mc/mc.hint.ru
%lang(uk) %{_datadir}/mc/mc.hint.uk
%lang(zh) %{_datadir}/mc/mc.hint.zh

%dir %{_datadir}/mc/extfs
%{_datadir}/mc/extfs/README
%{_datadir}/mc/extfs/extfs.ini
%{_datadir}/mc/extfs/sfs.ini
%attr(755,root,root) %{_datadir}/mc/extfs/a
%attr(755,root,root) %{_datadir}/mc/extfs/apt
%attr(755,root,root) %{_datadir}/mc/extfs/audio
%attr(755,root,root) %{_datadir}/mc/extfs/bpp
%attr(755,root,root) %{_datadir}/mc/extfs/deb*
%attr(755,root,root) %{_datadir}/mc/extfs/dpkg
#%attr(755,root,root) %{_datadir}/mc/extfs/ftplist
%attr(755,root,root) %{_datadir}/mc/extfs/hp48
%attr(755,root,root) %{_datadir}/mc/extfs/lslR
%attr(755,root,root) %{_datadir}/mc/extfs/mailfs
%attr(755,root,root) %{_datadir}/mc/extfs/patchfs
%attr(755,root,root) %{_datadir}/mc/extfs/rpm*
%attr(755,root,root) %{_datadir}/mc/extfs/trpm
%attr(755,root,root) %{_datadir}/mc/extfs/uar*
#%attr(755,root,root) %{_datadir}/mc/extfs/ucpio
%attr(755,root,root) %{_datadir}/mc/extfs/uha
%attr(755,root,root) %{_datadir}/mc/extfs/ulha
%attr(755,root,root) %{_datadir}/mc/extfs/urar
#%attr(755,root,root) %{_datadir}/mc/extfs/uesp
%attr(755,root,root) %{_datadir}/mc/extfs/uzip
%attr(755,root,root) %{_datadir}/mc/extfs/uzoo
#%attr(755,root,root) %{_datadir}/mc/extfs/srpm
%{_datadir}/mc/mc.charsets
%{_datadir}/mc/term/
#%{_datadir}/applications/*.desktop
#%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ru) %{_mandir}/ru/man1/*

%changelog
* Sat Mar 12 2005 Igor Zubkov <icesik@mail.ru> 4.6.0-los1
- Initial build for Los Angeles GNU/Linux.
