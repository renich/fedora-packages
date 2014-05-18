# commit
%global commit cc928c85325e3bdb869d9df50f9f35b08e18d52f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# hardened build
%global _hardened_build 1

Name:           glb
Version:        1.0.1
Release:        1%{?dist}
Summary:        A simple TCP connection balancer made with scalability and performance in mind.

License:        GPLv2
URL:            https://github.com/codership/%{name}
Source0:        https://github.com/codership/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  libtool%{?_isa}

%description
A simple TCP connection balancer made with scalability and performance in mind. It was inspired by pen, but unlike pen its
functionality is limited only to balancing generic TCP connections.

Features:
* list of backend servers is configurable in runtime.
* supports server "draining", i.e. does not allocate new connections to server, but does not kill existing ones, waiting for them to end gracefully.
* can use epoll API provided by Linux version 2.6 and higher for ultimate routing performance.
* glbd is multithreaded, so it can utilize multiple CPU cores. Also, if your OS does not support epoll API, consider using several threads even on a single core machine as it will lessen poll() overhead proportionally and can improve overall performance by a factor of 2 or more.
* optional watchdog module can monitor destinations and adjust routing table automatically.

libglb is a shared library that provides 0-effort connection balancing to any Linux application that uses standard libc connect()
call by overloading that function in runtime. No other program functionality is affected and no program modification or
recompilation is needed. See below for details.


%prep
%setup -qn %{name}-%{commit}


%build
./bootstrap.sh
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%doc


%changelog
* Sun May 18 2014 Renich Bon Ciric
- initial packaging
