Summary:	Library integrating clutter with Cairo
Summary(pl.UTF-8):	Biblioteka integrująca clutter z Cairo
Name:		clutter-cairo
Version:	0.1.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.clutter-project.org/sources/clutter-cairo/0.1/%{name}-%{version}.tar.gz
# Source0-md5:	69e65f708399802ffce434716ea7714e
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	cairo-devel
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/clutter-*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
