Summary:	Oregano - schematic capture and simulation of electrical circuits
Summary(pl):	Oregano - zdobywanie schematów i symulacja obwodów elektrycznych
Name:		oregano
Version:	0.23
Release:	7
License:	GPL
Group:		Applications/Engineering
Source0:	ftp://ftp.codefactory.se/pub/software/oregano/%{name}-%{version}.tar.gz
# Source0-md5:	226b84622dd1b877ee87228ba74d68d1
URL:		http://people.imendio.com/richard/oregano/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-print-devel >= 0.30
BuildRequires:	libglade-gnome-devel >= 0.8
BuildRequires:	libtool
BuildRequires:	libxml-devel >= 1.8.10
Conflicts:	applnk < 1.5.18
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
	Applicationsdir=%{_applnkdir}/Scientific/Engineering \
	samplesdir=%{_examplesdir}/%{name}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Scientific/Engineering/oregano.desktop
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_datadir}/oregano
%{_examplesdir}/%{name}
