Name:		xcompmgr
Version:	1.1.7
Release:	1
Summary:	Sample X Compositing Manager
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
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
%configure
%make

%install
%makeinstall

%files
%doc ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
