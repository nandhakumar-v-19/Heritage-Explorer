import os

# Correct absolute path to the folder
folder_path = r"C:/Users/Sathish.R/Desktop/Python Projects/tamilnadu_heritage/IMAGE_UPDATED"  # Change this to the correct path

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"Error: Folder '{folder_path}' not found!")
else:
    # Get all image filenames in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

    # Check if images exist in the folder
    if image_files:
        print("\n".join(image_files))  # Print image names
    else:
        print("No images found in the folder.")
