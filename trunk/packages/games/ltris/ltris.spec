%define sum		ltris
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		ltris
%define ver		1.0.9
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
Source0:	%{name}-%{ver}.tar.gz
License:	GPL v2
Group:		Games
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	SDL-dev
BuildRequires:	SDL_mixer-dev

%description
ltris - tetris.

%prep
%setup -q

%build
export LDFLAGS="-Wl,-rpath,/usr/X11R6/lib"
%configure
%{__make}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install

%files
%defattr(-,root,root)
%{_bindir}/ltris
%{_datadir}/ltris/
%{_localstatedir}/

%changelog
* Mon May 02 2005 Igor Zubkov <icesik@mail.ru> 1.0.9-los1
- Initial build for Los Angeles GNU/Linux.
