# hhvm
%global hhvm-commit 1da451b79f40686de6472d23cf90fdd09fa4dc23
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# hardened build
%global _hardened_build 1

Name:           hhvm
Version:        3.0.1
Release:        1%{?dist}
Summary:        HHVM virtual machine, runtime, and JIT for the PHP language

License:        PHP and Zend and BSD
URL:            http://www.hhvm.com/
Source0:        https://github.com/facebook/hhvm/archive/%{hhvm-commit}/%{name}-%{hhvm-commit}.tar.gz
Source1:        https://github.com/facebook/folly/archive/%{folly-commit}/%{name}-%{folly-commit}.tar.gz

BuildRequires:	binutils-devel%{?_isa}
BuildRequires:	boost-devel%{?_isa}
BuildRequires:	bzip2-devel%{?_isa}
BuildRequires:	chrpath%{?_isa}
BuildRequires:	cmake%{?_isa}
BuildRequires:	elfutils-libelf-devel%{?_isa}
BuildRequires:	expat-devel%{?_isa}
BuildRequires:	freetype-devel%{?_isa}
BuildRequires:	gcc%{?_isa}
BuildRequires:	glibc-devel%{?_isa}
BuildRequires:	glog-devel%{?_isa}
BuildRequires:	ImageMagick-devel%{?_isa}
BuildRequires:	jemalloc-devel%{?_isa}
BuildRequires:	libcap-devel%{?_isa}
BuildRequires:	libcurl-devel%{?_isa}
BuildRequires:	libdwarf-devel%{?_isa}
BuildRequires:	libedit-devel%{?_isa}
BuildRequires:	libevent-devel%{?_isa}
BuildRequires:	libicu-devel%{?_isa}
BuildRequires:	libjpeg-devel%{?_isa}
BuildRequires:	libmcrypt-devel%{?_isa}
BuildRequires:	libmemcached-devel%{?_isa}
BuildRequires:	libpng-devel%{?_isa}
BuildRequires:	libxml2-devel%{?_isa}
BuildRequires:	libxslt-devel%{?_isa}
BuildRequires:	mariadb-devel%{?_isa}
BuildRequires:	ncurses-devel%{?_isa}
BuildRequires:	ocaml%{?_isa}
BuildRequires:	oniguruma-devel%{?_isa}
BuildRequires:	openldap-devel%{?_isa}
BuildRequires:	openssl-devel%{?_isa}
BuildRequires:	pam-devel%{?_isa}
BuildRequires:	pcre-devel%{?_isa}
BuildRequires:	pigz%{?_isa}
BuildRequires:	readline-devel%{?_isa}
BuildRequires:	tbb-devel%{?_isa}
BuildRequires:	uw-imap-devel%{?_isa}
BuildRequires:	zlib-devel%{?_isa}

Requires:	ImageMagick%{?_isa}
Requires:	libxml2%{?_isa}
Requires:	libxslt%{?_isa}
Requires:	unixODBC%{?_isa}
Requires:	wget%{?_isa}

%description
HHVM is an open-source virtual machine designed for executing programs written in Hack and PHP. HHVM uses a just-in-time (JIT)
compilation approach to achieve superior performance while maintaining the development flexibility that PHP provides.


%prep
%setup -qn %{name}-%{hhvm-commit}


%build
LDFLAGS="-Wl,-z,relro -z now"
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
* Sun May 04 2014 Francisco Garibaldi <francisco.garibaldi@gmail.com> - 3.0.1-1
- Correction of LDFLAGS to prevent creation of Possition Independent Executables. Correct compilation problem with LibEvent test
- Correction of version of hhvm used
* Mon Apr 28 2014 Renich Bon Ciric <renich@woralelandia.com> - 2.3.1-1
- Initial package build.
