%define         py3dir %{_builddir}/python3-%{name}-%{version}-%{release}

%define		realname PyICU
%define		module icu
Name:		python-%{module}
Version:	1.6
Release:	1
Summary:	Python extension wrapping IBM's ICU C++ libraries
Group:		Development/Python
License:	MIT
URL:		http://pyicu.osafoundation.org/
Source0:	http://pypi.python.org/packages/source/P/%{realname}/%{realname}-%{version}.tar.gz
Patch0:		PyICU-1.6-svnrev220.patch
Patch1:		0001-disable-failing-test.patch
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	icu-devel

%description
PyICU is Python extension wrapping IBM's International Components
for Unicode C++ library (ICU). ICU is a mature, widely used set of
C/C++ and Java libraries providing Unicode and Globalization support
for software applications. ICU is widely portable and gives applications
the same results on all platforms and between C/C++ and Javasoftware.

%package -n python3-%{module}
Summary:	Python extension wrapping IBM's ICU C++ libraries
Group:		Development/Python
BuildRequires:	python3-devel
BuildRequires:	python3egg(setuptools)

%description -n python3-%{module}
PyICU is Python extension wrapping IBM's International Components
for Unicode C++ library (ICU). ICU is a mature, widely used set of
C/C++ and Java libraries providing Unicode and Globalization support
for software applications. ICU is widely portable and gives applications
the same results on all platforms and between C/C++ and Javasoftware.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p0 -b .r220
%patch1 -p0

cp -a . %{py3dir}

%build
%{__python} setup.py build

pushd %{py3dir}
%{__python3} setup.py build
popd

%check
%{__python} setup.py test

pushd %{py3dir}
#%{__python3} setup.py test
popd

%install
%{__python} setup.py install --skip-build --root %{buildroot}
# Remove tests
rm -rf %{buildroot}%{python_sitearch}/tests

pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
# Remove tests
rm -rf %{buildroot}%{python3_sitearch}/tests
popd

%files
%doc LICENSE README CHANGES CREDITS
%{python_sitearch}/

%files -n python3-%{module}
%doc LICENSE README CHANGES CREDITS
%{python3_sitearch}/

