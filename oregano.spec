Summary:	Oregano - schematic capture and simulation of electrical circuits
Name:		oregano
Version:	0.14
Release:	2
License:	GPL
Group:		Applications/Engineering
Group(pl):	Aplikacje/In¿ynierskie
Source0:	http://www.dtek.chalmers.se/~d4hult/oregano/download/%{name}-%{version}.tar.gz
Patch0:		oregano-applnk.patch
URL:		http://www.dtek.chalmers.se/~d4hult/oregano/
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	libxml-devel >= 1.5.0
BuildRequires:	libglade-devel >= 0.8
BuildRequires:	gnome-print-devel >= 0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Oregano is intended to be an application for schematic capture and
simulation of electrical circuits. The actual simulation is performed by
Berkeley Spice. Oregano can still be used without Spice, for schematic
capture.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/help/oregano
%{_applnkdir}/Applications/oregano.desktop
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_datadir}/oregano
