from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
import sys
from ament_index_python.packages import get_package_share_directory

# Add shared_config/config to Python path
shared_config_path = os.path.join(get_package_share_directory('shared_config'), 'config')
sys.path.insert(0, shared_config_path)
import ip_settings


def generate_launch_description():
    om_aiv_util_launch = os.path.join(get_package_share_directory('om_aiv_util'), 'launch', 'server.launch.py')
    amr_visualisation_launch = os.path.join(get_package_share_directory('amr_visualisation'), 'launch', 'display.launch.py')
    tm12s_moveit_launch = os.path.join(get_package_share_directory('tm12s_moveit_config'), 'launch', 'tm12s_run_move_group.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(om_aiv_util_launch)
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(amr_visualisation_launch)
        ),
        ExecuteProcess(
            cmd=['ros2', 'run', 'tm_driver', 'tm_driver', f'robot_ip:={ip_settings.TM_IP}'],
            output='screen'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(tm12s_moveit_launch)
        ),
    ])
