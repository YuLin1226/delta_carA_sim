# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/yulin/carA_sim_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/yulin/carA_sim_ws/build

# Utility rule file for run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.

# Include the progress variables for this target.
include fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/progress.make

fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml:
	cd /home/yulin/carA_sim_ws/build/fiducial_slam && ../catkin_generated/env_cached.sh /usr/bin/python /opt/ros/kinetic/share/catkin/cmake/test/run_tests.py /home/yulin/carA_sim_ws/build/test_results/fiducial_slam/rostest-test_init_map_aruco.xml "/opt/ros/kinetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/yulin/carA_sim_ws/src/fiducial_slam --package=fiducial_slam --results-filename test_init_map_aruco.xml --results-base-dir \"/home/yulin/carA_sim_ws/build/test_results\" /home/yulin/carA_sim_ws/src/fiducial_slam/test/init_map_aruco.xml "

run_tests_fiducial_slam_rostest_test_init_map_aruco.xml: fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml
run_tests_fiducial_slam_rostest_test_init_map_aruco.xml: fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/build.make

.PHONY : run_tests_fiducial_slam_rostest_test_init_map_aruco.xml

# Rule to build all files generated by this target.
fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/build: run_tests_fiducial_slam_rostest_test_init_map_aruco.xml

.PHONY : fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/build

fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/clean:
	cd /home/yulin/carA_sim_ws/build/fiducial_slam && $(CMAKE_COMMAND) -P CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/cmake_clean.cmake
.PHONY : fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/clean

fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/depend:
	cd /home/yulin/carA_sim_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/yulin/carA_sim_ws/src /home/yulin/carA_sim_ws/src/fiducial_slam /home/yulin/carA_sim_ws/build /home/yulin/carA_sim_ws/build/fiducial_slam /home/yulin/carA_sim_ws/build/fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : fiducial_slam/CMakeFiles/run_tests_fiducial_slam_rostest_test_init_map_aruco.xml.dir/depend

