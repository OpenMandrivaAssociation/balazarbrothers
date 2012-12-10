%define name 	balazarbrothers   
%define oname   BalazarBrothers
%define version 0.3.1
%define	rel	6
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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-6mdv2011.0
+ Revision: 616707
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-5mdv2010.0
+ Revision: 436767
- rebuild

* Wed Mar 11 2009 Emmanuel Andry <eandry@mandriva.org> 0.3.1-4mdv2009.1
+ Revision: 353554
- fix url

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-3mdv2009.0
+ Revision: 222599
- buildrequires python-devel instead of python
- BuildRequires python for distutils/core.py
- requires python for distutils
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Emmanuel Andry <eandry@mandriva.org>
    - drop old menu
    - Import balazarbrothers



* Sun Aug 27 2006 Emmanuel Andry <eandry@mandriva.org> 0.3.1-2mdv2007.0
- requires tofu (bug #24757)
- xdg cleanup

* Mon Jul 10 2006 Lenny Cartier <lenny@mandriva.com> 0.3.1-1mdv2007.0
- new
