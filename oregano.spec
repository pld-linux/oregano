%define  ver     0.12
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define  prefix  /usr

Summary: Oregano
Name: 		oregano
Version: 	%ver
Release: 	%rel
Copyright: 	GPL
Group: 		Applications/Engineering
Source: 	http://www.dtek.chalmers.se/~d4hult/oregano/oregano-%{ver}.tar.gz
Url:		http://www.dtek.chalmers.se/~d4hult/oregano
BuildRoot:	/var/tmp/oregano-%{PACKAGE_VERSION}-root
Docdir: 	%{prefix}/doc

Requires: gnome-libs >= 1.0.0
Requires: libxml >= 1.5.0
Requires: libglade >= 0.8
Requires: gnome-print >= 0.8

%description
Oregano, schematic capture and simulation of electrical circuits.

%prep
%setup -q

%build
%ifarch alpha
  MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix $MYARCH_FLAGS --sysconfdir=/etc

if [ "$SMP" != "" ]; then
	make -j$SMP "MAKE=make -j$SMP"
else
	make
fi

%install

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc ChangeLog NEWS README COPYING TODO

%{prefix}/bin/*
%{prefix}/share/locale/*/*
%{prefix}/share/gnome/help/oregano/*/*
%{prefix}/share/gnome/apps/Applications/oregano.desktop
%{prefix}/share/mime-info/*
%{prefix}/share/pixmaps/*
%{prefix}/share/oregano/*
