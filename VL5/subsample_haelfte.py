sensor_werte = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
# soll sein [3.2, 2.8, 6.4]
print(len(sensor_werte))
print(len(sensor_werte) / 2 )
print(int(len(sensor_werte) / 2) )

print(sensor_werte[:int(len(sensor_werte)/2) + 1:2])