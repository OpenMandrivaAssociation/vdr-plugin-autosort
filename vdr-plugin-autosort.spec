
%define plugin	autosort
%define name	vdr-plugin-%plugin
%define version	0.1.3
%define rel	2

Summary:	VDR plugin: Channel Autosort
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.copypointburscheid.de/linux/autosort.htm
Source:		http://www.copypointburscheid.de/linux/vdr-%plugin-%version.tgz
Patch0:		autosort-90_ConfigDir.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin performs a presortion of new channels.

%prep
%setup -q -n %plugin-%version
sed -i 's,/video,%{_vdr_videodir},' scripts/*.pl README*
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 scripts/*.pl %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY examples
%{_bindir}/createopengroups.pl

