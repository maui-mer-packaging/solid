# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kf5-solid

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 1 integration module that provides hardware information
Version:    4.99.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-solid.yaml
Requires:   kf5-filesystem
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  kf5-rpm-macros
BuildRequires:  libupnp-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
Provides:   kf5-solid-runtime = %{version}-%{release}
Provides:   kf5-solid-runtime%{?_isa} = %{version}-%{release}

%description
Solid provides the following features for application developers:
 - Hardware Discovery
 - Power Management
 - Network Management


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications |
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
%kf5_make_install
%find_lang solid5_qt --with-qt --all-name
# << install post

%files -f solid5_qt.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README.md TODO
%{_kf5_qmldir}/org/kde/solid
%{_kf5_libdir}/libKF5Solid.so.*
%{_kf5_bindir}/solid-hardware5
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/solid_version.h
%{_kf5_includedir}/Solid
%{_kf5_libdir}/libKF5Solid.so
%{_kf5_libdir}/cmake/KF5Solid
%{_kf5_archdatadir}/mkspecs/modules/qt_Solid.pri
# >> files devel
# << files devel
