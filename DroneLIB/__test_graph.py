import random
import matplotlib.pyplot as plt
from droneConstructor import Drone

# Create a drone instance
drone = Drone()

# Set drone parameters for stability
drone.mass = 0.5
drone.thrust_coefficient = 0.8
drone.drag_coefficient = 0.1

# Set simulation parameters
total_simulation_time = 10.0  # total simulation time in seconds

# Simulate the flight and obtain altitude data
altitude_data = []
time_data = []

dt = 0.01  # time step size
num_steps = int(total_simulation_time / dt)

for step in range(num_steps):
    # Generate random throttle command between 0 and 1
    throttle_command = random.uniform(0.5, 1.0)

    # Simulate one time step with the random throttle command
    drone.simulate(dt, throttle_command)

    # Store altitude and time data
    altitude_data.append(drone.position[2])
    time_data.append(step * dt)

# Plot altitude over time
plt.figure(figsize=(10, 5))
plt.plot(time_data, altitude_data)
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Drone Altitude over Time')
plt.grid(True)
plt.show()

# Analyze stability
drone.analyze_stability()

# Evaluate performance
drone.evaluate_performance()
