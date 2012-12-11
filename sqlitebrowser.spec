%define beta b1
%define svn  r68

Name: sqlitebrowser
Version: 2.0
Release: %mkrel -c %svn 1

Summary:    Design and edit database files compatible with SQLite
License:    Public Domain
Group:      System/Configuration/Other
Url:        http://sqlitebrowser.sourceforge.net/index.html
#Source0:    http://heanet.dl.sourceforge.net/sourceforge/sqlitebrowser/%{name}_200_%{beta}_src.tar.gz
Source0:    http://heanet.dl.sourceforge.net/sourceforge/sqlitebrowser/%{name}-%{svn}.tar.xz
Patch0:     sqlitebrowser-2.0-fix-str-fmt.patch
Patch1:     sqlitebrowser-2.0-use_system_sqlite.patch

BuildRequires: qt4-devel
BuildRequires: sqlite3-devel

%description
SQLite Database Browser is a freeware, public domain, open source 
visual tool used to create, design and edit database files compatible 
with SQLite. It is meant to be used for users and developers that want 
to create databases, edit and search data using a familiar 
spreadsheet-like interface, without the need to learn complicated 
SQL commands.

%prep
%setup -q -n %{name}/%{name}/%{name}
%patch0 -p0
%patch1 -p3
chmod 644 *txt

%build
%qmake_qt4
%make

%install
install -d -m 755 %{buildroot}/%{_bindir}
cp sqlitebrowser %{buildroot}/%{_bindir}/

install -d -m 755 %{buildroot}%{_datadir}/applications/
cat >%{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=SQLite database browser
Comment=GUI editor for SQLite databases
TryExec=sqlitebrowser
Exec=sqlitebrowser
Icon=sqlitebrowser
Terminal=false
Type=Application
Categories=Development;Database;Qt;
MimeType=application/x-sqlite3;
EOF

install -m 644 -D images/128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%files
%doc *.txt
%{_bindir}/sqlitebrowser
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
