# Some functions that will help Physics students to calculate fundamental properties.

# defined variables.
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# takes a temperature in Fahrenheit and coverts it to a temperature in Celcius.
def f_to_c(f_temp):
    c_temp = f_temp - 32 * 5/9 
    return c_temp
f100_in_celsius = f_to_c(100)

# takes a temperature in Celcius and coverts it to a temperature in Fahrenheit.
def c_to_f(c_temp):
    f_temp = c_temp * 9/5 + 32 
    return f_temp
co_in_fahrenheit = c_to_f(0)

# takes mass multiplied by acceleration and defines 'force'. 
def get_force(mass, acceleration):
    get_force = mass * acceleration
    return get_force
train_force = get_force(train_mass,train_acceleration)
print("The train supplies " + str(train_force) + " Newtons of force.")

# takes mass multiplied by c squared (c set to the speed of light) and defines 'energy'.
def get_energy(mass, c=3*10**8):
    get_energy = mass * c**2
    return get_energy
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " +str(bomb_energy) + " Joules.")

# takes force multiplied by distance and defines 'work'.
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# Testing 'work' on the train variables.
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

