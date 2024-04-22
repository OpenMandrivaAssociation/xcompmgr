Name:		xcompmgr
Version:	1.1.9
Release:	1
Summary:	Sample X Compositing Manager
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
URL:		https://xapps.freedesktop.org
License:	MIT
Group:		System/X11
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)

%description
Sample X Compositing Manager.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
