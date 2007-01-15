Summary: Russian translations of Linux manpages.
Summary(ru): ������� �������� ������� ����������� �� Linux.
Name: manpages-ru
Packager: Igor Zubkov <icesik@mail.ru>
Version: 0.7
Release: los1
Url: http://alexm.here.ru/manpages-ru/
Source: http://alexm.here.ru/%{name}/download/%{name}-%{version}.tar.gz
Copyright: Freely Distributable
Group: Documentation
Group(ru): ������������
Buildroot: /var/tmp/%{name}-root
BuildArchitectures: noarch

%description
A small collection of man pages (documentation) from the Linux Documentation
Project (LDP) translated to russian.  The man pages are organized into the
following sections: Section 1, user commands; Section 2, system
calls; Section 3, libc calls; Section 4, devices (e.g., hd, sd); Section 5,
file formats and protocols (e.g., wtmp, /etc/passwd, nfs); Section 6, games
(intro only); Section 7, conventions, macro packages, etc. (e.g., nroff,
ascii); and Section 8, system administration.

%description -l ru_RU.KOI8-R
��������� ��������� ������� ����������� �� ������� ������������ ��
������, �� ������� �����.  �������� ����������� ������������ ���������
�������: ������ 1, ������� ������������; ������ 2, ��������� ������;
������ 3, ������� ���������� ����� C; ������ 4, ���������� (��������,
hd, sd); ������ 4, ������� ������ � ��������� (��������, wtmp,
/etc/passwd, nfs); ������ 6, ���� (������ ��������); ������ 7,
����������, �����-������, � �. �. (��������, nroff, ascii); � ������
8, ������� ��������������.

%prep
%setup -q
rm -f man5/passwd.5

%install
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/
%{__make} install INSTALLPATH=${RPM_BUILD_ROOT}%{_mandir}/ LANG_SUBDIR=ru COMPRESS=none

%files
%defattr(-,root,root)
%doc CREDITS FAQ NEWS README
%{_mandir}/ru/*/*

%changelog
* Sat Mar 12 2005 Igor Zubkov <icesik@mail.ru> 0.7-los1
- Initial build for Los Angeles GNU/Linux.
