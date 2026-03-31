def calculate_real_size():
    print("--- Specimen Size Calculator ---")
    try:
        image_size = float(input("Enter the microscope image size (e.g., in mm): "))
        magnification = float(input("Enter the magnification (e.g., 40, 100, 400): "))
        
        real_size = image_size / magnification
        
        print(f"\nThe real life size of the specimen is: {real_size:.4f} units")
    except ValueError:
        print("Please enter valid numerical values.")
    except ZeroDivisionError:
        print("Magnification cannot be zero.")

if __name__ == "__main__":
    calculate_real_size()