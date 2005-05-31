Summary:	Oregano - schematic capture and simulation of electrical circuits
Summary(it):	Oregano - disegno e simulazione di circuiti elettrici
Summary(pl):	Oregano - tworzenie schematów i symulacja obwodów elektrycznych
Summary(sv):	Oregano - kretsschemariting och simulering av elektriska kretsar
Name:		oregano
Version:	0.40.4
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://gforge.lug.fi.uba.ar/frs/download.php/61/%{name}-%{version}.tar.gz
# Source0-md5:	12c285faca69cbaf97cc1f5242a9a99b
#Patch0:		%{name}-desktop.patch
URL:		http://arrakis.gforge.lug.fi.uba.ar/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel >= 2.6
BuildRequires:	libgnomeprint-devel >= 2.10
BuildRequires:	libgnomeprintui-devel >= 2.10
BuildRequires:	libgnome >= 2.10
BuildRequires:	gnome-common >= 2.6
BuildRequires:	gtksourceview-devel >= 1.2
BuildRequires:	popt-devel >= 1.10
BuildRequires:	cairo-devel >= 0.4
BuildRequires:	libpixman-devel >= 0.1.4
BuildRequires:	libtool

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
#%patch0 -p1

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
