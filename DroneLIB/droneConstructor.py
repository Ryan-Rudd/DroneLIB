import random
import math
import matplotlib.pyplot as plt

class Drone:
    def __init__(self):
        # Drone properties
        self.mass = 1.0
        self.thrust_coefficient = 0.1
        self.drag_coefficient = 0.01

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

    def apply_thrust(self, throttle):
        # Compute the thrust produced by each propeller
        self.throttle = throttle
        self.propeller_thrust = self.thrust_coefficient * self.throttle

    def compute_drag(self):
        # Compute the total drag force
        velocity_magnitude = math.sqrt(sum(v ** 2 for v in self.velocity))
        drag_force = [-self.drag_coefficient * v * velocity_magnitude for v in self.velocity]
        return drag_force

    def compute_gravity(self):
        # Compute the gravity force
        gravity_force = [0.0, 0.0, -self.mass * 9.81]
        return gravity_force

    def compute_net_force(self):
        # Compute the net force acting on the drone
        total_thrust = self.propeller_thrust * math.cos(self.pitch) * math.cos(self.roll)
        total_drag = self.compute_drag()
        total_gravity = self.compute_gravity()

        net_force = [total_thrust + drag + gravity for drag, gravity in zip(total_drag, total_gravity)]
        return net_force

    def update_acceleration(self):
        # Update the acceleration using the current net force
        self.acceleration = [force / self.mass for force in self.compute_net_force()]

    def update_velocity(self, dt):
        # Update the velocity using the current acceleration
        self.velocity = [v + a * dt for v, a in zip(self.velocity, self.acceleration)]

    def update_position(self, dt):
        # Update the position using the current velocity
        self.position = [p + v * dt for p, v in zip(self.position, self.velocity)]

    def simulate(self, dt, throttle):
        # Simulate the motion of the drone for one time step
        self.apply_thrust(throttle)
        self.update_acceleration()
        self.update_velocity(dt)
        self.update_position(dt)

    def simulate_flight(self, time, throttle):
        # Simulate the flight of the drone for the specified time
        dt = 0.01  # time step size
        num_steps = int(time / dt)
        altitude_data = []
        for _ in range(num_steps):
            self.simulate(dt, throttle)
            altitude_data.append(self.position[2])

        return altitude_data

    def analyze_stability(self):
        # Analyze the stability of the drone
        roll_stability = abs(sum(self.angular_acceleration) / len(self.angular_acceleration)) / (abs(sum(self.angular_velocity) / len(self.angular_velocity)) + 1e-6)
        pitch_stability = abs(sum(self.angular_acceleration) / len(self.angular_acceleration)) / (abs(sum(self.angular_velocity) / len(self.angular_velocity)) + 1e-6)

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
        
        return roll_stability, pitch_stability

    def evaluate_performance(self):
        # Evaluate the performance of the drone
        # Calculate the average velocity and acceleration
        average_velocity = sum(self.velocity) / 3
        average_acceleration = sum(self.acceleration) / 3

        # Print performance evaluation results
        print("Performance Evaluation:")
        print(f"Average Velocity: {average_velocity}")
        print(f"Average Acceleration: {average_acceleration}")