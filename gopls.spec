%define		vendor_version	0.16.0

Summary:	Official Go language server developed by the Go team
Name:		gopls
Version:	0.16.0
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://github.com/golang/tools/archive/gopls/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9900960222762d2012728709b8301c79
Source1:	%{name}-vendor-%{vendor_version}.tar.xz
# Source1-md5:	3f7cffe5a425e93688288df4ac5be615
URL:		https://pkg.go.dev/golang.org/x/tools/gopls
BuildRequires:	golang >= 1.19
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
gopls (pronounced "Go please") is the official Go language server
developed by the Go team. It provides IDE features to any
LSP-compatible editor.

%prep
%setup -q -n tools-%{name}-v%{version} -a1

%{__mkdir} .go-cache

%build
cd gopls
%__go build -v -mod=vendor -o target/gopls

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

cp -p gopls/target/gopls $RPM_BUILD_ROOT%{_bindir}/gopls

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc gopls/doc/*.md gopls/README.md
%attr(755,root,root) %{_bindir}/gopls
