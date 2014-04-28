%global commit 1da451b79f40686de6472d23cf90fdd09fa4dc23
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global _hardened_build 1

Name:           hhvm
Version:        2.3.1
Release:        1%{?dist}
Summary:        HHVM virtual machine, runtime, and JIT for the PHP language

License:        PHP and Zend and BSD
URL:            http://www.hhvm.com/
Source0:        https://github.com/facebook/hhvm/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  ImageMagick-devel%{?_isa}
BuildRequires:  binutils-devel%{?_isa}
BuildRequires:  boost-devel%{?_isa}
BuildRequires:  bzip2-devel%{?_isa}
BuildRequires:  cmake%{?_isa}
BuildRequires:  elfutils-libelf-devel%{?_isa}
BuildRequires:  expat-devel%{?_isa}
BuildRequires:  gd-devel%{?_isa}
BuildRequires:  jemalloc-devel%{?_isa}
BuildRequires:  libc-client%{?_isa}
BuildRequires:  libcap-devel%{?_isa}
BuildRequires:  libcurl-devel%{?_isa}
BuildRequires:  libdwarf-devel%{?_isa}
BuildRequires:  libedit-devel%{?_isa}
BuildRequires:  libevent%{?_isa}
BuildRequires:  libicu-devel%{?_isa}
BuildRequires:  libmcrypt-devel%{?_isa}
BuildRequires:  libmemcached-devel%{?_isa}
BuildRequires:  libtool%{?_isa}
BuildRequires:  libxml2-devel%{?_isa}
BuildRequires:  libxslt-devel%{?_isa}
BuildRequires:  mariadb-devel%{?_isa}
BuildRequires:  memcached%{?_isa}
BuildRequires:  ocaml%{?_isa}
BuildRequires:  oniguruma-devel%{?_isa}
BuildRequires:  openldap-devel%{?_isa}
BuildRequires:  pam-devel%{?_isa}
BuildRequires:  pcre-devel%{?_isa}
BuildRequires:  pigz%{?_isa}
BuildRequires:  tbb-devel%{?_isa}
BuildRequires:  uw-imap-devel%{?_isa}
BuildRequires:  wget%{?_isa}
Requires:       glog%{?_isa}

%description
HHVM is an open-source virtual machine designed for executing programs written in Hack and PHP. HHVM uses a just-in-time (JIT)
compilation approach to achieve superior performance while maintaining the development flexibility that PHP provides.


%prep
%setup -qn %{name}-%{commit}


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%check
ctest


%files
%doc



%changelog
* Mon Apr 28 2014 Renich Bon Ciric <renich@woralelandia.com> - 2.3.1-1
- Initial package build.
