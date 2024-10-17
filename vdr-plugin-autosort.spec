%define plugin	autosort

Summary:	VDR plugin: Channel Autosort
Name:		vdr-plugin-%plugin
Version:	0.1.3
Release:	7
Group:		Video
License:	GPL
URL:		https://www.copypointburscheid.de/linux/autosort.htm
Source:		http://www.copypointburscheid.de/linux/vdr-%plugin-%version.tgz
Patch0:		autosort-90_ConfigDir.dpatch
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
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 scripts/*.pl %{buildroot}%{_bindir}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY examples
%{_bindir}/createopengroups.pl



%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.3-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.3-3mdv2009.1
+ Revision: 359284
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3-2mdv2009.0
+ Revision: 197899
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3-1mdv2009.0
+ Revision: 197630
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- fix too early configdir invocation (P0 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.10-14mdv2008.1
+ Revision: 145027
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.10-13mdv2008.1
+ Revision: 144978
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.10-12mdv2008.1
+ Revision: 103059
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.10-11mdv2008.0
+ Revision: 49968
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.10-10mdv2008.0
+ Revision: 42055
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.10-9mdv2008.0
+ Revision: 22704
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-8mdv2007.0
+ Revision: 90890
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-7mdv2007.1
+ Revision: 73950
- rebuild for new vdr
- Import vdr-plugin-autosort

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-2mdv2007.0
- use _ prefix for system path macros

* Sun Jun 11 2006 Anssi Hannula <anssi@mandriva.org> 0.0.10-1mdv2007.0
- initial Mandriva release

