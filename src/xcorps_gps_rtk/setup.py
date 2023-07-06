from setuptools import find_packages, setup

package_name = 'xcorps_gps_rtk'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jiyoung Seo',
    maintainer_email='mouse890@snu.ac.kr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'xcorps_gps_rtk = xcorps_gps_rtk.xcorps_gps_rtk:main',
            'xcorps_gps_rtk_spd = xcorps_gps_rtk.xcorps_gps_rtk_spd:main',
        ],
    },
)
