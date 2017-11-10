%{?_javapackages_macros:%_javapackages_macros}

%define oname JabRef
%define name %(echo %oname | tr [:upper:] [:lower:])

Summary:	A graphical Java application for editing BibTeX and Biblatex databases
Name:		%{name}
Version:	3.8.2
Release:	0
License:	MIT
Group:		Editors
URL:		https://www.jabref.org/
Source0:	https://github.com/%{oname}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Adapted from manpage generated with help2man
#    help2man -L C -s 1 -N -o jabref.1 /usr/bin/jabref 
Source1:	%{name}.3.8
# xjc schemas
Source10:	http://www.loc.gov/mods/xml.xsd
Source11:	http://www.loc.gov/standards/xlink/xlink.xsd
Source100:	%{name}-3.8.2-swingx-metadata.xml
Source101:	%{name}-3.8.2-libreoffice-metadata.xml
Patch1:		%{name}-3.8.2-gradle-local-mode.patch
Patch2:		%{name}-3.8.2-gradle-remove-unused-plugin.patch
Patch3:		%{name}-3.8.2-gradle-add-missing-dependencies.patch
Patch4:		%{name}-3.8.2-gradle-add-maven-plugin.patch
Patch5:		%{name}-3.8.2-xjc-use-local-schemas.patch
Patch6:		%{name}-3.8.2-dont-check-for-updates.patch
Patch7:		%{name}-3.8.2-remove-osx-support.patch
Patch8:		%{name}-3.8.2-guava_17.patch
Patch9:		%{name}-3.8.2-use-system-citationstyles.patch

BuildRequires:	imagemagick
BuildRequires:	librsvg
BuildRequires:	jpackage-utils
BuildRequires:	gradle-local
#BuildRequires:	maven-local
BuildRequires:	citationstyles-locales #-java #mvn(org.citationstyles:locales)	#NEW
BuildRequires:	citationstyles-styles #-java #mvn/org.citationstyles:styles)	#NEW
BuildRequires:	libreoffice-java						#mvn(org.openoffice:juh)
BuildRequires:	libreoffice-java						#mvn(org.openoffice:jurt)
BuildRequires:	libreoffice-java						#mvn(org.openoffice:ridl)
BuildRequires:	libreoffice-java						#mvn(org.openoffice:unoil)
BuildRequires:	mvn(com.github.lgooddatepicker:LGoodDatePicker)			#NEW, uploaded
BuildRequires:	mvn(com.google.guava:guava)					# >= 20.0
BuildRequires:	mvn(com.googlecode.java-diff-utils:diffutils)			#NEW, :1.3.0', uploaded
BuildRequires:	mvn(com.impossibl.pgjdbc-ng:pgjdbc-ng)				#NEW, uploaded
BuildRequires:	mvn(com.jgoodies:jgoodies-common)				#updated, uploaded
BuildRequires:	mvn(com.jgoodies:jgoodies-forms)				#updated, uploaded
BuildRequires:	mvn(com.jgoodies:jgoodies-looks)				#updated, uploaded
BuildRequires:	mvn(com.mashape.unirest:unirest-java)				#NEW, uploaded
BuildRequires:	mvn(com.yuvimasory:orange-extensions)				#NEW, uploaded
BuildRequires:	mvn(commons-cli:commons-cli) >= 1.3.1
BuildRequires:	mvn(commons-codec:commons-codec)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(de.undercouch:citeproc-java)				#NEW, uploaded
BuildRequires:	mvn(info.debatty:java-string-similarity)			#NEW, uploaded
BuildRequires:	mvn(mysql:mysql-connector-java)
BuildRequires:	mvn(net.java.dev.glazedlists:glazedlists)			# updated, uploaded
BuildRequires:	mvn(org.antlr:antlr)
BuildRequires:	mvn(org.antlr:antlr-runtime)
BuildRequires:	mvn(org.antlr:antlr4)
BuildRequires:	mvn(org.antlr:antlr4-runtime)
BuildRequires:	mvn(org.apache.commons:commons-lang3)
BuildRequires:	mvn(org.apache.logging.log4j:log4j-jcl)
BuildRequires:	mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:	mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:	mvn(org.apache.pdfbox:pdfbox)					#updated, uploaded
BuildRequires:	mvn(org.apache.pdfbox:fontbox)					#updated, uploaded
BuildRequires:	mvn(org.apache.pdfbox:jempbox)					#updated, uploaded
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk15on)				#updated, uploaded
BuildRequires:	mvn(org.jsoup:jsoup)						#NEW, uploaded
BuildRequires:	mvn(org.xmlunit:xmlunit-core)					#updated, uploaded
BuildRequires:	mvn(org.xmlunit:xmlunit-matchers)				#updated, uploaded
BuildRequires:	mvn(spin:spin)							#NEW, uploaded
BuildRequires:	swingx <= 1.6.1 #mvn(org.swinglabs:swingx:1.6.1)		# do not update, 1.6.5.1 is broken
#   tests
#BuildRequires:	mvn(junit:junit)
#BuildRequires:	mvn(org.mockito:mockito-core)					#FIXME: not packaged yew
#BuildRequires:	mvn(com.github.tomakehurst:wiremock)				#FIXME: not packaged yew
#BuildRequires:	mvn(org.assertj:assertj-swing-junit)				#FIXME: not packaged yew
#   required by gradle plugins
BuildRequires:	mvn(org.python:jython-standalone)
BuildRequires:	mvn(com.sun.xml.bind:jaxb-xjc)

