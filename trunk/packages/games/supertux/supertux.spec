Summary:	supertux
Name:		supertux
Version:	0.1.1
Release:	los1
License:	GPL v2
Group:		Games
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	SDL-dev
BuildRequires:	SDL_mixer-dev
BuildRequires:	SDL_image-dev
BuildRequires:	libz-dev

%description
supertux

%prep
%setup -q

%build
export LDFLAGS="-Wl,-rpath,/usr/X11R6/lib"
%configure \
	--disable-debug
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL LEVELDESIGN NEWS README TODO
%{_bindir}/supertux
%{_datadir}/supertux/

%changelog
* Mon May 02 2005 Igor Zubkov <icesik@mail.ru> 0.1.1-los1
- Initial build for Los Angeles GNU/Linux.
