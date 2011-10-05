%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from yajl-ruby-0.8.2.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname yajl-ruby
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%define __arch_install_post   /usr/lib/rpm/check-rpaths

Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library
Name: ruby-enterprise-rubygem-%{gemname}
Version: 0.8.2
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/brianmario/yajl-ruby
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(rake-compiler) >= 0.7.5
Requires: ruby-enterprise-rubygem(rspec) >= 2.0.0
Requires: ruby-enterprise-rubygem(activesupport) >= 0
Requires: ruby-enterprise-rubygem(json) >= 0
BuildRequires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.8.2-2.hhg
- Rebuild for Ruby Enterprise Edition

* Thu May 05 2011 Sergio Rubio <rubiojr@frameos.org> - 0.8.2-2
- buildrequire ruby-devel

* Thu Apr 14 2011 Sergio Rubio <rubiojr@frameos.org> - 0.8.2-1
- Initial package
