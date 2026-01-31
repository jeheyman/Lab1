from launch import LaunchDescription
from launch_ros.actions import Node

# run this launch file with the following command:
# ros2 launch chatterbot.launch.py

def generate_launch_description():

    
    publisher = Node(
        package='mypubsub',
        executable='publisher',
        name='publisher',
        remappings=[('chatter', 'chatter1')]
    )

    subscriber = Node(
        package='mypubsub',
        executable='subscriber',
        name='subscriber',
        remappings=[('chatter', 'chatter1')]
    )
    
    launch_description = LaunchDescription([
        publisher,
        subscriber,
    ])

    return launch_description