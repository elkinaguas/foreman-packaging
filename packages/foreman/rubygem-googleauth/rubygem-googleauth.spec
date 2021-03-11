# Generated from googleauth-0.6.7.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name googleauth

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.13.1
Release: 2%{?dist}
Summary: Google Auth Library for Ruby
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/google/google-auth-library-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.4.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(faraday) >= 0.17.3
Requires: %{?scl_prefix}rubygem(faraday) < 2.0
Requires: %{?scl_prefix}rubygem(jwt) >= 1.4
Requires: %{?scl_prefix}rubygem(jwt) < 3.0
Requires: %{?scl_prefix}rubygem(memoist) >= 0.16
Requires: %{?scl_prefix}rubygem(memoist) < 1
Requires: %{?scl_prefix}rubygem(multi_json) >= 1.11
Requires: %{?scl_prefix}rubygem(multi_json) < 2
Requires: %{?scl_prefix}rubygem(os) >= 0.9
Requires: %{?scl_prefix}rubygem(os) < 2.0
Requires: %{?scl_prefix}rubygem(signet) >= 0.14
Requires: %{?scl_prefix}rubygem(signet) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.4.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Allows simple authorization for accessing Google APIs.
Provide support for Application Default Credentials, as described at
https://developers.google.com/accounts/docs/application-default-credentials.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.kokoro
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.repo-metadata.json
%license %{gem_instdir}/COPYING
%{gem_libdir}
%{gem_instdir}/rakelib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%{gem_instdir}/Rakefile
%{gem_instdir}/googleauth.gemspec
%{gem_instdir}/integration
%{gem_instdir}/test
%{gem_instdir}/spec

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.13.1-2
- Rebuild against rh-ruby27

* Thu Oct 08 2020 Ondřej Ezr <oezr@redhat.com> 0.13.1-1
- Update to 0.13.1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.6.7-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.6.7-2
- Update spec to remove the ror scl

* Thu Mar 14 2019 kgaikwad <kavitagaikwad103@gmail.com> 0.6.7-1
- Add rubygem-googleauth generated by gem2rpm using the scl template

