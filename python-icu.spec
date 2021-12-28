%define         py3dir %{_builddir}/python3-%{name}-%{version}-%{release}

%define		realname PyICU
%define		module icu
Name:		python-%{module}
Version:	2.8
Release:	1
Summary:	Python extension wrapping IBM's ICU C++ libraries
Group:		Development/Python
License:	MIT
URL:		https://gitlab.pyicu.org/main/pyicu
Source0:	https://pypi.python.org/packages/source/P/%{realname}/%{realname}-%{version}.tar.gz
Patch1:		0001-disable-failing-test.patch
BuildRequires:	python3-devel
BuildRequires:	python-setuptools
BuildRequires:	icu-devel
%rename	python3-icu

%description
PyICU is Python extension wrapping IBM's International Components
for Unicode C++ library (ICU). ICU is a mature, widely used set of
C/C++ and Java libraries providing Unicode and Globalization support
for software applications. ICU is widely portable and gives applications
the same results on all platforms and between C/C++ and Javasoftware.

%package -n python2-%{module}
Summary:	Python extension wrapping IBM's ICU C++ libraries
Group:		Development/Python
BuildRequires:	python2-devel
BuildRequires:	python2dist(setuptools)

%description -n python2-%{module}
PyICU is Python extension wrapping IBM's International Components
for Unicode C++ library (ICU). ICU is a mature, widely used set of
C/C++ and Java libraries providing Unicode and Globalization support
for software applications. ICU is widely portable and gives applications
the same results on all platforms and between C/C++ and Javasoftware.

%prep
%setup -q -n %{realname}-%{version}
%autopatch -p1

cp -a . %{py3dir}

%build
%{__python2} setup.py build

pushd %{py3dir}
%{__python3} setup.py build
popd

%check
#%{__python2} setup.py test

pushd %{py3dir}
%{__python3} setup.py test
popd

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
# Remove tests
rm -rf %{buildroot}%{python_sitearch}/tests

pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
# Remove tests
rm -rf %{buildroot}%{python3_sitearch}/tests
popd

%files
%doc LICENSE README.md CHANGES CREDITS
%{python_sitearch}/

%files -n python2-%{module}
%doc LICENSE README.md CHANGES CREDITS
%{python2_sitearch}/

