Name: mythes-sv
Summary: Swedish thesaurus
Version: 1.2
Release: 2.1%{?dist}
Source: http://extensions.services.openoffice.org/files/934/3/SwedishThesaurus.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/SweThes
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: MIT
BuildArch: noarch

%description
Swedish thesaurus.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_sv_SE.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_sv_SE_v2.dat
cp -p dictionaries/th_sv_SE.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_sv_SE_v2.idx
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s th_sv_SE_v2.dat "th_"$lang"_v2.dat"
        ln -s th_sv_SE_v2.idx "th_"$lang"_v2.idx"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Info-en.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2-2.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Caolan McNamara <caolanm@redhat.com> - 1.2-1
- latest version

* Thu Mar 05 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090225-1
- initial version
