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


%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.6-1
+ Revision: 781034
- version update 1.1.6

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-2mdv2011.0
+ Revision: 615519
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.5-1mdv2010.1
+ Revision: 464913
- New version: 1.1.5
  Replace X11-devel requirement for the right packages

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.1.4-3mdv2010.0
+ Revision: 435068
- rebuild

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1.1.4-2mdv2009.0
+ Revision: 269766
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.1.4-1mdv2009.0
+ Revision: 193027
- new release
- new release

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.3-3mdv2008.1
+ Revision: 166455
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.3-2mdv2008.1
+ Revision: 155951
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.1.3-1mdv2008.0
+ Revision: 64407
- new upstream release: 1.1.3
- Import xcompmgr

