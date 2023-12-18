from PIL import Image

def rotate_image(input_path, output_path, degrees):
    # Åpne bildet
    image = Image.open(input_path)

    # Utfør rotasjon
    rotated_image = image.rotate(degrees)

    # Lagre det roterte bildet
    rotated_image.save(output_path)






# Bruk funksjonen
input_image_path = "path/to/your/image.jpg"
output_image_path = "path/to/your/rotated_image.jpg"

# Rotere 90 grader med klokken
# rotate_image(input_image_path, output_image_path, 90)

# Rotere 90 grader mot klokken
# rotate_image(input_image_path, output_image_path, -90)

# Rotere 180 grader
# rotate_image(input_image_path, output_image_path, 180)





input_image_path = input("Oppgi hvilket bilde du vil rotere: ")
output_image_path = input("Oppgi navnet på bildet som skal eksporteres: ")
degrees = int(input("Oppgi hvor mange grader du vil rotere bildet: "))

# Kjøre programmet
rotate_image(input_image_path, output_image_path, degrees)