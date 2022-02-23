%global repo_orgname RedHatInsights
%global repo_name insights-client-role

%global role_orgname %{repo_orgname}
%global role_name insights-client

Name: ansiblerole-insights-client
Summary: Packaging of the insights-client Ansible role
Version: 1.7.1
Release: 2%{?dist}
License: ASL 2.0

Source0: https://github.com/%{repo_orgname}/%{repo_name}/archive/v%{version}.tar.gz#/%{role_name}-%{version}.tar.gz
Url: https://github.com/%{repo_orgname}/%{repo_name}/
BuildArch: noarch

%if 0%{?rhel} == 7
Requires: ansible
%else
Requires: (ansible or ansible-core)
%endif

%description
This package installs the insights-client Ansibile role.

Make sure that "/usr/share/ansible/roles" is on your Ansible role_path.

%prep

%setup -qc

%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible/roles
cp -pR %{repo_name}-%{version} %{buildroot}%{_datadir}/ansible/roles/%{role_orgname}.%{role_name}

%files
%{_datadir}/ansible/roles/%{role_orgname}.%{role_name}
%doc %{repo_name}-%{version}/examples/*.yml
%doc %{repo_name}-%{version}/README.md
%license %{repo_name}-%{version}/LICENSE

%changelog
* Wed Feb 23 2022 Evgeni Golov - 1.7.1-2
- Require ansible or ansible-core on EL8+

* Tue Nov 26 2019 Marek Hulan <mhulan@redhat.com> - 1.7.1-1
- Update to 1.7.1

* Mon Sep 17 2018 Marek Hulan <mhulan@redhat.com> - 1.6-1
- Update to 1.6

* Thu Mar 15 2018 Gavin Romig-Koch <gavin@redhat.com> - 1.5-1
- Initial release.  Based largely on the pattern of rhel-system-roles.spec
