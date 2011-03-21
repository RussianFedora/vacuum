Summary:	Client application for the Jabber network
Name:		vacuum
Version:	1.1.0
Release:	2%{dist}

License:	GPLv3
Group:		Applications/Internet
URL:		http://code.google.com/p/vacuum-im/
Source0:	http://vacuum-im.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:	zlib-devel 
BuildRequires:	qt-devel 
BuildRequires:	openssl-devel
BuildRequires:	qca2-devel
BuildRequires:	libXScrnSaver-devel
%if 0%{?fedora} >= 14
BuildRequires:	qt-webkit-devel
%endif

Requires:	qca2-ossl


%description
The core program is just a plugin loader - all functionality is made available
via plugins. This enforces modularity and ensures well defined component
interaction via interfaces. Supported XMPP extension protocols.


%prep
%setup -q


%build
qmake-qt4 INSTALL_PREFIX=/usr INSTALL_LIB_DIR=%{_lib} -recursive vacuum.pro
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

# remove unversion doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}
# remove devel link
rm -f %{buildroot}/%{_libdir}/libvacuumutils.so


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc COPYING CHANGELOG AUTHORS README TRANSLATORS
%{_bindir}/%{name}
%{_libdir}/%{name}/plugins
%{_libdir}/*.so.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Tue Mar 22 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-2
- qt-webkit-devel only for fedora >= 14

* Mon Mar 21 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-1
- initial build for Fedora 
