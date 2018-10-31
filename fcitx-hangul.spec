Summary: Hangul (Korean IM) plugin for fcitx
Name: fcitx-hangul
Version: 0.3.0
Release: 2
Source0: http://fcitx.googlecode.com/files/%{name}-%{version}.tar.xz
URL: http://fcitx.googlecode.com/
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(libhangul) >= 0.0.12
BuildRequires: intltool

%track
prog %{name} = {
	url = http://code.google.com/p/fcitx/downloads/list
	regex = %name-(__VER__)\.tar\.xz
	version = %{version}
}

%description
Hangul (Korean IM) plugin for fcitx.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %{name}

%files -f %name.lang
%{_libdir}/fcitx/fcitx-hangul.so
%{_datadir}/fcitx/addon/fcitx-hangul.conf
%{_datadir}/fcitx/configdesc/fcitx-hangul.desc
%{_datadir}/fcitx/hangul
%{_datadir}/fcitx/imicon/hangul.png
%{_datadir}/fcitx/inputmethod/hangul.conf
%{_datadir}/icons/hicolor/48x48/status/fcitx-hanja-active.png
%{_datadir}/icons/hicolor/48x48/status/fcitx-hanja-inactive.png
%{_datadir}/icons/hicolor/64x64/apps/fcitx-hangul.png
