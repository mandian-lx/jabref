%{?_javapackages_macros:%_javapackages_macros}

%define oname JabRef
%define name %(tr [:upper:] [:lower:] <<<%{oname})

Summary:	Graphical application for managing bibtex (.bib) databases
Name:		%{name}
Version:	2.11.1
Release:	1
License:	GPLv2+ and BSD
Group:		Development/Java
URL:		http://jabref.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/%{name}/%{oname}-%{version}-src.tar.gz
Source0:	https://github.com/JabRef/%{name}/archive/v_%{version}/%{name}-%{version}.tar.gz
# Adapted from help2man output
Source1:	jabref.%{version}
Patch0:		%{name}-2.11.1-build_xml.patch
Patch1:		%{name}-2.11.1-javadoc.patch
Patch2:		%{name}-2.11.1-classpath.patch
Patch3:		%{name}-2.11.1-antlr.patch
Patch4:		%{name}-2.11.1-remove_mrDlib.patch
Patch5:		%{name}-2.11.1-jgoodies_forms.patch
Patch6:		%{name}-2.11.1-plugin.patch
#BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	mvn(commons-cli:commons-cli)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(com.google.guava:guava)
BuildRequires:	mvn(com.jgoodies:jgoodies-common)
BuildRequires:	mvn(com.jgoodies:jgoodies-forms)
BuildRequires:	mvn(com.jgoodies:jgoodies-looks)
BuildRequires:	mvn(com.michaelbaranov.microba:microba)
BuildRequires:	mvn(mysql:mysql-connector-java)
BuildRequires:	mvn(net.java.dev.glazedlists:glazedlists)
BuildRequires:	mvn(net.java.dev.jna:jna)
BuildRequires:	mvn(org.antlr:antlr)
BuildRequires:	mvn(org.antlr:antlr-runtime)
BuildRequires:	mvn(org.antlr:antlr4)
BuildRequires:	mvn(org.antlr:antlr4-runtime)
BuildRequires:	mvn(org.apache.pdfbox:pdfbox)
BuildRequires:	mvn(org.apache.pdfbox:fontbox)
BuildRequires:	mvn(org.apache.pdfbox:jempbox)
BuildRequires:	mvn(postgresql:postgresql)
BuildRequires:	mvn(spin:spin)
BuildRequires:	swingx #mvn(org.swinglabs:swingx)
# plugins
BuildRequires:	jpf
BuildRequires:	jpf-boot
BuildRequires:	jpfcodegen
BuildRequires:	mvn(org.apache.velocity:velocity)
# LibreOffice integration
BuildRequires:	libreoffice-java
# tests
BuildRequires:	mvn(junit:junit)

Requires:	mvn(commons-cli:commons-cli)
Requires:	mvn(commons-logging:commons-logging)
Requires:	mvn(com.google.guava:guava)
Requires:	mvn(com.jgoodies:jgoodies-common)
Requires:	mvn(com.jgoodies:jgoodies-forms)
Requires:	mvn(com.jgoodies:jgoodies-looks)
Requires:	mvn(com.michaelbaranov.microba:microba)
Requires:	mvn(mysql:mysql-connector-java)
Requires:	mvn(net.java.dev.glazedlists:glazedlists)
Requires:	mvn(net.java.dev.jna:jna)
Requires:	mvn(org.antlr:antlr)
Requires:	mvn(org.antlr:antlr-runtime)
Requires:	mvn(org.antlr:antlr4)
Requires:	mvn(org.antlr:antlr4-runtime)
Requires:	mvn(org.apache.pdfbox:pdfbox)
Requires:	mvn(org.apache.pdfbox:fontbox)
Requires:	mvn(org.apache.pdfbox:jempbox)
Requires:	mvn(postgresql:postgresql)
Requires:	mvn(spin:spin)
Requires:	swingx
# plugins
Requires:	apache-commons-logging
Requires:	jpf
Requires:	jpf-boot
Requires:	jpfcodegen
# libreoffice integration
Requires:	libreoffice-java >= 1:3.5.2

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
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1*
%doc README.md
%doc CHANGELOG
%doc TODO
%doc gpl2.txt 
%doc gpl3.txt 
%doc lesser.txt 

#----------------------------------------------------------------------------

%package javadoc
Summary:	API documentation for %{oname}
BuildArch:	noarch

%description javadoc
API documentation for %{oname}.

%files javadoc
%doc %{_javadocdir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q

# Delete all pre-build binaries
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Apply all patches
%patch0 -p1 -b .orig
%patch1 -p1 -b .javadoc
%patch2 -p1 -b .classpath
%patch3 -p1 -b .antlr
%patch4 -p1 -b .remove_mrDlib
%patch5 -p1 -b .jgoodies
%patch6 -p1 -b .plugin

# Remove bundled libs
#   mrDlib
rm -f src/main/java/spl/{DocumentWrapper,DocumentsWrapper,SplWebClient,gui/MetaDataListDialog}.java

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
	   }' src/main/java/net/sf/jabref/oo/OpenOfficePanel.java

%build
export ANT_OPTS=" -Dlo.lib.dir=%{_libdir}/libreoffice/program/classes/ -Dsystem.lib.dir=%{_javadir} -Djavadoc.encoding=ISO-8859-1 -Djavadoc.docencoding=UTF-8"

# Use system jars
export CLASSPATH=$(build-classpath antlr antlr3 antlr3-runtime antlr4 antlr4-runtime fontbox glazedlists jempbox jgoodies-common jgoodies-forms jgoodies-looks jna microba mysql-connector-java pdfbox postgresql-jdbc ritopt spin stringtemplate stringtemplate4/ST4 swingx)
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
%jpackage_script net.sf.jabref.JabRefMain "" "" antlr:antlr3:antlr3-runtime:antlr4-runtime:apache-commons-cli:apache-commons-logging:glazedlists:guava:jempbox:jgoodies-common:jgoodies-forms:jgoodies-looks:jpf:jpf-boot:jpfcodegen-rt:microba:pdfbox:ritopt:spin:swingx:jabref jabref true

# jar
install -dm 0755 %{buildroot}%{_javadir}/
install -pm 0644 buildant/lib/%{oname}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -dm 0755 p %{buildroot}%{_javadocdir}/%{name}/
cp -ar buildant/docs/API/* %{buildroot}%{_javadocdir}/%{name}

# icons
install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps/
install -pm 0644 src/main/resources/images/%{oname}-icon.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -pm 0644 src/main/resources/images/%{oname}-icon-32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -pm 0644 src/main/resources/images/%{oname}-icon-48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
#	missing formats
for d in 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -scale ${d}x${d} src/main/resources/images/%{oname}-icon-48.png \
			%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
#   pixmap
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -size 32x32 src/main/resources/images/%{oname}-icon-32.png %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

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

