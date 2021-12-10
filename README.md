
# FRA502_Nachata_Vongweeratorn


## Installation
1. Build package from source: navigate to the source folder of your catkin workspace and build this package using:
	```
	$ git clone https://github.com/nxmcha/FRA502-Nachata-Vongweeratorn-62340500030.git
	$ cd ..
	$ catkin_make
	```
2. Install Required dependencies:
	```
	$ sudo apt-get install ros-melodic-dwa-local-planner
	```

## Simultaneous Localization And Mapping (SLAM)

1. Load the robot in the Gazebo environment. 
	```
	$ roslaunch diff_drive_bot gazebo.launch 
	```
2. Launch the **slam_gmapping** node. This will also start **rviz** where you can visualize the map being created:
	```
	$ roslaunch diff_drive_bot gmapping.launch
	```
3. Move the robot around. 
	 
	 teleop using keyboard:
	 ```
	 $ rosrun diff_drive_bot keyboard_teleop.py 
	 ```
4. Move the robot in your environment till a satisfactory map is created. 
5. Save the map using:
	```
	$ rosrun map_server map_saver -f ~/test_map
	```
6. Copy the map file to ```~/diff_drive_bot/maps/``` directory and edit the .yaml file to match the path. 
	
## Autonomous Navigation
  
0. To use your generated map, edit ```/launch/amcl_move_base.launch``` and add map .yaml location and name to map_server node launch.
1. Load the robot in gazebo environment:
	```
	$ roslaunch diff_drive_bot gazebo.launch 
	```
2. Start the **amcl**, **move_base** and **rviz** nodes:
	```
	$ roslaunch diff_drive_bot amcl_move_base.launch
	```
3. In rviz, click on ***2D Pose Estimate*** and set initial pose estimate of the robot.
4. To move to a goal, click on ***2D Nav Goal*** to set your goal location and pose.  
## Speech Command
 
1. go to zone 1 จะทำการส่งอาหารให้กับลูกค้า
2.  เมื่อส่งเสร็จจะกลับไปยังตำแหน่งที่ตั้งหลักของหุ่น
3. สามารถไปยังโซนได้ทั้งหมด 4 โซน (1,2,3,4)

## Summary

 โปจเจคนี้เริ่มจากการวาด world และ urdf จากนั้นทำการ spawn หุ่นบน world ให้ได้ ต่อมาทำการ gmapping เพื่อทำแผนที่ให้กับหุ่นยนต์เพื่อวางแผนการเดิน จากนั้นทำ amcl 
และ movebase เพื่อหาตำแหน่งของหุ่นยนต์บนแผนที่และทำการเคลื่อนที่ใน rviz โดยใช้  2d navigation ก่อน และใช้โค้ด .py เพื่อสั่งการเดินจากตำแหน่งปัจจุบันไปยังตำแหน่งที่ต้องการ
อย่างสุดท้ายใช้ speechrecognition เพื่อทำให้เราสามารถสั่งใช้งานหุ่นยนต์ด้วยเสียงได้

## Problem
การเคลื่อนที่ของหุ่นยนต์ยังเคลื่อนที่ได้ไม่ดีพอ การปรับค่าใน params ได้ไม่ดี จึงทำให้การเคลื่อนที่ของหุ่นยนต์ไม่คงเส้นคงวา การเลี้ยวยังมีการชนขอบ
ความยากใน world ที่มีพื้นต่างระดับทำให้การเคลื่อนที่มีความยากขึ้น

Nachata Vongweeratorn
