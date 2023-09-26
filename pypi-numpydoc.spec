#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-numpydoc
Version  : 1.6.0
Release  : 63
URL      : https://files.pythonhosted.org/packages/5f/ed/5ca4b2e90f4b0781f5fac49cdb2947cf719b6d289eedb67e8b1a63d019e3/numpydoc-1.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/ed/5ca4b2e90f4b0781f5fac49cdb2947cf719b6d289eedb67e8b1a63d019e3/numpydoc-1.6.0.tar.gz
Summary  : Sphinx extension to support docstrings in Numpy format
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-numpydoc-bin = %{version}-%{release}
Requires: pypi-numpydoc-license = %{version}-%{release}
Requires: pypi-numpydoc-python = %{version}-%{release}
Requires: pypi-numpydoc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(nose)
BuildRequires : pypi(pytest)
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=====================================
numpydoc -- Numpy's Sphinx extensions
=====================================

%package bin
Summary: bin components for the pypi-numpydoc package.
Group: Binaries
Requires: pypi-numpydoc-license = %{version}-%{release}

%description bin
bin components for the pypi-numpydoc package.


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
Requires: pypi(tabulate)

%description python3
python3 components for the pypi-numpydoc package.


%prep
%setup -q -n numpydoc-1.6.0
cd %{_builddir}/numpydoc-1.6.0
pushd ..
cp -a numpydoc-1.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695766503
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . Jinja2
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . Jinja2
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-numpydoc
cp %{_builddir}/numpydoc-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-numpydoc/121809b54d1ff9d839b72546078700f1d44a50ba || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
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
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/validate-docstrings

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-numpydoc/121809b54d1ff9d839b72546078700f1d44a50ba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
