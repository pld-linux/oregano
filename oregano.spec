Summary:	Oregano - schematic capture and simulation of electrical circuits
Summary(it.UTF-8):	Oregano - disegno e simulazione di circuiti elettrici
Summary(pl.UTF-8):	Oregano - tworzenie schematów i symulacja obwodów elektrycznych
Summary(sv.UTF-8):	Oregano - kretsschemariting och simulering av elektriska kretsar
Name:		oregano
Version:	0.69.0
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://gforge.lug.fi.uba.ar/frs/download.php/86/%{name}-%{version}.tar.gz
# Source0-md5:	f98abc5c79cc733b49cd07995afc9c1e
Patch0:		%{name}-desktop.patch
URL:		http://arrakis.gforge.lug.fi.uba.ar/
BuildRequires:	libxml-devel >= 1.8.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oregano is intended to be an application for schematic capture and
simulation of electrical circuits. The actual simulation is performed
by Berkeley Spice. Oregano can still be used without Spice, for
schematic capture.

%description -l pl.UTF-8
Oregano jest aplikacją do tworzenia schematów i symulacji obwodów
elektrycznych. Właściwa symulacja jest robiona przez Berkeley Spice.
Bez Spice nadal można używać Oregano - do rysowania schematów.

%prep
%setup -q
#%%patch0 -p1

%build
rm -f missing
scons PREFIX=/usr

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT

scons install \
	DESTDIR=$RPM_BUILD_ROOT/ \
	PREFIX=/usr

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Changelog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/oregano.desktop
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_datadir}/oregano
