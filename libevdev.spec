Summary:	Handler library for evdev events
Name:		libevdev
Version:	1.4
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/libevdev/%{name}-%{version}.tar.xz
# Source0-md5:	eba88e8897fd296f3bb746bc39da18b3
URL:		http://www.freedesktop.org/wiki/Software/libevdev/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	check-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Handler library for evdev events.

%package devel
Summary:	Header files for libevdev library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libevdev library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/libevdev-tweak-device
%attr(755,root,root) %{_bindir}/mouse-dpi-tool
%attr(755,root,root) %{_bindir}/touchpad-edge-detector
%attr(755,root,root) %ghost %{_libdir}/libevdev.so.2
%attr(755,root,root) %{_libdir}/libevdev.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevdev.so
%{_includedir}/libevdev-1.0
%{_pkgconfigdir}/libevdev.pc
%{_mandir}/man3/libevdev.3*

