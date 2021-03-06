#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-molecule_docker
Version  : 2.0.0
Release  : 7
URL      : https://files.pythonhosted.org/packages/65/ce/e8ffe18bef0720157bdc22a58567a86792957d3ab3d6b956c0f488e33561/molecule-docker-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/ce/e8ffe18bef0720157bdc22a58567a86792957d3ab3d6b956c0f488e33561/molecule-docker-2.0.0.tar.gz
Summary  : Molecule aids in the development and testing of Ansible roles
Group    : Development/Tools
License  : MIT
Requires: pypi-molecule_docker-license = %{version}-%{release}
Requires: pypi-molecule_docker-python = %{version}-%{release}
Requires: pypi-molecule_docker-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docker)
BuildRequires : pypi(molecule)
BuildRequires : pypi(pip)
BuildRequires : pypi(py)
BuildRequires : pypi(requests)
BuildRequires : pypi(selinux)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
**********************
Molecule Docker Plugin
**********************
.. image:: https://badge.fury.io/py/molecule-docker.svg
:target: https://badge.fury.io/py/molecule-docker
:alt: PyPI Package

%package license
Summary: license components for the pypi-molecule_docker package.
Group: Default

%description license
license components for the pypi-molecule_docker package.


%package python
Summary: python components for the pypi-molecule_docker package.
Group: Default
Requires: pypi-molecule_docker-python3 = %{version}-%{release}

%description python
python components for the pypi-molecule_docker package.


%package python3
Summary: python3 components for the pypi-molecule_docker package.
Group: Default
Requires: python3-core
Provides: pypi(molecule_docker)
Requires: pypi(docker)
Requires: pypi(molecule)
Requires: pypi(requests)
Requires: pypi(selinux)

%description python3
python3 components for the pypi-molecule_docker package.


%prep
%setup -q -n molecule-docker-2.0.0
cd %{_builddir}/molecule-docker-2.0.0
pushd ..
cp -a molecule-docker-2.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658155648
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-molecule_docker
cp %{_builddir}/molecule-docker-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-molecule_docker/82314adfc4f5f364b3443f5df8a3393fd2121964
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-molecule_docker/82314adfc4f5f364b3443f5df8a3393fd2121964

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
