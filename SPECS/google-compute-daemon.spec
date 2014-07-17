%global project_commit fe29956c2ef34c9892b5e505a46d0fbee5f04562
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global reponame google-daemon

Name:               google-compute-daemon
Version:            1.1.4
Release:            1%{?dist}
Summary:            A daemon required for VM integration

License:            ASL 2.0
URL:                https://github.com/GoogleCloudPlatform/compute-image-packages/tree/master/%{reponame}
Source0:            https://github.com/GoogleCloudPlatform/compute-image-packages/archive/%{project_commit}/%{reponame}-%{project_commit}.tar.gz

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
%autosetup -n compute-image-packages-%{project_commit}

# remove unneeded files
rm %{reponame}/README.md
rm -fr %{reponame}/%{_sysconfdir}/init
rm -fr %{reponame}/%{_sysconfdir}/init.d


%build


%install
rsync -a %{reponame}/ %{buildroot}/


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
%{_datadir}/google/google_daemon/accounts_manager_daemon.py
%{_datadir}/google/google_daemon/address_manager.py
%{_datadir}/google/google_daemon/utils.py
%{_datadir}/google/google_daemon/manage_accounts.py
%{_datadir}/google/google_daemon/desired_accounts.py
%{_datadir}/google/google_daemon/accounts_manager.py
%{_datadir}/google/google_daemon/accounts.py
%{_datadir}/google/google_daemon/manage_addresses.py


%changelog
* Tue Jun 24 2014 renich@woralelandia.com - 1.1.4-1
- updated to v1.1.4
- changed name to fit upstream's

* Tue Jun 24 2014 renich@woralelandia.com - 1.1.3-5
- moved google daemon back to /usr/share/google

* Thu Jun 19 2014 renich@woralelandia.com - 1.1.3-4
- updated source to commit: 2a5ae7492f0172fb4e305c2d556866c35ecee258
- fixes the issue where last user's ssh keys linger

* Thu Jun 19 2014 renich@woralelandia.com - 1.1.3-3
- removed /etc/init files for good

* Thu Jun 19 2014 renich@woralelandia.com - 1.1.3-2
- fix config and systemd path to datadir

* Thu Jun 19 2014 renich@woralelandia.com - 1.1.3-1
- First build

