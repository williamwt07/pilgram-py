from PIL import Image

def rotate_image(input_path, output_path, degrees):
    # Åpne bildet
    print(f"Åpner bildet: {input_path}")
    image = Image.open(input_path)

    # Utfør rotasjon
    rotated_image = image.rotate(degrees)

    # Lagre det roterte bildet
    rotated_image.save(output_path)
    print(f"Lagret rotert bilde som: {output_path}")

def resize_image(input_path, output_path, target_width):
    # Åpne bildet
    print(f"Åpner bildet: {input_path}")
    image = Image.open(input_path)

    # Beregn høyde proporsjonalt for å opprettholde sideforholdet
    width_percent = (target_width / float(image.size[0]))
    target_height = int((float(image.size[1]) * float(width_percent)))

    # Endre størrelsen på bildet
    resized_image = image.resize((target_width, target_height), Image.LANCZOS)

    # Lagre det endrede bildet
    resized_image.save(output_path)
    print(f"Lagret endret bilde som: {output_path}")

# Bruk funksjonene
input_image_path = input("Oppgi hvilket bilde du vil rotere og endre størrelsen på: ")
degrees = int(input("Oppgi hvor mange grader du vil rotere bildet: "))

# Kjør roteringsfunksjonen
output_rotated_path = input("Oppgi navnet på det roterte bildet: ")
rotate_image(input_image_path, output_rotated_path, degrees)

# Oppdater sti til det roterte bildet
input_rotated_image_path = output_rotated_path

# Kjør endringsfunksjonen
output_resized_path = input("Oppgi navnet på det endrede bildet: ")
target_width = 1080
resize_image(input_rotated_image_path, output_resized_path, target_width)

print("Programmet fullført.")
