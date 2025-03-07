%define		realname PyICU
%define		module icu
Name:		python-%{module}
Version:	2.14
Release:	2
Summary:	Python extension wrapping IBM's ICU C++ libraries
Group:		Development/Python
License:	MIT
URL:		https://gitlab.pyicu.org/main/pyicu
Source0:	https://pypi.python.org/packages/source/P/%{realname}/%{realname}-%{version}.tar.gz
Patch1:		0001-disable-failing-test.patch
BuildRequires:	python3-devel
BuildRequires:	python-pip
BuildRequires:	icu-devel
%rename	python3-icu

%description
PyICU is Python extension wrapping IBM's International Components
for Unicode C++ library (ICU). ICU is a mature, widely used set of
C/C++ and Java libraries providing Unicode and Globalization support
for software applications. ICU is widely portable and gives applications
the same results on all platforms and between C/C++ and Javasoftware.

%prep
%autosetup -p1 -n pyicu-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}
# Remove tests
rm -rf %{buildroot}%{python3_sitearch}/tests

%files
%doc LICENSE README.md CHANGES CREDITS
%{python_sitearch}/icu
%{python_sitearch}/*.*-info
