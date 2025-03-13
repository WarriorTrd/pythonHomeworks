import numpy as np
from PIL import Image

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)
temps_f = np.array([32, 68, 100, 212, 77])
temps_c = vectorized_f_to_c(temps_f)
print("Temps in Celsius:", temps_c)

def power_function(base, exp):
    return base ** exp

vectorized_power = np.vectorize(power_function)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
powered_values = vectorized_power(bases, exponents)
print("Powered values:", powered_values)

coeffs_1 = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
consts_1 = np.array([7, 4, 5])
sol_1 = np.linalg.solve(coeffs_1, consts_1)
print("Solution for system 1 (x, y, z):", sol_1)

coeffs_2 = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
consts_2 = np.array([12, -5, 15])
sol_2 = np.linalg.solve(coeffs_2, consts_2)
print("Solution for circuit (I1, I2, I3):", sol_2)

image = Image.open("images/birds.jpg")
image_array = np.array(image)

flipped_image = np.flipud(np.fliplr(image_array))

noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
noisy_image = np.clip(image_array + noise, 0, 255)

brightened_image = np.clip(image_array + 40, 0, 255)

h, w, _ = image_array.shape
mask_size = 100
start_x, start_y = (w // 2 - mask_size // 2, h // 2 - mask_size // 2)
image_array[start_y:start_y + mask_size, start_x:start_x + mask_size] = 0
masked_image = image_array

Image.fromarray(flipped_image).save("flipped_birds.jpg")
Image.fromarray(noisy_image).save("noisy_birds.jpg")
Image.fromarray(brightened_image).save("brightened_birds.jpg")
Image.fromarray(masked_image).save("masked_birds.jpg")