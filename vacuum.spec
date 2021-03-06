%define cmake_build_dir build

Name:             vacuum
Version:          1.2.5
Release:          1%{dist}
Summary:          Client application for the Jabber network
Summary(ru):      Свободный jabber-клиент

License:          GPLv3
Group:            Applications/Internet
URL:              https://github.com/Vacuum-IM
Source0:          https://github.com/Vacuum-IM/vacuum-im/archive/1.2.5/%{name}-%{version}.tar.gz

BuildRequires:    gcc-c++
BuildRequires:    cmake
BuildRequires:    libidn-devel
BuildRequires:    libXScrnSaver-devel
BuildRequires:    minizip-devel
BuildRequires:    openssl-devel
BuildRequires:    qt-devel
BuildRequires:    qt-webkit-devel
BuildRequires:    qtlockedfile-devel
BuildRequires:    zlib-devel

%description
The core program is just a plugin loader - all functionality is made available
via plugins. This enforces modularity and ensures well defined component
interaction via interfaces. Supported XMPP extension protocols.

%description -l ru
Vacuum-IM - это свободный кросплатформенный Jabber-клиент, написанный на Qt4.
Принципиальное отличие от других кросплатформенных клиентов заключается в
открытой модульной архитектуре, позволяющей гибко настраивать функциональность
под конкретные нужды, а также использовать возможности уже имеющихся модулей
при разработке собственных.

%package devel
Summary:          Shared library and header files for the %{name}
Summary(ru):      Разделяемая библиотека и заголовочные файлы для %{name}
Group:            Development/Libraries
Requires:         %{name} = %{version}

%description devel
The %{name}-devel package contains API documentation for developing %{name}.

%description devel -l ru
Пакет %{name}-devel содержит документацию и API для %{name}.

%prep
%setup -q -n %{name}-im-%{version}
mkdir %{cmake_build_dir}
pushd %{cmake_build_dir}
      %cmake .. -DINSTALL_LIB_DIR=%{_lib} -DCFLAGS="%{optflags}" -DCXXFLAGS="%{optflags}"
popd

%build
pushd %{cmake_build_dir}
      %make_build
popd

%install
pushd %{cmake_build_dir}
      %make_install
popd

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
%doc CHANGELOG AUTHORS README TRANSLATORS
%license COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}/plugins
%{_libdir}/libvacuumutils.so.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/*.png

%files devel
%{_includedir}/%{name}
%{_libdir}/libvacuumutils.so

%changelog
* Tue Jul 14 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.5-1
- 1.2.5 stable release.

* Sun Mar 30 2014 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.2.4-1
- 1.2.4 stable release.

* Tue Dec 24 2013 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.2.3-1
- 1.2.3 stable release.

* Sun Mar 10 2013 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.2.2-1
- 1.2.2 stable release.

* Tue Jan 15 2013 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.2.1-1
- 1.2.1 stable release.

* Wed Aug 01 2012 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.2.0-2
- Fix package naming.

* Wed Aug 01 2012 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.2.0-1.R
- 1.2.0 stable release.

* Wed Dec 28 2011 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.1.1-5.R
- Minor version update.

* Wed Dec 7 2011 Alexey N. Ivanov <alexey.ivanes@gmail.com> - 1.1.1-4.R
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

