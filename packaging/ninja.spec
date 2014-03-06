Name:           ninja
Version:        1.4.0
Release:        0
License:        Apache-2.0
Summary:        Ninja build system
Url:            http://martine.github.com/ninja/
Group:          System/Utilities
Source:         %{name}.tar.bz2
Source1001:     ninja.manifest

BuildRequires:  python

%description
Ninja is a small build system with a focus on speed.
http://martine.github.com/ninja/

See the manual -- http://martine.github.com/ninja/manual.html or
doc/manual.asciidoc included in the distribution -- for background
and more details.

%prep
%setup -q
cp %{SOURCE1001} .


%build
python ./bootstrap.py 

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 ninja %{buildroot}%{_bindir}/ninja

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/ninja
%license COPYING

