Name:		xcompmgr
Version:	1.1.3
Release:	%mkrel 2
Summary:	Sample X Compositing Manager
Source:		http://xapps.freedesktop.org/release/%{name}-%{version}.tar.gz
URL:		http://xapps.freedesktop.org
License:	MIT
Group:		System/X11
BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libxdamage-devel		>= 1.1.1
BuildRequires: libxcomposite-devel	>= 0.4.0
BuildRequires: libxrender-devel		>= 0.9.4

BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Sample X Compositing Manager.

%prep
%setup -q

%build
%configure
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
