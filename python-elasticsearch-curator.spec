%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname curator

Name:       python-elasticsearch-curator
Version:    2.0.2
Release:    1%{?dist}
Summary:    Manage Elasticsearch indices via the Elasticsearch Curator API
Group:      Development/Libraries
License:    Apache License, Version 2.0
URL:        https://github.com/elasticsearch/curator
Source0:    https://github.com/elasticsearch/curator/archive/v%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

BuildRequires:  python-setuptools
Requires:   python-elasticsearch
Requires:   python-urllib3
Requires:   python-argparse

Obsoletes:  elasticsearch-curator

%description
The Curator script is a wrapper for the Elasticsearch Curator API, which allows
you to manage your indices with commands like delete, optimize, close,
snapshot, alias ... and more!


%prep
%setup -q -n %{srcname}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
rm -rf %{buildroot}
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/curator
%{_bindir}/es_repo_mgr
%{python2_sitelib}/elasticsearch_curator-%{version}-py*.egg-info/*
%{python2_sitelib}/curator/*


%changelog
* Thu Oct 29 2014 Alex Schultz <aschultz@next-development.com> 2.0.2-1
- Update to 2.0.2 and spec file updates
* Thu Aug 21 2014 Matt Dainty <matt@bodgit-n-scarper.com> 1.2.2-1
- Rename package to python-* and obsolete old package name.
* Mon Jun 23 2014 Matt Dainty <matt@bodgit-n-scarper.com> 1.1.2-1
- Initial build.
