%define name	xcompmgr
%define version	1.1.3
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Sample X Compositing Manager
Source:		http://xapps.freedesktop.org/release/%{name}-%{version}.tar.gz
URL:		http://xapps.freedesktop.org
License:	GPL
Group:		System/X11
BuildRequires:  X11-devel

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
%doc ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
