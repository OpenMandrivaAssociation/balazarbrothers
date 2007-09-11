%define name 	balazarbrothers   
%define oname   BalazarBrothers
%define version 0.3.1
%define	rel	2
%define release %mkrel %{rel}

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Url:		http://home.gna.org/oomadness/en/balazar_brother/index.html
Source:        http://download.gna.org/soya/%{oname}-%{version}.tar.bz2
Group:          Games/Puzzles
Summary:        Balazar Brother is an amazing libre (GPL'ed) 3D puzzle game
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	cerealizer soya glew openal cal3d python-twisted
Requires:	pyvorbis pyogg pyopenal tofu
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

cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%name): needs="x11" \
        section="More Applications/Games/Puzzles" \
        title="Balazar Brothers" \
        longtitle="%{summary}" \
        command="%{_bindir}/balazar_brothers" \
        icon="puzzle_section.png" \
        startup_notify="true" \
        multiple_files="true" \
        xdg="true"
EOF

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

%post
%{update_menus}

%postun
%{clean_menus}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%_bindir/*
%_datadir/balazar_brothers
%_menudir/*
%_datadir/applications/*
