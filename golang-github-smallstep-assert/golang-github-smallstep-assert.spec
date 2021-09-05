# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/smallstep/assert
%global goipath         github.com/smallstep/assert
%global commit          82e2b9b3b262f82582f3c8795e6804c1cd131475

%gometa

%global common_description %{expand:
A simple assertion framework for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        A simple assertion framework for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Sep 05 2021 Petr Menšík <pemensik@redhat.com> - 0-0.1%{?dist}.20210905git82e2b9b
- Initial package

