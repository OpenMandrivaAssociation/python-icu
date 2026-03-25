%define module icu
%define oname PyICU
%bcond tests 1

Name:		python-icu
Version:	2.16.2
Release:	1
Summary:	Python extension wrapping IBM's ICU C++ libraries
Group:		Development/Python
License:	MIT
URL:		https://gitlab.pyicu.org/main/pyicu
Source0:	https://pypi.python.org/packages/source/p/pyicu/pyicu-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem: python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	pkgconfig(icu-i18n)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%rename	python3-icu

%description
PyICU is Python extension wrapping IBM's International Components
for Unicode C++ library (ICU). ICU is a mature, widely used set of
C/C++ and Java libraries providing Unicode and Globalization support
for software applications. ICU is widely portable and gives applications
the same results on all platforms and between C/C++ and Javasoftware.

%prep -a
# Remove bundled egg-info
rm -rf py/%{oname}.egg-info

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pytest
%endif

%files
%doc README.md CHANGES CREDITS
%{python_sitearch}/%{module}
%{python_sitearch}/py%{module}-%{version}.dist-info
