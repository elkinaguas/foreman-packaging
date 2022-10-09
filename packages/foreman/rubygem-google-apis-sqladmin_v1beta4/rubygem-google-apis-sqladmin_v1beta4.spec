# template: default
%global gem_name google-apis-sqladmin_v1beta4

Name: rubygem-%{gem_name}
Version: 0.38.0
Release: 1%{?dist}
Summary: Simple REST client for Cloud SQL Admin API V1beta4
License: Apache-2.0
URL: https://github.com/google/google-api-ruby-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This is the simple REST client for Cloud SQL Admin API V1beta4. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud SQL Admin API, but
note that some services may provide a separate modern client that is easier to
use.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE.md
%doc %{gem_instdir}/OVERVIEW.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md

%changelog
* Sun Oct 09 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.38.0-1
- Update to 0.38.0

* Wed Jul 13 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.32.0-1
- Add rubygem-google-apis-sqladmin_v1beta4 generated by gem2rpm using the default template

