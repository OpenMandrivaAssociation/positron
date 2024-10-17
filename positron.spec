%define name positron
%define version 1.1
%define release %mkrel 4

Summary: A synchronization manager for the Neuros Audio Computer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: Sound
BuildArchitectures: noarch
Url: https://www.xiph.org/positron/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: pyogg, pyvorbis, python-devel

%description
positron is the synchronization manager for the Neuros Audio Computer.
It supports adding, removing, and syncing files to/from the Neuros
device.

%prep
%setup

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/positron
%{_libdir}/python%pyver/site-packages/positron/
%{_defaultdocdir}/positron/*
%{_mandir}/man1/*

