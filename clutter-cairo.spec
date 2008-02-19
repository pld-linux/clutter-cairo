Summary:	Library integrating clutter with Cairo
Summary(pl.UTF-8):	Biblioteka integrująca clutter z Cairo
Name:		clutter-cairo
Version:	0.6.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.clutter-project.org/sources/clutter-cairo/0.6/%{name}-%{version}.tar.gz
# Source0-md5:	0be2d3c2bb1882b266673f7d9106fc2d
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	clutter-devel >= 0.6.0
BuildRequires:	cairo-devel >= 1.4
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
Requires:	clutter-devel >= 0.6.0
Requires:	cairo-devel >= 1.4

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
%attr(755,root,root) %{_libdir}/libclutter-cairo-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-cairo-*.so
%{_libdir}/libclutter-cairo-*.la
%{_includedir}/clutter-0.6/clutter-cairo
%{_pkgconfigdir}/clutter-cairo-*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libclutter-cairo-*.a
