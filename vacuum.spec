Summary:	Client application for the Jabber network
Name:		vacuum
Version:	1.1.0
Release:	3%{dist}

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
BuildRequires:	cmake

Requires:	qca2-ossl


%description
The core program is just a plugin loader - all functionality is made available
via plugins. This enforces modularity and ensures well defined component
interaction via interfaces. Supported XMPP extension protocols.


%package devel
Summary:	Static library and header files for the %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}


%description devel
The %{name}-devel package contains API documentation for
developing %{name}.


%prep
%setup -q


%build
mkdir build
cd build
%{cmake_kde4} .. \
	-DINSTALL_LIB_DIR=%{_lib}

make %{?_smp_mflags}
cd -


%install
make DESTDIR=%{buildroot} install -C build

# remove unversion doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}

for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 128x128 ; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size/apps
  install -m644 resources/menuicons/shared/%{name}.png \
	%{buildroot}%{_datadir}/icons/hicolor/$size/apps/
done


%post
/sbin/ldconfig
touch --no-create /usr/share/icons/hicolor &>/dev/null || :


%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    touch --no-create /usr/share/icons/hicolor &>/dev/null
    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :


%files
%defattr(-, root, root, 0755)
%doc COPYING CHANGELOG AUTHORS README TRANSLATORS
%{_bindir}/%{name}
%{_libdir}/%{name}/plugins
%{_libdir}/*.so.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/*.png


%files devel
%defattr(-, root, root, 0755)
%{_includedir}/%{name}
%{_libdir}/*.so


%changelog
* Tue Mar 22 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-3
- build via cmake with devel package
- place icons also in /usr/share/icons

* Tue Mar 22 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-2
- qt-webkit-devel only for fedora >= 14

* Mon Mar 21 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-1
- initial build for Fedora 
