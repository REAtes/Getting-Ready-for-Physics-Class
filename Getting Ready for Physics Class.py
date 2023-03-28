# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  return (f_temp - 32 ) * 5/9

# Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input.
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)


def c_to_f(c_temp):
  return c_temp * (9/5) + 32
# Define a variable c0_in_fahrenheit and set it equal to the value of c_to_f with 0 as an input.
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Define a function called get_energy that takes in mass and c. 
# c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8. 
# get_energy should return mass multiplied by c squared.
# Test get_energy by using it on bomb_mass, with the default value of c. Save the result to a variable called bomb_energy.
def get_energy(mass, c=3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Define a final function called get_work that takes in mass, acceleration, and distance.
# Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result.
# Test get_work by using it on train_mass, train_acceleration, and train_distance. Save the result to a variable called train_work.

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters") 




