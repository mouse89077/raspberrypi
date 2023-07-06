import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
from datetime import datetime
import os

FILEPATH= os.path.join(os.path.expanduser('~'), 'pygpsclient', 'data_pos.txt')
cache=[]


lat = String()
lon = String()

class XcorpsGPSRTK(Node):

    def __init__(self):
        super().__init__('xcorps_gps_rtk')
        
        self.namespace_OS = '/OS'
        self.lat_publisher_ = self.create_publisher(String, self.namespace_OS + '/gps/lat', 10)
        self.lon_publisher_ = self.create_publisher(String, self.namespace_OS + '/gps/lon', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
    
        while True:
            try:
                f = open(FILEPATH, 'r')
                data=f.read()
                f.close
                break
            except:
                continue
        
        cache=data.split('/')
        if len(cache)>2:
            lat.data = str(cache[0].strip())
            lon.data = str(cache[1].strip())

        self.lat_publisher_.publish(lat)
        self.lon_publisher_.publish(lon)

        self.get_logger().info('Latitude is: "%s"' % lat.data)
        self.get_logger().info('Longitude is: "%s"' % lon.data)



def main(args=None):
    rclpy.init(args=args)

    xcorps_gps_rtk = XcorpsGPSRTK()

    rclpy.spin(xcorps_gps_rtk)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    xcorps_gps_rtk.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
