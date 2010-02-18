%define beta b1
Summary: Design and edit database files compatible with SQLite
Name: sqlitebrowser
Version: 2.0
Release: %mkrel -c %beta 1
Source0: http://heanet.dl.sourceforge.net/sourceforge/sqlitebrowser/%{name}_200_%{beta}_src.tar.gz
Patch0: sqlitebrowser-2.0-fix-str-fmt.patch
License: Public Domain
Group: System/Configuration/Other
Url: http://sqlitebrowser.sourceforge.net/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel

%description
SQLite Database Browser is a freeware, public domain, open source 
visual tool used to create, design and edit database files compatible 
with SQLite. It is meant to be used for users and developers that want 
to create databases, edit and search data using a familiar 
spreadsheet-like interface, without the need to learn complicated 
SQL commands. Controls and wizards are available for users to:

    * Create and compact database files
    * Create, define, modify and delete tables
    * Create, define and delete indexes
    * Browse, edit, add and delete records
    * Search records
    * Import and export records as text
    * Import and export tables from/to CSV files
    * Import and export databases from/to SQL dump files
    * Issue SQL queries and inspect the results
    * Examine a log of all SQL commands issued by the application


%prep
%setup -q -n trunk/%{name}/%{name}
%patch0 -p0

%build
%qmake_qt4
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}/%{_bindir}
cp sqlitebrowser %{buildroot}/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSING
%{_bindir}/sqlitebrowser


