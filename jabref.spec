%{?_javapackages_macros:%_javapackages_macros}

%define oname JabRef
%define name %(tr [:upper:] [:lower:] <<<%{oname})

Summary:	Graphical application for managing bibtex (.bib) databases
Name:		%{name}
Version:	2.10
Release:	1
License:	GPLv2+ and BSD
Group:		Development/Java
URL:		http://jabref.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/%{name}/%{oname}-%{version}-src.tar.bz2
Source0:	https://github.com/JabRef/%{name}/archive/v_%{version}/%{name}-%{version}.tar.gz
# Adapted from help2man output
Source1:	jabref.%{version}
Patch0:		%{name}-2.10-build_xml.patch
Patch1:		%{name}-2.10-encoding.patch
Patch2:		%{name}-2.10-classpath.patch
Patch3:		%{name}-2.10-remove_ayatana.patch
Patch4:		%{name}-2.10-remove_mrDlib.patch
Patch5:		%{name}-2.10-jgoodies_forms.patch
Patch6:		%{name}-2.10-plugin.patch
# http://sourceforge.net/p/jabref/bugs/1278/
# https://github.com/JabRef/jabref/commit/6f23b7f8bf393826924f3755579dc546c044b091
# https://github.com/JabRef/jabref/commit/a2979b5170214e8cb024f34142cc57d3d1a8ba55
Patch7:		%{name}-2.10-lookAndFeel.patch
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	antlr3-java
BuildRequires:	antlr3-tool
BuildRequires:	antlr-tool
BuildRequires:	fontbox
BuildRequires:	glazedlists
BuildRequires:	jempbox
BuildRequires:	jgoodies-common
BuildRequires:	jgoodies-forms
BuildRequires:	jgoodies-looks
BuildRequires:	microba
BuildRequires:	mysql-connector-java
BuildRequires:	pdfbox
 BuildRequires:	postgresql-jdbc
BuildRequires:	ritopt
BuildRequires:	spin
# plugins
BuildRequires:	apache-commons-collections
BuildRequires:	apache-commons-lang
BuildRequires:	apache-commons-logging
BuildRequires:	jpf
BuildRequires:	jpf-boot
BuildRequires:	jpfcodegen
BuildRequires:	velocity
# LibreOffice integration
BuildRequires:	libreoffice-java
# tests
BuildRequires:	junit

Requires:	java-headless >= 1:1.6
Requires:	jpackage-utils
Requires:	antlr3-java
Requires:	antlr3-tool
Requires:	antlr-tool
Requires:	fontbox
Requires:	glazedlists
Requires:	jempbox
Requires:	jgoodies-common
Requires:	jgoodies-forms
Requires:	jgoodies-looks
Requires:	microba
Requires:	mysql-connector-java
Requires:	pdfbox
Requires:	postgresql-jdbc
Requires:	ritopt
Requires:	spin
# plugins
Requires:	apache-commons-logging
Requires:	jpf
Requires:	jpf-boot
Requires:	jpfcodegen
# libreoffice integration
Requires:	libreoffice-java

%description
JabRef is a graphical Java application for editing BibTeX (.bib)
databases. JabRef lets you organize your entries into overlapping
logical groups, and with a single click limit your view to a single
group or an intersection or union of several groups. You can customize
the entry information shown in the main window, and sort by any of the
standard Bibtex fields. JabRef can auto-generate BibTeX keys for your
entries. JabRef also lets you easily link to PDF or web sources for your
reference entries.

JabRef can import from and export to several formats, and you can
customize export filters. JabRef can be run as a command line application
to convert from any import format to any export format.

%files
%{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_datadir}/applications/openmandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
#%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1*
%doc README.md
%doc src/txt/README
%doc src/txt/CHANGELOG
%doc src/txt/TODO
%doc src/txt/gpl2.txt 
%doc src/txt/gpl3.txt 
%doc src/txt/lesser.txt 

#----------------------------------------------------------------------------

%package javadoc
Summary:	API documentation for %{oname}

%description javadoc
API documentation for %{oname}.

