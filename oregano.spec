Summary:	Oregano - schematic capture and simulation of electrical circuits
Summary(it):	Oregano - disegno e simulazione di circuiti elettrici
Summary(pl):	Oregano - tworzenie schematów i symulacja obwodów elektrycznych
Summary(sv):	Oregano - kretsschemariting och simulering av elektriska kretsar
Name:		oregano
Version:	0.23
Release:	9
License:	GPL
Group:		Applications/Engineering
Source0:	ftp://ftp.codefactory.se/pub/software/oregano/%{name}-%{version}.tar.gz
# Source0-md5:	226b84622dd1b877ee87228ba74d68d1
Patch0:		%{name}-desktop.patch
URL:		http://people.imendio.com/richard/oregano/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-print-devel >= 0.30
BuildRequires:	libglade-gnome-devel >= 0.8
BuildRequires:	libtool
BuildRequires:	libxml-devel >= 1.8.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oregano is intended to be an application for schematic capture and
simulation of electrical circuits. The actual simulation is performed
by Berkeley Spice. Oregano can still be used without Spice, for
schematic capture.

%description -l pl
Oregano jest aplikacj± do tworzenia schematów i symulacji obwodów
elektrycznych. W³a¶ciwa symulacja jest robiona przez Berkeley Spice.
Bez Spice nadal mo¿na u¿ywaæ Oregano - do rysowania schematów.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir} \
	samplesdir=%{_examplesdir}/%{name}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/oregano.desktop
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_datadir}/oregano
%{_examplesdir}/%{name}
