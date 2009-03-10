%define name 	balazarbrothers   
%define oname   BalazarBrothers
%define version 0.3.1
%define	rel	4
%define release %mkrel %{rel}

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Url:		http://home.gna.org/oomadness/fr/balazar_brothers/index.html
Source:		http://download.gna.org/soya/%{oname}-%{version}.tar.bz2
Group:          Games/Puzzles
Summary:        Amazing libre (GPL'ed) 3D puzzle game
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	cerealizer soya glew openal cal3d python-twisted python
Requires:	pyvorbis pyogg pyopenal tofu
# (tv) for python:/usr/lib/python2.5/distutils/core.py
BuildRequires: python-devel
Buildarch:	noarch

%description
Balazar Brother is an amazing libre (GPL'ed) 3D puzzle gam

%prep
%setup -q  -n %{oname}-%{version}
rm -rf `find -name CVS` `find -name .cvswrappers`

%build
# needed to generate proper c code for gcc4
#pyrexc _ode.pyx 

%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

install -d %{buildroot}%{_menudir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Balazar Brothers
Comment=%{summary}
Exec=%{_bindir}/balazar_brothers %U
Icon=puzzle_section 
Terminal=false
Type=Application
Categories=Game;LogicGame
StartupNotify=true
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README 
%_bindir/*
%_datadir/balazar_brothers
%_datadir/applications/*
%_datadir/*.egg-info


