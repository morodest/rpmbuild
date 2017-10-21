Name:           example
Version:        1.0
Release:        1%{?dist}
Summary:        Example

License:        GNU General Public License v3.0
URL:            https://git.wrke.in/ops/python-template
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	example_bin

BuildRequires:  bash
Requires:	bash

Autoreq:        0

%description
Github - https://github.com/morodest/rpmbuild

%build


%install
rm -rf %{buildroot}
install -d %{buildroot}/opt/pkg_name
install ../../app/* -t %{buildroot}/opt/pkg_name/

install -d %{buildroot}/usr/bin
install %{SOURCE0} %{buildroot}/usr/bin/example_bin

%files
%defattr(644, root, root, 755)
%dir /opt/pkg_name/
/opt/pkg_name/*
%attr(755, root, root) /usr/bin/example_bin

%changelog
* Sat Oct 21 2017 Vasiliy Mosunov <morodest@gmail.com> - 1.0-2
- init
