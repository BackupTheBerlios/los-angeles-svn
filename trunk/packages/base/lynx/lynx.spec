Summary:	Text based browser for the world wide web
Name:		lynx
Version:	2.8.5
Release:	los1
License:	GPL v2
Group:		Applications/Networking
Source0:	lynx%{version}rel.1.tar.bz2
Source1:	lynx%{version}rel.1.tar.bz2.asc
URL:		http://lynx.browser.org/
BuildRequires:	libncurses-dev
#BuildRequires:	gnutls-devel
BuildRequires:	libz-dev
Provides:	webclient
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%prep
%setup -q -n %{name}2-8-5

%build
%configure \
	--with-screen=ncurses \
	--without-included-gettext \
	--with-zlib \
	--enable-justify-elts \
	--enable-nested-tables \
	--enable-read-eta \
	--enable-kbd-layout \
	--enable-addrlist-page \
	--enable-cgi-links \
	--enable-default-colors \
	--enable-exec-links \
	--enable-exec-scripts \
	--enable-externs \
	--enable-gzip-help \
	--enable-internal-links \
	--enable-ipv6 \
	--enable-libjs \
	--enable-nls \
	--enable-nsl-fork \
	--enable-persistent-cookies \
	--enable-prettysrc \
	--enable-source-cache \
	--enable-warnings
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install install-help

%find_lang %{name}

%clean

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES COPYHEADER COPYING INSTALLATION PROBLEMS README samples test
%doc docs
%config(noreplace) %verify(not size mtime md5) %{_libdir}/lynx.cfg
%{_bindir}/lynx
%{_libdir}/lynx_help/
%doc %{_man1dir}/*

%changelog
