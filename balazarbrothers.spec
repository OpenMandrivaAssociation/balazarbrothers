%define name 	balazarbrothers   
%define oname   BalazarBrothers
%define version 0.3.1
%define	rel	3
%define release %mkrel %{rel}

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Url:		http://home.gna.org/oomadness/en/balazar_brother/index.html
Source:		http://download.gna.org/soya/%{oname}-%{version}.tar.bz2
Group:          Games/Puzzles
Summary:        Amazing libre (GPL'ed) 3D puzzle game
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	cerealizer soya glew openal cal3d python-twisted python
Requires:	pyvorbis pyogg pyopenal tofu
# (tv) for python:/usr/lib/python2.5/distutils/core.py
BuildRequires: python
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
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_menudir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%_bindir/*
%_datadir/balazar_brothers
%_datadir/applications/*
%_datadir/*.egg-info


