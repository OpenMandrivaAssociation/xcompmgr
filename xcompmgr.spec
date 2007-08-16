%define name	xcompmgr
%define version	1.1.1
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Sample X Compositing Manager
Source:		http://freedesktop.org/xapps/release/%{name}-%{version}.tar.bz2
URL:		http://freedesktop.org/Software/xapps
License:	GPL
Group:		System/X11
BuildRequires:  X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Sample X Compositing Manager.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog INSTALL
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
