%global project_commit 2582dfef02e559d7accb7200987910950e74b747
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:               google-daemon
Version:            1.1.3
Release:            2%{?dist}
Summary:            A daemon required for VM integration

License:            ASL 2.0
URL:                https://github.com/GoogleCloudPlatform/compute-image-packages/tree/master/%{name}
Source0:            https://github.com/GoogleCloudPlatform/compute-image-packages/archive/%{project_commit}/%{name}-%{project_commit}.tar.gz
Patch0:             20140619-google-daemon-fix_datadir_path_on_config_and_systemd.patch

BuildArch:          noarch
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
BuildRequires:      systemd
BuildRequires:      systemd-units
BuildRequires:      rsync

%description
Google daemon runs in the background and provides the following services:

    * Creates new accounts based on the instance metadata.
    * Configures ssh to accept the accounts' public keys from 
      the instance metadata.

This package is part of the compute-image-packages


%prep
%autosetup -p1 -n compute-image-packages-%{project_commit}

# remove unneeded files
rm %{name}/README.md
rm -fr %{name}/%{_sysconfdir}/init.d

# fix google_daemon location
mv %{name}%{_datadir}/google/google_daemon %{name}%{_datadir}/google_daemon
rmdir %{name}%{_datadir}/google

# move init to sysconfig
mv %{name}%{_sysconfdir}/init %{name}%{_sysconfdir}/sysconfig


%build


%install
rsync -a %{name}/ %{buildroot}/


%post
%systemd_post google-address-manager.service
%systemd_post google-accounts-manager.service

%preun
%systemd_preun google-address-manager.service
%systemd_preun google-accounts-manager.service

%postun
%systemd_postun_with_restart google-address-manager.service
%systemd_postun_with_restart google-accounts-manager.service


%files
%doc LICENSE
%config %{_unitdir}/google-address-manager.service
%config %{_unitdir}/google-accounts-manager.service
%config(noreplace) %{_sysconfdir}/sysconfig/google-accounts-manager-service.conf
%config(noreplace) %{_sysconfdir}/sysconfig/google-accounts-manager-task.conf
%config(noreplace) %{_sysconfdir}/sysconfig/google-address-manager.conf
%{_datadir}/google_daemon/accounts_manager_daemon.py
%{_datadir}/google_daemon/address_manager.py
%{_datadir}/google_daemon/utils.py
%{_datadir}/google_daemon/manage_accounts.py
%{_datadir}/google_daemon/desired_accounts.py
%{_datadir}/google_daemon/accounts_manager.py
%{_datadir}/google_daemon/accounts.py
%{_datadir}/google_daemon/manage_addresses.py


%changelog
* Thu Jun 19 2014 renich@woralelandia.com - 1.1.3-2
- fix config and systemd path to datadir

* Thu Jun 19 2014 renich@woralelandia.com - 1.1.3-1
- First build

