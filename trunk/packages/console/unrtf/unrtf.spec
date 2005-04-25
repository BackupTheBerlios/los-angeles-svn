%define sum		rtf to html convertor
%define maintainer	Igor Zubkov <icesik@mail.ru>
%define name		unrtf
%define ver		0.19.3
%define rel		los1

Summary:	%{sum}
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	GPL
Group:		Utils
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
UnRTF is a moderately complicated converter from RTF to other
formats, including HTML, LaTeX, text, and PostScript. Converting
to HTML, it supports tables, fonts, colors, embedded images, 
hyperlinks, paragraph alignment among other things. All other
conversions are "alpha"--just begun.

Compiling with GCC: type "make all", and assuming you have GCC
and GNU make, it should compile without any warnings or errors 
under Linux, BSD, and DOS (using DJGPP). Amiga/GCC users
should utilize the build.amiga file. Please let me know of 
any compilation problems.

This program includes no warranty whatsoever. It is provided
"AS IS". For more information please read the COPYING
document, which should be included with the source code.
It describes the GNU Public License, which covers UnRTF.

%prep
%setup -q

%build
%{__make} %{_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}/
mkdir -p ${RPM_BUILD_ROOT}%{_man1dir}/

cp unrtf ${RPM_BUILD_ROOT}%{_bindir}/
cp unrtf.1 ${RPM_BUILD_ROOT}%{_man1dir}/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES COPYING README TODO doc/unrtf.html
%{_bindir}/*
%doc %{_man1dir}/*

%changelog
* Tue Apr 19 2005 Igor Zubkov <icesik@mail.ru> 0.19.3-los1
- update to 0.19.3.

* Thu May 20 2004 Igor Zubkov <icesik@mail.ru> 0.18.1-los1
- Initial build for Los Angeles GNU/Linux.
