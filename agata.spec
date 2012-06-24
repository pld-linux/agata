# TODO: applnk

Summary:	Agata Reports
Name:		agata
Version:	3_final
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.codigolivre.org.br/agata/%{name}_%{version}.zip
Patch0:		%{name}-ini.patch
URL:		http://agata.codigolivre.org.br/
Requires:	php-gtk
Requires:	php-pear-DB
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Agata Report is a Database Reporting Tool and EIS tool, MIS tool (graph
generation), like Crystal Reports. Its written in PHP-GTK and allows you
to edit and get SQL results from several databases as Text or PostScript Files. 

%prep
%setup -q -n %{name}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/agata

# What a mess...
cp -rf classes $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rf images $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rf jpgraph $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rf themes $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -f agata.php $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -f common.php $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -f config.php $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -f Main.php $RPM_BUILD_ROOT%{_datadir}/%{name}

cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/agata
#!/bin/sh
cd %{_datadir}/%{name}
php agata.php
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS config.ini
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
