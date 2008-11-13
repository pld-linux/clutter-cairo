Summary:	Library integrating clutter with Cairo
Summary(pl.UTF-8):	Biblioteka integrująca clutter z Cairo
Name:		clutter-cairo
Version:	0.8.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.clutter-project.org/sources/clutter-cairo/0.8/%{name}-%{version}.tar.gz
# Source0-md5:	c3bfae082d007be37d9725e5e7b4a30b
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel >= 1.4
BuildRequires:	clutter-devel >= 0.8.2
BuildRequires:	clutter-devel < 0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library integrating clutter with Cairo.

%description -l pl.UTF-8
Biblioteka integrująca clutter z Cairo.

%package devel
Summary:	Header files for clutter-cairo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter-cairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.4
Requires:	clutter-devel >= 0.8.2
Requires:	clutter-devel < 0.9

%description devel
Header files for clutter-cairo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter-cairo.

%package static
Summary:	Static clutter-cairo library
Summary(pl.UTF-8):	Statyczna biblioteka clutter-cairo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static clutter-cairo library.

%description static -l pl.UTF-8
Statyczna biblioteka clutter-cairo.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libclutter-cairo-0.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclutter-cairo-0.8.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-cairo-0.8.so
%{_libdir}/libclutter-cairo-0.8.la
%{_includedir}/clutter-0.8/clutter-cairo
%{_pkgconfigdir}/clutter-cairo-0.8.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-cairo-0.8.a
