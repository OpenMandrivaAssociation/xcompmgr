%define name   xcompmgr
%define version        1.1.6
%define release        1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Sample X Compositing Manager
Source0:	http://xapps.freedesktop.org/release/%{name}-%{version}.tar.gz
URL:		http://xapps.freedesktop.org
License:	MIT
Group:		System/X11
BuildRequires:  libxcomposite-devel
BuildRequires:  libxfixes-devel
BuildRequires:  libxdamage-devel
BuildRequires:  libxrender-devel
BuildRequires:  libxext-devel

%description
Sample X Compositing Manager.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall

%files
%doc ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
