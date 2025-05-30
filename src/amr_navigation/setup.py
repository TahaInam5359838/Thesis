from setuptools import setup

package_name = 'amr_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='omron',
    maintainer_email='guanyewtan@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_server = amr_navigation.action_server:main',
            'goto_goal = amr_navigation.goto_goal:main',
            'goto_goal_demo = amr_navigation.goto_goal_demo:main',
            'dock = amr_navigation.dock:main',
            'goto_point = amr_navigation.goto_point:main',
            'localize_at_point = amr_navigation.localize_at_point:main',
            'execute_macro = amr_navigation.execute_macro:main'
        ],
    },
)
