from pathlib import Path
import cv2

def delete_non_face_images(image_dir):
    """
    Deletes all images in the specified directory that do not contain a face.

    Args:
        image_dir (str): The directory containing the images.
    """
    # Convert the path to a Path object
    image_dir_path = Path(image_dir)

    # Check if the provided directory exists
    if not image_dir_path.is_dir():
        print(f"The directory {image_dir} does not exist.")
        return

    # Initialize the face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Iterate over all image files in the directory
    for image_path in image_dir_path.glob('*'):
        if image_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']:
            # Read the image
            image = cv2.imread(str(image_path))
            if image is None:
                print(f"Could not read {image_path}. Skipping.")
                continue

            # Convert the image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # If no faces are detected, delete the image
            if len(faces) == 0:
                print(f"No faces found in {image_path}. Deleting...")
                image_path.unlink()

    print("Process completed.")

# Example usage
pdir = Path(r'C:\dumpinggrounds\stable_video\faceless')
for p in pdir.iterdir():
    if p.is_dir():
        delete_non_face_images(str(p))
