import matplotlib.pyplot as plt

waktu = [0, 1, 2, 3, 4, 5]        # menit
suhu  = [25, 26, 28, 27, 30, 29]  # celcius

plt.plot(waktu, suhu, marker='o')
plt.title('Temperature vs Time')
plt.xlabel('Waktu (menit)')
plt.ylabel('Suhu (°C)')
plt.grid(True)
plt.savefig('temp_vs_time.png')
plt.show()