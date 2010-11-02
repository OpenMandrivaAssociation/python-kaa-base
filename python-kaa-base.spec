%define pkgname kaa-base

Summary: Set of python modules related to media
Name: python-%{pkgname}
Version: 0.6.0
Release: %mkrel 2
Source0: http://mesh.dl.sourceforge.net/sourceforge/freevo/%{pkgname}-%{version}.tar.gz
License: LGPL
URL: http://sourceforge.net/projects/freevo/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: python-devel
BuildRequires: glib2-devel
Requires: glib2
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

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%dir %py_platsitedir/kaa
%py_platsitedir/kaa/*
%py_platsitedir/kaa_base-%{version}-*.egg-info


