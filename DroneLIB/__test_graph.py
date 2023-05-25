import random
import matplotlib.pyplot as plt
from droneConstructor import Drone

# Create a drone instance
drone = Drone()

# Set drone parameters for stability
drone.mass = 12.0001
drone.thrust_coefficient = 20.8
drone.drag_coefficient = 50.1

# Set simulation parameters
total_simulation_time = 10.0  # total simulation time in seconds

# Simulate the flight and obtain altitude data
altitude_data = []
time_data = []
roll_stability_data = []
pitch_stability_data = []

dt = 0.01  # time step size
num_steps = int(total_simulation_time / dt)

for step in range(num_steps):
    # Generate random throttle command between 0.5 and 1.0
    throttle_command = random.uniform(0.5, 1.0)

    # Simulate one time step with the random throttle command
    drone.simulate(dt, throttle_command)

    # Store altitude and time data
    altitude_data.append(max(drone.position[2], 0.0))  # Ensure non-negative altitude
    time_data.append(step * dt)

    # Analyze stability and store stability data
    roll_stability, pitch_stability = drone.analyze_stability()
    roll_stability_data.append(roll_stability)
    pitch_stability_data.append(pitch_stability)

# Plot altitude, roll stability, and pitch stability over time
plt.figure(figsize=(10, 5))
plt.plot(time_data, altitude_data, label='Altitude')
plt.plot(time_data, roll_stability_data, label='Roll Stability')
plt.plot(time_data, pitch_stability_data, label='Pitch Stability')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('Drone Performance')
plt.grid(True)
plt.legend()
plt.show()

# Analyze stability
drone.analyze_stability()

# Evaluate performance
drone.evaluate_performance()