Requires:	citationstyles-locales
Requires:	citationstyles-styles
Requires:	libreoffice-java				#mvn(org.openoffice:juh)
Requires:	libreoffice-java				#mvn(org.openoffice:jurt)
Requires:	libreoffice-java				#mvn(org.openoffice:ridl)
Requires:	libreoffice-java				#mvn(org.openoffice:unoil)
Requires:	mvn(commons-cli:commons-cli) >= 1.3.1
Requires:	swingx <= 1.6.1					#mvn(org.swinglabs:swingx:1.6.1)

BuildArch:      noarch

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

%files -f .mfiles
%{_bindir}/%{name}
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

%package javadoc
Summary:	Javadoc for JabRef
Group:		Documentation
BuildArch:	noarch

%description javadoc
API documentation for JabRef.

%files javadoc -f .mfiles-javadoc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

# Delete all JARs and classes
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Apply all patches
%patch1 -p1 -b .gradle_local
%patch2 -p1 -b .plugin
%patch3 -p1 -b .deps
%patch4 -p1 -b .maven
%patch5 -p1 -b .xjc
%patch6 -p1 -b .updates
%patch7 -p1 -b .osx
%patch8 -p1 -b .guava
%patch9 -p1 -b .citationstyles

# copy xjc schemas
cp %{SOURCE10} %{SOURCE11} src/main/resources/xjc/mods

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

#  fix groupId:asrtifactId
sed -i -e 's|com.github.bkromhout:java-diff-utils|com.googlecode.java-diff-utils:diffutils|' build.gradle

#  add missing maven metadata
#     SwingX
sed -e 's|@LIBDIR@|%{_libdir}|g' %{SOURCE100} > swingx-maven-metadata.xml
%mvn_config resolverSettings/metadataRepositories/repository swingx-maven-metadata.xml
#     LibreOffice
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE101}

#   remove OSx connector
rm -fr src/main/java/osx/

# Fix LibreOffice path
sed -i -e '{
	     s|/opt/openoffice.org3|%{_libdir}/libreoffice|
	     s|/usr/lib/openoffice/program/soffice|%{_libdir}/libreoffice/program/soffice|
	     s|/opt/openoffice.org/basis3.0|%{_libdir}/libreoffice|
	   }' src/main/java/net/sf/jabref/preferences/JabRefPreferences.java


%build
# jar
gradle build javadoc install -x test --offline -s

# FIXME: remove dependencies without maven stuff from pom.xml
%pom_remove_dep org.openoffice:jurt build/poms/pom-default.xml
%pom_remove_dep org.openoffice:ridl build/poms/pom-default.xml
%pom_remove_dep org.openoffice:juh build/poms/pom-default.xml
%pom_remove_dep org.openoffice:unoil build/poms/pom-default.xml
%pom_remove_dep org.swinglabs.swingx:swingx-core build/poms/pom-default.xml

# mv build/libs/%{oname}-%{version}.jar build/libs/%{name}.jar
%mvn_artifact build/poms/pom-default.xml build/libs/%{oname}-%{version}.jar
%mvn_file :%{oname} %{name}

%install
%mvn_install -J build/docs/javadoc

# launcher
%jpackage_script net.sf.jabref.JabRefMain "" "" antlr:antlr3:antlr3-runtime:antlr4:antlr4-runtime:bcprov:citeproc-java:commons-cli:commons-codec:commons-lang3:commons-logging:fontbox:glazedlists:guava:httpcomponents/client:java-diff-utils/diffutils:jbibtex:java-string-similarity:jempbox:jgoodies-common:jgoodies-forms:jgoodies-looks:json:jsoup:lgooddatepicker/LGoodDatePicker:libreoffice/juh:libreoffice/jurt:libreoffice/ridl:libreoffice/unoil:mysql-connector-java:log4j:log4j/log4j-api:log4j/log4j-core:log4j/log4j-jcl:pdfbox:pgjdbc-ng:spin:stringtemplate4:swingx:unirest-java:xmlunit-core:xmlunit-matchers:jabref jabref true
#:orange-extensions


# icons
# FIXME: imagemagick produces empty images (maybe
#	a bug in inkskape maybe a bug into the icon) and
#	rsvg-convert works properly for png only
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

