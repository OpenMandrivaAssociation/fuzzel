Name:           fuzzel
Version:        1.9.2
Release:        1
Summary:        Application launcher for wlroots based Wayland compositors
 
License:        MIT
URL:            https://codeberg.org/dnkl/fuzzel
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  meson >= 0.58
BuildRequires:  tllist-static

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fcft) >= 3.0.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
#BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
 
%description
Fuzzel is a Wayland-native application launcher, similar to rofi's drun mode.
 
Features:
  * Wayland native
  * Rofi drun-like mode of operation
  * dmenu mode where newline separated entries are read from stdin
  * Emacs key bindings
  * Icons!
  * Remembers frequently launched applications
 
 
%prep
%autosetup -n %{name} -p1
 
 
%build
%meson \
       -Denable-cairo=enabled \ 
       -Dpng-backend=libpng \
       -Dsvg-backend=nanosvg
%meson_build
 
%install
%meson_install
# Will be installed to correct location with rpm macros
rm %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/fish/vendor_completions.d/*.fish
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/*.5*
%{_sysconfdir}/xdg/%{name}/
