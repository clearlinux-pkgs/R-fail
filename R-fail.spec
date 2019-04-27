#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fail
Version  : 1.3
Release  : 13
URL      : https://cran.r-project.org/src/contrib/fail_1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fail_1.3.tar.gz
Summary  : File Abstraction Interface Layer (FAIL)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-assertthat
Requires: R-cli
Requires: R-withr
BuildRequires : R-BBmisc
BuildRequires : R-assertthat
BuildRequires : R-backports
BuildRequires : R-checkmate
BuildRequires : R-cli
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
in a key-value fashion.

%prep
%setup -q -c -n fail

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552836464

%install
export SOURCE_DATE_EPOCH=1552836464
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fail
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fail
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fail
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  fail || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fail/DESCRIPTION
/usr/lib64/R/library/fail/INDEX
/usr/lib64/R/library/fail/LICENSE
/usr/lib64/R/library/fail/Meta/Rd.rds
/usr/lib64/R/library/fail/Meta/features.rds
/usr/lib64/R/library/fail/Meta/hsearch.rds
/usr/lib64/R/library/fail/Meta/links.rds
/usr/lib64/R/library/fail/Meta/nsInfo.rds
/usr/lib64/R/library/fail/Meta/package.rds
/usr/lib64/R/library/fail/NAMESPACE
/usr/lib64/R/library/fail/NEWS
/usr/lib64/R/library/fail/R/fail
/usr/lib64/R/library/fail/R/fail.rdb
/usr/lib64/R/library/fail/R/fail.rdx
/usr/lib64/R/library/fail/help/AnIndex
/usr/lib64/R/library/fail/help/aliases.rds
/usr/lib64/R/library/fail/help/fail.rdb
/usr/lib64/R/library/fail/help/fail.rdx
/usr/lib64/R/library/fail/help/paths.rds
/usr/lib64/R/library/fail/html/00Index.html
/usr/lib64/R/library/fail/html/R.css
/usr/lib64/R/library/fail/tests/test_all.R
/usr/lib64/R/library/fail/tests/testthat/test_apply.R
/usr/lib64/R/library/fail/tests/testthat/test_as_list.R
/usr/lib64/R/library/fail/tests/testthat/test_assign.R
/usr/lib64/R/library/fail/tests/testthat/test_constructor.R
/usr/lib64/R/library/fail/tests/testthat/test_get_put.R
/usr/lib64/R/library/fail/tests/testthat/test_mapply.R
/usr/lib64/R/library/fail/tests/testthat/test_remove.R
/usr/lib64/R/library/fail/tests/testthat/test_sail.R
/usr/lib64/R/library/fail/tests/testthat/test_size.R
