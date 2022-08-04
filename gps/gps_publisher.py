import rclpy
import serial

from rclpy.node import Node

from std_msgs.msg import String


class GPSPublisher(Node):

    def __init__(self):
        super().__init__('GPS_publisher')
        self.publisher_ = self.create_publisher(String, 'gps_data', 10)
        timer_period = 5.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.ser = serial.Serial('/dev/ttyUSB0', 4800)

    def timer_callback(self):
        msg = String()
        msg.data = ''
        k = 0
        while k < 18 :
            data = self.ser.readline()
            if data and str(data)[2]=='$':
                data = str(data)
                n = len(data)
                data_str = data[2:n-4]
                msg.data += data_str + '\n'
            else :
                k = k-1
            k=k+1
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    GPS_publisher = GPSPublisher()

    rclpy.spin(GPS_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    GPS_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()