Summary:	Oregano - schematic capture and simulation of electrical circuits
Summary(pl):	Oregano - zdobywanie schematów i symulacja obwodów elektrycznych
Name:		oregano
Version:	0.23
Release:	2
License:	GPL
Group:		Applications/Engineering
Group(de):	Applikationen/Ingenieurwesen
Group(pl):	Aplikacje/In¿ynierskie
Source0:	ftp://ftp.codefactory.se/pub/software/oregano/%{name}-%{version}.tar.gz
URL:		http://oregano.codefactory.se/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	libxml-devel >= 1.8.10
BuildRequires:	libglade-devel >= 0.8
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Oregano is intended to be an application for schematic capture and
simulation of electrical circuits. The actual simulation is performed
by Berkeley Spice. Oregano can still be used without Spice, for
schematic capture.

%description -l pl
Oregano jest aplikacj± do zdobywania schematów i symulacji obwodów
elektrycznych. W³a¶ciwa symulacja jest robiona przez Berkeley Spice.
Bez Spice nadal mo¿na u¿ywaæ Oregano - do schematów.

%prep
%setup -q

%build
rm -f missing
gettextize --copy --force
libtoolize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Scientific/Misc \
	samplesdir=%{_examplesdir}/%{name}

gzip -9nf ChangeLog NEWS README

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Scientific/Misc/oregano.desktop
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_datadir}/oregano
%{_examplesdir}/%{name}
