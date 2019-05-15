
Name: sqlitebrowser
Version: 3.11.2
Release: 1

Summary:    Design and edit database files compatible with SQLite
License:    Public Domain
Group:      System/Configuration/Other
Url:        https://github.com/sqlitebrowser
Source0:    https://github.com/sqlitebrowser/sqlitebrowser/archive/%name-%{version}.tar.gz 
#Patch0:	    fix-cmake-qscinitlla2-search.patch
BuildRequires: qt5-devel
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Test)
BuildRequires: sqlite3-devel
BuildRequires: antlr-C++
BuildRequires: %{_lib}qscintilla_qt5-devel

#Requires: antlr
#Requires: customplot
#Requires: qhexedit
#Requires: qscintilla

%description
SQLite Database Browser is a freeware, public domain, open source 
visual tool used to create, design and edit database files compatible 
with SQLite. It is meant to be used for users and developers that want 
to create databases, edit and search data using a familiar 
spreadsheet-like interface, without the need to learn complicated 
SQL commands.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1
chmod 644 *txt

%build
%cmake -DQSCINTILLA_INCLUDE_DIR=/usr/include/qt5/Qsci -DQSCINTILLA_LIBRARY=/usr/lib64/libqscintilla2_qt5.so  .

%make_build 

%install
cd build
%make_install 

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

mkdir -p %{buildroot}/usr/lib64
cp libs/qhexedit/libqhexedit.so %{buildroot}/usr/lib64/
cp libs/qcustomplot-source/libqcustomplot.so %{buildroot}/usr/lib64/

%files
%doc *.txt
%{_bindir}/sqlitebrowser
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/appdata/sqlitebrowser.desktop.appdata.xml
%{_libdir}/libqhexedit.so
%{_libdir}/libqcustomplot.so