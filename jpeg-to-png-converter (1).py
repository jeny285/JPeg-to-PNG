from PIL import Image
import os

def convert_jpeg_to_png(input_path):
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError("Input file does not exist")
        
        # Check if input file is a JPEG
        if not input_path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError("Input file is not a JPEG image")
        
        # Open the JPEG image
        with Image.open(input_path) as img:
            # Create output filename
            output_path = os.path.splitext(input_path)[0] + '.png'
            
            # Convert and save as PNG
            img.save(output_path, 'PNG')
            
            return True, output_path
    
    except Exception as e:
        return False, str(e)

def main():
    print("JPEG to PNG Converter")
    print("--------------------")
    
    while True:
        # Get input file path
        input_path = input("\nEnter the path to the JPEG file (or 'q' to quit): ")
        
        if input_path.lower() == 'q':
            break
        
        # Attempt conversion
        success, result = convert_jpeg_to_png(input_path)
        
        if success:
            print(f"Conversion successful!")
            print(f"PNG image saved as: {result}")
        else:
            print(f"Error: {result}")
        
        # Ask if user wants to convert another image
        if input("\nConvert another image? (y/n): ").lower() != 'y':
            break
    
    print("Thank you for using the JPEG to PNG converter!")

if __name__ == "__main__":
    main()
