%{?_javapackages_macros:%_javapackages_macros}
%define debug_package %{nil}

%define oname JabRef
%define name %(echo %oname | tr [:upper:] [:lower:])

Summary:	A graphical Java application for editing BibTeX and Biblatex databases
Name:		%{name}
Version:	3.6
Release:	1
License:	MIT
Group:		Editors
URL:		https://www.jabref.org/
Source0:	https://github.com/%{oname}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Adapted from manpage generated with help2man
#    help2man -L C -s 1 -N -o jabref.1 /usr/bin/jabref 
Source1:	%{name}.3.6
# FIXME: gradle has not been packaged yet.
#	(https://issues.openmandriva.org/show_bug.cgi?id=1665)
Source2:	%{name}-3.6.build.xml
Patch0:		%{name}-3.6-json.patch
Patch1:		%{name}-3.6-MacAdapter.patch
# The following patch is because there is an outdate version
# of guava in repo. It can be safely removed when guava 20.0
# will be provided.
Patch2:		%{name}-3.6-guava.patch
BuildArch:	noarch

BuildRequires:	imagemagick
BuildRequires:	librsvg
BuildRequires:	javapackages-local
BuildRequires:	ant
BuildRequires:	mvn(com.google.guava:guava)
BuildRequires:	mvn(com.googlecode.java-diff-utils:diffutils)
BuildRequires:	mvn(com.jgoodies:jgoodies-common)
BuildRequires:	mvn(com.jgoodies:jgoodies-forms)
BuildRequires:	mvn(com.jgoodies:jgoodies-looks)
BuildRequires:	mvn(com.mashape.unirest:unirest-java)
BuildRequires:	mvn(com.michaelbaranov.microba:microba)
BuildRequires:	mvn(com.sun.xml.bind:jaxb-xjc)
BuildRequires:	mvn(info.debatty:java-string-similarity)
BuildRequires:	mvn(mysql:mysql-connector-java)
BuildRequires:	mvn(net.java.dev.glazedlists:glazedlists_java15)
BuildRequires:	mvn(org.apache.httpcomponents:httpclient)
BuildRequires:	mvn(org.json:json)
BuildRequires:	mvn(postgresql:postgresql)
BuildRequires:	orange-extensions
BuildRequires:	mvn(org.antlr:antlr)
BuildRequires:	mvn(org.antlr:antlr-runtime)
BuildRequires:	mvn(org.antlr:antlr4)
BuildRequires:	mvn(org.antlr:antlr4-runtime)
BuildRequires:	mvn(org.antlr:ST4)
BuildRequires:	mvn(org.apache.commons:commons-cli) >= 1.3.1
BuildRequires:	mvn(org.apache.commons:commons-lang3)
BuildRequires:	mvn(org.apache.commons:commons-logging)
BuildRequires:	mvn(org.apache.logging.log4j:log4j-jcl)
BuildRequires:	mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:	mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:	mvn(org.apache.pdfbox:pdfbox)
BuildRequires:	mvn(org.apache.pdfbox:fontbox)
BuildRequires:	mvn(org.apache.pdfbox:jempbox)
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:	mvn(org.jsoup:jsoup)
#BuildRequires:	spin
BuildRequires:	swingx < 1.6.5.1	#mvn(org.swinglabs:swingx) --- NOTE: do not update, 1.6.5.1 is broken
# LibreOffice integration
BuildRequires:	libreoffice-java	#mvn(org.openoffice:juh)
BuildRequires:	libreoffice-java	#mvn(org.openoffice:jurt)
BuildRequires:	libreoffice-java	#mvn(org.openoffice:ridl)
BuildRequires:	libreoffice-java	#mvn(org.openoffice:unoil)
# tests
#BuildRequires:	mvn(junit:junit)
#BuildRequires:	mvn(org.mockito:mockito-core)
#BuildRequires:	mvn(com.github.tomakehurst:wiremock)
#BuildRequires:	mvn(org.assertj:assertj-swing-junit)

Requires:	java-headless >= 1:1.6
Requires:	jpackage-utils
Requires:	antlr
Requires:	antlr3
Requires:	antlr3-java
Requires:	antlr4
Requires:	antlr4-runtime
Requires:	apache-commons-cli >= 1.3
Requires:	apache-commons-logging
Requires:	java-diff-utils
Requires:	glazedlists
Requires:	java-string-similarity
Requires:	jempbox
Requires:	jgoodies-common >= 1.4.0
Requires:	jgoodies-forms >= 1.6.0
Requires:	jgoodies-looks >= 2.5.0
Requires:	json
Requires:	jsoup
Requires:	libreoffice-java >= 1:3.5.2
Requires:	log4j
Requires:	microba
Requires:	orange-extensions
Requires:	pdfbox
Requires:	ritopt
Requires:	spin
Requires:	stringtemplate4
Requires:	swingx
Requires:	unirest-java
# libreoffice integration
Requires:	libreoffice-java >= 1:3.5.2

