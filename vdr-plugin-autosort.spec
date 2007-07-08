
%define plugin	autosort
%define name	vdr-plugin-%plugin
%define version	0.0.10
%define rel	11

Summary:	VDR plugin: Channel Autosort
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.copypointburscheid.de/linux/autosort.htm
Source:		http://www.copypointburscheid.de/linux/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin performs a presortion of new channels.

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -D -m644 autosort.conf %{buildroot}%{_vdr_plugin_cfgdir}/autosort.conf

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY
%config(noreplace) %{_vdr_plugin_cfgdir}/autosort.conf


