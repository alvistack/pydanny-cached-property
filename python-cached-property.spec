# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-cached-property
Epoch: 100
Version: 2.0.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Cached-property for decorating methods in Python classes
License: BSD-3-Clause
URL: https://github.com/pydanny/cached-property/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
cached_property allows properties in Python classes to be cached until
the cache is invalidated or expired.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cached-property
Summary: Cached-property for decorating methods in Python classes
Requires: python3
Provides: python3-cached_property = %{epoch}:%{version}-%{release}
Provides: python3dist(cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cached_property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cached_property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cached-property) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-cached-property
cached_property allows properties in Python classes to be cached until
the cache is invalidated or expired.

%files -n python%{python3_version_nodots}-cached-property
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-cached-property
Summary: Cached-property for decorating methods in Python classes
Requires: python3
Provides: python3-cached_property = %{epoch}:%{version}-%{release}
Provides: python3dist(cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cached_property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cached_property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cached-property) = %{epoch}:%{version}-%{release}

%description -n python3-cached-property
cached_property allows properties in Python classes to be cached until
the cache is invalidated or expired.

%files -n python3-cached-property
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-cached_property
Summary: Cached-property for decorating methods in Python classes
Requires: python3
Provides: python3-cached_property = %{epoch}:%{version}-%{release}
Provides: python3dist(cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cached_property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cached-property) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cached_property = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cached-property) = %{epoch}:%{version}-%{release}

%description -n python3-cached_property
cached_property allows properties in Python classes to be cached until
the cache is invalidated or expired.

%files -n python3-cached_property
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
