Name:		liquidlnf
Group:		Graphics
Summary:	Java look and feel based on the Mosfet Liquid KDE 3.x theme
Version:	2.9.1
License:	LGPLv2.1
Release:	2
# register an user at https://www.dev.java.net
# cvs -d :pserver:username@cvs.dev.java.net:/cvs checkout liquidlnf
# cp -far liquidlnf liquidlnf-2.9.1
# find liquidlnf-2.9.1 -name CVS -type d -exec rm -fr {} \; 2> /dev/null
Source0:	liquidlnf-2.9.1.tar.xz
URL:		https://liquidlnf.dev.java.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

#-----------------------------------------------------------------------
BuildRequires:  ant
BuildRequires:  ant-swing
BuildRequires:  java-rpmbuild
BuildRequires:	jpackage-utils

#-----------------------------------------------------------------------
Patch0:		liquidlnf-2.9.1-SwingUtilities2.patch

#-----------------------------------------------------------------------
%description
Liquid look & feel

The goal of this project is to provide a look and feel based on the
Mosfet Liquid KDE 3.x theme.

#-----------------------------------------------------------------------
%prep
%setup -q

%patch0 -p1

#-----------------------------------------------------------------------
%define ant	JAVA_HOME=%{java_home} ant

%build
%ant

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{_javadir}/liquidlnf
cp -far dist/bin/* %{buildroot}%{_javadir}/liquidlnf

#-----------------------------------------------------------------------
%files
%defattr(-,root,root)
%{_javadir}/liquidlnf


%changelog
* Fri Jan 07 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.9.1-1mdv2011.0
+ Revision: 629669
- Import liquidlnf 2.9.1
- liquidlnf

