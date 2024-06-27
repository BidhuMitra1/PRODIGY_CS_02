from PIL import Image

def encrypt_image(image, operation):
    encrypted_image = image.copy()
    pixels = encrypted_image.load()
    width, height = encrypted_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if operation == "swap":
                pixels[x, y] = (b, g, r)
            elif operation == "add_10":
                pixels[x, y] = ((r + 10) % 256, (g + 10) % 256, (b + 10) % 256)
            elif operation == "multiply_2":
                pixels[x, y] = ((r * 2) % 256, (g * 2) % 256, (b * 2) % 256)
            else:
                raise ValueError("Invalid operation")

    return encrypted_image

def decrypt_image(encrypted_image, operation):
    decrypted_image = encrypted_image.copy()
    pixels = decrypted_image.load()
    width, height = decrypted_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if operation == "swap":
                pixels[x, y] = (b, g, r)
            elif operation == "add_10":
                pixels[x, y] = ((r - 10) % 256, (g - 10) % 256, (b - 10) % 256)
            elif operation == "multiply_2":
                pixels[x, y] = ((r // 2) % 256, (g // 2) % 256, (b // 2) % 256)
            else:
                raise ValueError("Invalid operation")

    return decrypted_image

def main():
    while True:
        print("Image Encryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            image_path = input("Enter the path to the image: ")
            operation = input("Enter the operation (swap, add_10, multiply_2): ")
            image = Image.open(image_path)
            encrypted_image = encrypt_image(image, operation)
            encrypted_image.save("encrypted_image.png")
            print("Encrypted image saved as encrypted_image.png")

        elif choice == "2":
            image_path = input("Enter the path to the encrypted image: ")
            operation = input("Enter the operation (swap, add_10, multiply_2): ")
            encrypted_image = Image.open(image_path)
            decrypted_image = decrypt_image(encrypted_image, operation)
            decrypted_image.save("decrypted_image.png")
            print("Decrypted image saved as decrypted_image.png")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
