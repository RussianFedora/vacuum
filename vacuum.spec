Name:      vacuum
Version:    1.1.1
Release:    4%{dist}.R
Summary:    Client application for the Jabber network
Summary(ru):Свободный jabber-клиент

License:    GPLv3
Group:      Applications/Internet
URL:        http://code.google.com/p/vacuum-im/
Source0:    http://vacuum-im.googlecode.com/files/%{name}-%{version}.tar.xz


BuildRequires:  zlib-devel
BuildRequires:  qt-devel
BuildRequires:  openssl-devel
BuildRequires:  qca2-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  qt-webkit-devel
BuildRequires:  cmake
BuildRequires:  libidn-devel
BuildRequires:  minizip-devel
BuildRequires:  qtlockedfile-devel

Requires:      qca2-ossl


%description
The core program is just a plugin loader - all functionality is made available
via plugins. This enforces modularity and ensures well defined component
interaction via interfaces. Supported XMPP extension protocols.

%description -l ru
Vacuum IM - это свободный кросплатформенный Jabber-клиент, написанный на Qt4.
Принципиальное отличие от других кросплатформенных клиентов заключается в
открытой модульной архитектуре, позволяющей гибко настраивать функциональность
под конкретные нужды, а также использовать возможности уже имеющихся модулей
при разработке собственных.


%package devel
Summary:    Static library and header files for the %{name}
Summary(ru):Статичная библиотека и заголовочные файлы для %{name}
Group:      Development/Libraries
Requires:  %{name} = %{version}


%description devel
The %{name}-devel package contains API documentation for
developing %{name}.

%description devel -l ru
Пакет %{name}-devel содержит документацию и API для %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo \
         -DCMAKE_INSTALL_PREFIX=/usr \
         -DINSTALL_LIB_DIR=%{_lib}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd build
make DESTDIR=%{buildroot} install


#remove unversion doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}

install -D -m644 %{buildroot}%{_datadir}/%{name}/resources/menuicons/shared/mainwindowlogo128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png 
install -D -m644 %{buildroot}%{_datadir}/%{name}/resources/menuicons/shared/mainwindowlogo96.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{name}.png 
install -D -m644 %{buildroot}%{_datadir}/%{name}/resources/menuicons/shared/mainwindowlogo64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png 
install -D -m644 %{buildroot}%{_datadir}/%{name}/resources/menuicons/shared/mainwindowlogo48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png 
install -D -m644 %{buildroot}%{_datadir}/%{name}/resources/menuicons/shared/mainwindowlogo32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png 
install -D -m644 %{buildroot}%{_datadir}/%{name}/resources/menuicons/shared/mainwindowlogo24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png 
install -D -m644 %{buildroot}%{_datadir}/%{name}/resources/menuicons/shared/mainwindowlogo16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png 



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
%{_libdir}/*.so*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/*.png


%files devel
%defattr(-, root, root, 0755)
%{_includedir}/%{name}


%changelog
* Tue Dec 6 2011 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.1.1-4.R
- Fixed work.

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-3.R
- Added description in russian language

* Thu Oct 06 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-2.R
- New build procedure suitable for F16

* Thu Aug 25 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-1.R
- update to 1.1.1
- drop vacuum-1.1.0-system-libs.patch

* Fri Apr 22 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-5.R
- added BR: libidn-devel minizip-devel qtlockedfile-devel

* Fri Apr 22 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-4.R
- use system libs (qtlockedfile, minizip, idn)

* Tue Mar 22 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-3
- build via cmake with devel package
- place icons also in /usr/share/icons

* Tue Mar 22 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-2
- qt-webkit-devel only for fedora >= 14

* Mon Mar 21 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-1
- initial build for Fedora 

