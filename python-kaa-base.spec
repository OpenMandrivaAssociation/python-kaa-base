%define pkgname kaa-base

Summary: Set of python modules related to media
Name: python-%{pkgname}
Version: 0.6.0
Release: 5
Source0: http://mesh.dl.sourceforge.net/sourceforge/freevo/%{pkgname}-%{version}.tar.gz
License: LGPL
URL: https://sourceforge.net/projects/freevo/
Group: Development/Python

BuildRequires: python-devel
BuildRequires: glib2-devel
Requires: python-sqlite2
Requires: python-libxml2

%description
Kaa base module that implements the common features needed for application 
development, such as mainloop management, timers, signals, callbacks, 
file descriptor monitors, etc.

%prep
%setup -q -n %{pkgname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT 

%files 
%dir %py_platsitedir/kaa
%py_platsitedir/kaa/*
%py_platsitedir/kaa_base-%{version}-*.egg-info



%changelog
* Fri Dec 02 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.6.0-3
+ Revision: 737316
- rebuild
- removed dup requires
- cleaned up spec
- removed mkrel, BuildRoot, clean section & defattr

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.6.0-2mdv2011.0
+ Revision: 591978
- Rebuild

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-1mdv2010.0
+ Revision: 397065
- update to new version 0.6.0

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.4.0-3mdv2009.1
+ Revision: 320592
- rebuild for new python

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-2mdv2009.0
+ Revision: 269027
- rebuild early 2009.0 package (before pixel changes)

* Mon May 12 2008 Crispin Boylan <crisb@mandriva.org> 0.4.0-1mdv2009.0
+ Revision: 206407
- New tar
- New version

* Mon May 12 2008 Crispin Boylan <crisb@mandriva.org> 0.3.0-3mdv2009.0
+ Revision: 206398
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3.0-2mdv2008.1
+ Revision: 171061
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Feb 06 2008 Crispin Boylan <crisb@mandriva.org> 0.3.0-1mdv2008.1
+ Revision: 163254
- New release

* Fri Dec 28 2007 Crispin Boylan <crisb@mandriva.org> 0.2.0-1mdv2008.1
+ Revision: 138782
- New release

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Crispin Boylan <crisb@mandriva.org> 0.1.3-1mdv2008.0
+ Revision: 17243
- New release


* Mon Mar 12 2007 Crispin Boylan <crisb@mandriva.org> 0.1.2-2mdv2007.1
+ Revision: 141743
- Fix requires

* Sun Mar 11 2007 Crispin Boylan <crisb@mandriva.org> 0.1.2-1mdv2007.1
+ Revision: 141398
- Initial Mandriva package.
- Create python-kaa-base

