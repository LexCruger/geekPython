start_distance = float(input('Start distance: '))
target_distance = float(input('Finish distance: '))

distance_ = start_distance
day_counter = 1

while distance_ < target_distance:
    day_counter += 1
    distance_ *= 1.1

print(day_counter)
