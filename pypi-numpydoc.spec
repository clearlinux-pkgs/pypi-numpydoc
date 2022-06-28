#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-numpydoc
Version  : 1.4.0
Release  : 53
URL      : https://files.pythonhosted.org/packages/d6/fb/dce2345676623f26ea9a8c9a8c3485a4ea232cb598a6f5e8be8d32947bed/numpydoc-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/fb/dce2345676623f26ea9a8c9a8c3485a4ea232cb598a6f5e8be8d32947bed/numpydoc-1.4.0.tar.gz
Summary  : Sphinx extension to support docstrings in Numpy format
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-numpydoc-license = %{version}-%{release}
Requires: pypi-numpydoc-python = %{version}-%{release}
Requires: pypi-numpydoc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jinja2)
BuildRequires : pypi(nose)
BuildRequires : pypi(pytest)
BuildRequires : pypi(sphinx)

%description
=====================================
numpydoc -- Numpy's Sphinx extensions
=====================================

%package license
Summary: license components for the pypi-numpydoc package.
Group: Default

%description license
license components for the pypi-numpydoc package.


%package python
Summary: python components for the pypi-numpydoc package.
Group: Default
Requires: pypi-numpydoc-python3 = %{version}-%{release}

%description python
python components for the pypi-numpydoc package.


%package python3
Summary: python3 components for the pypi-numpydoc package.
Group: Default
Requires: python3-core
Provides: pypi(numpydoc)
Requires: pypi(jinja2)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-numpydoc package.


%prep
%setup -q -n numpydoc-1.4.0
cd %{_builddir}/numpydoc-1.4.0
pushd ..
cp -a numpydoc-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656390853
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . Jinja2
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . Jinja2
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-numpydoc
cp %{_builddir}/numpydoc-1.4.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpydoc/0a9bbd882e5acb52126c545e871416f67b99e445
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} Jinja2
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-numpydoc/0a9bbd882e5acb52126c545e871416f67b99e445

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
