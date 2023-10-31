%define		vendor_version	0.14.1

Summary:	Official Go language server developed by the Go team
Name:		gopls
Version:	0.14.1
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://github.com/golang/tools/archive/gopls/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2c62f3480a00f593fd0daf162da6ebdc
Source1:	%{name}-vendor-%{vendor_version}.tar.xz
# Source1-md5:	b56d52317eb9cb2d8725df1b40033e4a
URL:		https://pkg.go.dev/golang.org/x/tools/gopls
BuildRequires:	golang >= 1.18
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
