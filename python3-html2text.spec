%define		module	html2text
Summary:	A HTML to markdown-structured text converter
Name:		python3-%{module}
Version:	2024.2.26
Release:	3
License:	GPL v3
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/h/html2text/%{module}-%{version}.tar.gz
# Source0-md5:	b67974402e2e3ea0e7d611ce3096388c
URL:		https://github.com/Alir3z4/html2text/
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A HTML to markdown-structured text converter.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/html2text
%{py3_sitescriptdir}/html2text/*.py
%{py3_sitescriptdir}/html2text/__pycache__
%{py3_sitescriptdir}/html2text/py.typed
%{py3_sitescriptdir}/html2text-*.egg-info