%description
JabRef is a graphical Java application for editing BibTeX and Biblatex .bib
databases. JabRef lets you organize your entries into overlapping logical
groups, and with a single click limit your view to a single group or an
intersection or union of several groups. You can customize the entry
information shown in the main window, and sort by any of the standard BibTeX
fields. JabRef can autogenerate BibTeX keys for your entries. JabRef also
lets you easily link to PDF or web sources for your reference entries.

JabRef can import from and export to several formats, and you can customize
export filters. JabRef can be run as a command line application to convert
from any import format to any export format.

%files
%{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/openmandriva-%{name}.desktop
%doc %{_mandir}/man1/%{name}.1.*
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc DEVELOPERS
%doc LICENSE.md

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

# Delete all JARs and classes
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Apply all patches
%patch0 -p1 -b .json
%patch1 -p1 -b .MacAdapter
%patch2 -p1 -b .guava

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

# Add build.xml
cp %{SOURCE2} ./build.xml

# Fix version in build.xml
sed -i -e 's|#version#|%{version}|g' ./build.xml

# Fix LibreOffice path
sed -i -e '{
	     s|/opt/openoffice.org3|%{_libdir}/libreoffice|
	     s|/usr/lib/openoffice/program/soffice|%{_libdir}/libreoffice/program/soffice|
	     s|/opt/openoffice.org/basis3.0|%{_libdir}/libreoffice|
	   }' src/main/java/net/sf/jabref/preferences/JabRefPreferences.java

%build
# Classpath
#    system jars
build-jar-repository lib ant antlr antlr3 antlr3-runtime antlr4 antlr4-runtime apache-commons-cli apache-commons-lang3 apache-commons-logging com.sun:tools bcprov-jdk15on fontbox glazedlists guava httpcomponents/httpclient java-diff-utils java-string-similarity jempbox jgoodies-common jgoodies-forms jgoodies-looks json jsoup libreoffice/juh libreoffice/urt libreoffice/ridl libreoffice/unoil microba mysql-connector-java log4j log4j/log4j-core log4j/log4j-api orange-extensions pdfbox postgresql-jdbc stringtemplate4 unirest-java swingx
# spin

# binary
%ant jars

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/
install -pm 0644 buildant/lib/%{oname}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
#install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/
#cp -r build/docs/API/* %{buildroot}%{_javadocdir}/%{name}/

# launcher
%jpackage_script net.sf.jabref.JabRefMain "" "" antlr:antlr3:antlr3-runtime:antlr4:antlr4-runtime:bcprov:commons-cli:commons-lang3:commons-logging:fontbox:glazedlists:guava:httpcomponents/client:java-diff-utils/diffutils:java-string-similarity:jempbox:jgoodies-common:jgoodies-forms:jgoodies-looks:json:jsoup:libreoffice/juh:libreoffice/jurt:libreoffice/ridl:libreoffice/unoil:mysql-connector-java:log4j:log4j/log4j-api:log4j/log4j-core:log4j/log4j-jcl:microba:orange-extensions:pdfbox:postgresql-jdbc:ritopt:spin:stringtemplate4:swingx:unirest-java:jabref jabref true


# icons
# FIXME: imagemagick makes empty images (maybe a bug in inkskape maybe
#        a bug in image) and rsvg-convert works properly for png only
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	rsvg-convert -f png -h ${d} -w ${d} src/main/resources/images/icons/%{oname}-icon.svg \
		-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
#	convert -background none -resize "${d}x${d}" src/main/resources/images/icons/%{oname}-icon.svg \
#		%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
#   pixmap
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
#rsvg-convert -f xpm -h ${d} -w ${d} src/main/resources/images/icons/%{oname}-icon.svg \
#		-o %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
convert -background none -resize 32x32 src/main/resources/images/icons/%{oname}-icon.svg \
		%{buildroot}%{_datadir}/pixmaps/%{name}.xpm
#   scalable
install -dm 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -pm 0644 src/main/resources/images/icons/%{oname}-icon.svg \
		%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

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

