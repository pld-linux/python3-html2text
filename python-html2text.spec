#
# Conditional build:
%bcond_without	python2		# Python 2 package
%bcond_without	python3		# Python 3 package

%define		module	html2text
Summary:	A HTML to markdown-structured text converter
Name:		python-%{module}
Version:	2016.1.8
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/h/html2text/%{module}-%{version}.tar.gz
# Source0-md5:	a1e9b15c2ad5643c95fe790fd4a5df61
URL:		https://github.com/Alir3z4/html2text/
%if %{with python2}
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-Cython
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A HTML to markdown-structured text converter.

%package -n python3-%{module}
Summary:	A HTML to markdown-structured text converter
Group:		Libraries/Python

%description -n python3-%{module}
A HTML to markdown-structured text converter.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/html2text
%{py_sitescriptdir}/html2text/*.py[co]
%{py_sitescriptdir}/html2text-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/html2text
%{py3_sitescriptdir}/html2text/*.py
%{py3_sitescriptdir}/html2text/__pycache__
%{py3_sitescriptdir}/html2text-*.egg-info
%endif
