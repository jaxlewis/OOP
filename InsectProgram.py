import InsectClass as I

mosquito = I.Insect("mosquito", 2, 4)
housefly = I.Insect("housefly", 2, 4)

mosquito.flight_length()
housefly.flight_length()

print(f"The {mosquito.get_name()} can fly up to {mosquito.get_miles()}")
print(f"The {housefly.get_name()} can fly up to {housefly.get_miles()}")

# still need to create an instance and print how many miles the insect can fly
# bhoj said that we are making a house fly and a mosquito
