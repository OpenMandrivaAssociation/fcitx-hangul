%define beta %{nil}
%define scmrev %{nil}

Name: fcitx-hangul
Version: 0.2.1
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 6
Source0: http://fcitx.googlecode.com/files/%{name}-%{version}.tar.xz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: Hangul (Korean IM) plugin for fcitx
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
Hangul (Korean IM) plugin for fcitx

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %name

%files -f %name.lang
%_libdir/fcitx/fcitx-hangul.so
%_datadir/fcitx/addon/fcitx-hangul.conf
%_datadir/fcitx/configdesc/fcitx-hangul.desc
%_datadir/fcitx/hangul
%_datadir/fcitx/imicon/hangul.png
%_datadir/fcitx/inputmethod/hangul.conf
%_datadir/icons/hicolor/48x48/status/fcitx-hanja-active.png
%_datadir/icons/hicolor/48x48/status/fcitx-hanja-inactive.png
%_datadir/icons/hicolor/64x64/apps/fcitx-hangul.png