%files javadoc
%doc %{_javadocdir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-v_%{version}

# Delete all pre-build binaries
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Apply all patches
%patch0 -p1 -b .orig
%patch1 -p1 -b .encoding
%patch2 -p1 -b .classpath
%patch3 -p1 -b .remove_ayatana
%patch4 -p1 -b .remove_mrDlib
%patch5 -p1 -b .jgoodies
%patch6 -p1 -b .plugin
%patch7 -p1 -b .orig

# Remove bundled libs
#   ritopt
rm -rf src/java/gnu
#   mrDlib
rm -f src/java/spl/{DocumentWrapper,DocumentsWrapper,SplWebClient,gui/MetaDataListDialog}.java

# .desktop
cat > openmandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{oname}
GenericName=Bibliographic databases manager
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Office;Database;
EOF

# Fix LibreOffice path
sed -i -e '{
	     s|/opt/openoffice.org3|%{_libdir}/libreoffice|
	     s|/usr/lib/openoffice/program/soffice|%{_libdir}/libreoffice/program/soffice|
	     s|/opt/openoffice.org/basis3.0|%{_libdir}/libreoffice/program/classes|
	   }' src/java/net/sf/jabref/oo/OpenOfficePanel.java

%build
export ANT_OPTS=" -Dlo.lib.dir=%{_libdir}/libreoffice/program/classes/ -Dsystem.lib.dir=%{_javadir} -Djavadoc.encoding=ISO-8859-1 -Djavadoc.docencoding=UTF-8"

# Use system jars
export CLASSPATH=$(build-classpath antlr antlr3 antlr3-runtime fontbox glazedlists jempbox jgoodies-common jgoodies-forms jgoodies-looks microba mysql-connector-java pdfbox postgresql-jdbc ritopt spin)
#   plugins
export CLASSPATH=$CLASSPATH:$(build-classpath apache-commons-collections apache-commons-lang apache-commons-logging jpf jpf-boot jpfcodegen jpfcodegen-rt velocity)
#   LibreOffice jars
export CLASSPATH=$CLASSPATH:$(build-classpath ../../%{_lib}/libreoffice/program/classes/juh.jar ../../%{_lib}/libreoffice/program/classes/jurt.jar ../../%{_lib}/libreoffice/program/classes/ridl.jar ../../%{_lib}/libreoffice/program/classes/unoil.jar)

# jars
%ant jars

# docs
%ant docs

%install
# Shell script
%jpackage_script net.sf.jabref.JabRefMain "" "" antlr:antlr3:antlr3-runtime:apache-commons-logging:fontbox:glazedlists:jempbox:jgoodies-common:jgoodies-forms:jgoodies-looks:jpf:jpf-boot:jpfcodegen-rt:microba:mysql-connector-java:postgresql-jdbc:pdfbox:ritopt:spin:../../%{_lib}/libreoffice/program/classes/juh.jar:../../%{_lib}/libreoffice/program/classes/jurt.jar:../../%{_lib}/libreoffice/program/classes/ridl.jar:../../%{_lib}/libreoffice/program/classes/unoil.jar:jabref jabref true

# jar
install -dm 0755 %{buildroot}%{_javadir}/
install -pm 0644 build/lib/%{oname}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -dm 0755 p %{buildroot}%{_javadocdir}/%{name}/
cp -ar build/docs/API/* %{buildroot}%{_javadocdir}/%{name}

# icons
install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps/
install -pm 0644 src/images/%{oname}-icon.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -pm 0644 src/images/%{oname}-icon-32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -pm 0644 src/images/%{oname}-icon-48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
#	missing formats
for d in 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -scale ${d}x${d} src/images/%{oname}-icon-48.png %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
#   pixmap
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -size 32x32 src/images/%{oname}-icon-32.png %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
#   scalable
#install -dm 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
#install -pm 0644 src/images/%{oname}-icon-48.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# .desktop file
install -dm 0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications/ \
	openmandriva-%{name}.desktop

# manpage
install -dm 0755 %{buildroot}%{_mandir}/man1/
install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%check
# desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/openmandriva-%{name}.desktop

