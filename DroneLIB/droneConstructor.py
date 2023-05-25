import matplotlib.pyplot as plt

class Drone:
    def __init__(self):
        # Default parameters
        self.mass = 1.0
        self.thrust_coefficient = 0.1
        self.drag_coefficient = 0.01

        # Drone configuration
        self.number_of_propellers = 4
        self.propeller_radius = 0.1
        self.propeller_thrust = 0.0

        # State variables
        self.position = [0.0, 0.0, 0.0]  # [x, y, z]
        self.velocity = [0.0, 0.0, 0.0]  # [Vx, Vy, Vz]
        self.acceleration = [0.0, 0.0, 0.0]  # [Ax, Ay, Az]
        self.orientation = [0.0, 0.0, 0.0]  # [Roll, Pitch, Yaw]
        self.angular_velocity = [0.0, 0.0, 0.0]  # [P, Q, R]
        self.angular_acceleration = [0.0, 0.0, 0.0]  # [P_dot, Q_dot, R_dot]

        # Control variables
        self.throttle = 0.0
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw_rate = 0.0

        # Battery information
        self.battery_voltage = 12.0
        self.battery_capacity = 5000.0
        self.battery_remaining = 100.0

        # GPS information
        self.gps_latitude = 0.0
        self.gps_longitude = 0.0
        self.gps_altitude = 0.0
        self.gps_speed = 0.0

        # Camera and sensors
        self.camera_enabled = False
        self.camera_resolution = (640, 480)
        self.imu_enabled = True
        self.gyroscope_enabled = True
        self.accelerometer_enabled = True

        # Aerodynamic properties
        self.wing_area = 0.0
        self.coefficient_of_lift = 0.0
        self.coefficient_of_drag = 0.0

        # Motor properties
        self.motor_max_speed = 1000.0
        self.motor_min_speed = 0.0

        # Environmental properties
        self.air_density = 1.225

        # Sensor noise parameters
        self.accelerometer_noise = 0.0
        self.gyroscope_noise = 0.0

        # Controller gains
        self.roll_pid_gain = [0.0, 0.0, 0.0]
        self.pitch_pid_gain = [0.0, 0.0, 0.0]
        self.yaw_pid_gain = [0.0, 0.0, 0.0]

        self.MAX_ACCELERATION = 30.0  # Maximum acceleration (m/s^2)
        self.MAX_VELOCITY = 50.0  # Maximum velocity (m/s)

    def apply_thrust(self, throttle):
        # Ensure throttle is in the range [0, 1]
        throttle = max(0.0, min(1.0, throttle))
        self.throttle = throttle

        # Compute the thrust produced by each propeller
        self.propeller_thrust = self.thrust_coefficient * self.throttle

        # Compute the total thrust produced by all propellers
        total_thrust = self.number_of_propellers * self.propeller_thrust

        return total_thrust

    def compute_drag(self):
        # Compute the total drag force
        total_drag = self.drag_coefficient * self.velocity[2] ** 2
        return total_drag

    def compute_acceleration(self, total_thrust, total_drag):
        # Compute the net force in the z direction
        net_force = total_thrust - total_drag - (self.mass * 9.81)

        # Apply Newton's second law to compute acceleration
        self.acceleration[2] = net_force / self.mass

    def update_velocity(self, dt):
        # Update the velocity using the current acceleration
        for i in range(3):
            self.velocity[i] += self.acceleration[i] * dt
            # Check if velocity magnitude exceeds maximum
            if abs(self.velocity[i]) > self.MAX_VELOCITY:
                self.velocity[i] = self.MAX_VELOCITY if self.velocity[i] > 0 else -self.MAX_VELOCITY

    def update_position(self, dt):
        # Update the position using the current velocity
        for i in range(3):
            self.position[i] += self.velocity[i] * dt

    def simulate(self, dt, throttle):
        # Apply the throttle command
        total_thrust = self.apply_thrust(throttle)

        # Compute the drag force
        total_drag = self.compute_drag()

        # Compute the current acceleration
        self.compute_acceleration(total_thrust, total_drag)

        # Update velocity and position
        self.update_velocity(dt)
        self.update_position(dt)

    def simulate_flight(self, time):
        # Simulate the flight of the drone for the specified time
        dt = 0.01  # time step size
        num_steps = int(time / dt)
        altitude_data = []
        for step in range(num_steps):
            self.simulate(dt, self.throttle)
            altitude_data.append(self.position[2])

        return altitude_data

    def analyze_stability(self):
        # Analyze the stability of the drone
        # Calculate the roll and pitch stability metrics
        roll_stability = abs(self.angular_acceleration[0]) / abs(self.angular_velocity[0]) if self.angular_velocity[0] != 0 else float('inf')
        pitch_stability = abs(self.angular_acceleration[1]) / abs(self.angular_velocity[1]) if self.angular_velocity[1] != 0 else float('inf')

        # Determine stability status based on the metrics
        if roll_stability < 1.0 and pitch_stability < 1.0:
            stability_status = "Stable"
        else:
            stability_status = "Unstable"

        # Print stability analysis results
        print("Stability Analysis:")
        print(f"Roll Stability: {roll_stability}")
        print(f"Pitch Stability: {pitch_stability}")
        print(f"Stability Status: {stability_status}")



    def evaluate_performance(self):
        # Evaluate the performance of the drone
        # Calculate the average velocity and acceleration
        average_velocity = sum(self.velocity) / 3
        average_acceleration = sum(self.acceleration) / 3

        # Print performance evaluation results
        print("Performance Evaluation:")
        print(f"Average Velocity: {average_velocity}")
        print(f"Average Acceleration: {average_acceleration}")
