%define oname   BalazarBrothers

Name:           balazarbrothers
Version:        0.3.1
Release:        6
License:        GPL
Url:		https://home.gna.org/oomadness/fr/balazar_brothers/index.html
Source:		http://download.gna.org/soya/%{oname}-%{version}.tar.bz2
Group:          Games/Puzzles
Summary:        Amazing libre (GPL'ed) 3D puzzle game
Requires:	cerealizer
Requires:	soya
Requires:	glew
Requires:	openal
Requires:	cal3d
Requires:	python-twisted python
Requires:	pyvorbis
Requires:	pyogg
Requires:	pyopenal
Requires:	tofu

BuildRequires: python2-devel

Buildarch:	noarch

%description
Balazar Brother is an amazing libre (GPL'ed) 3D puzzle game.

%prep
%setup -qn %{oname}-%{version}
rm -rf `find -name CVS` `find -name .cvswrappers`

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

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


%files
%doc README 
%{_bindir}/*
%{_datadir}/balazar_brothers
%{_datadir}/applications/*
%{_datadir}/*.egg-info
