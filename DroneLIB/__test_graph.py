import matplotlib.pyplot as plt 
from droneConstructor import Drone

drone= Drone()

throttle_command = 0.5

# Set simulation parameters
total_simulation_time = 10.0  # total simulation time in seconds
dt = 0.01  # time step size

# Number of time steps
num_steps = int(total_simulation_time / dt)

# Lists to store simulation data
time_data = []
altitude_data = []

# Simulate the drone
for step in range(num_steps):
    # Simulate one time step
    drone.simulate(dt, throttle_command)
    
    # Store simulation data
    time_data.append(step * dt)
    altitude_data.append(drone.position[2])

# Plot altitude over time
plt.figure(figsize=(10, 5))
plt.plot(time_data, altitude_data)
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Drone Altitude over Time')
plt.grid(True)
plt.show()
