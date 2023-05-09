Summary:	Server99 Anaconda Config Files
Name:     	server99-anaconda
Version:	1.0
Release:	1%{?dist}
License:	GPLv2+ and MIT
URL: 		https://github.com/Server99-industries/server99-anaconda

BuildArch: 	noarch
Requires: 	anaconda
Requires:	server99-logos
Source0: server99-text-mode.ks

%description
Server99 Anaconda Config Files

%prep
%build
cat > Server99.conf <<EOF   
# Anaconda configuration file for Server99.

[Profile]
# Define the profile.
profile_id = server99
base_profile = fedora-server

[Profile Detection]
# Match os-release values.
os_id = server99
EOF

%install
mkdir -p %{buildroot}%{_sysconfdir}/anaconda/profile.d
install -m 655 Server99.conf %{buildroot}%{_sysconfdir}/anaconda/profile.d/Server99.conf
mkdir -p %{buildroot}%{_datadir}/anaconda/post-scripts
install -m 655 %{SOURCE0} %{buildroot}%{_datadir}/anaconda/post-scripts/server99-text-mode.ks

%files
%{_sysconfdir}/anaconda/profile.d/Server99.conf
%{_datadir}/anaconda/post-scripts/server99-text-mode.ks


%changelog
* Tue May 09 2023 Core-i99
- Package created

