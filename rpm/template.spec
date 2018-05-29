Name:           ros-kinetic-turtlebot3
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS turtlebot3 package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/turtlebot3
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-turtlebot3-bringup
Requires:       ros-kinetic-turtlebot3-description
Requires:       ros-kinetic-turtlebot3-example
Requires:       ros-kinetic-turtlebot3-navigation
Requires:       ros-kinetic-turtlebot3-slam
Requires:       ros-kinetic-turtlebot3-teleop
BuildRequires:  ros-kinetic-catkin

%description
ROS packages for the Turtlebot3 (meta package)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue May 29 2018 Pyo <pyo@robotis.com> - 1.0.0-0
- Autogenerated by Bloom

* Wed Mar 14 2018 Pyo <pyo@robotis.com> - 0.2.1-0
- Autogenerated by Bloom

* Mon Mar 12 2018 Pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

* Mon Aug 14 2017 Pyo <pyo@robotis.com> - 0.1.6-0
- Autogenerated by Bloom

* Thu May 25 2017 Pyo <pyo@robotis.com> - 0.1.5-0
- Autogenerated by Bloom

* Tue May 23 2017 Pyo <pyo@robotis.com> - 0.1.4-0
- Autogenerated by Bloom

* Mon Apr 24 2017 Pyo <pyo@robotis.com> - 0.1.3-0
- Autogenerated by Bloom

