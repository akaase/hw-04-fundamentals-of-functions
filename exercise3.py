def ask_for_distance(person_name):
    return float(input(f'How far did {person_name} run (in feet)? '))

def ask_for_minutes(person_name, distance):
    return float(input(f'How many minutes did {person_name} run take to run {distance} feet? '))

def compute_speed(distance, min):
    sec = min * 60
    return distance/sec

def run(name):
    distance = ask_for_distance(name)
    mins = ask_for_minutes(name, distance)
    speed = compute_speed(distance, mins)
    return speed

speed1 = run('person 1')
speed2 = run('person 2')
speed3 = run('person 3')

# Award Ceremonies
if speed3 > speed2 and speed3 > speed1:
    print(f'Person 3 was the fastest at {speed3} f/s')
elif speed2 > speed3 and speed2 > speed1:
    print(f'Person 2 was the fastest at {speed2} f/s')
elif speed1 > speed3 and speed1 > speed2:
    print(f'Person 1 was the fastest at {speed1} f/s')
elif speed1 == speed2 and speed2 == speed3:
    print(f'Everyone tied at {speed1} m/s')

print('Well done everyone!')
