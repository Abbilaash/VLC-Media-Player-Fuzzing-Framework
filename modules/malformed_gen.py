import os
import random

# Path to the folder containing video and audio files
INPUT_FOLDER = r"A:\PROJECTS\VLC-Media-Player-Fuzzing-Framework\modules\samples"
OUTPUT_FOLDER = r"A:\PROJECTS\VLC-Media-Player-Fuzzing-Framework\modules\malformed_samples"

# Make sure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def generate_malformed_file(input_file, output_file, corruption_level=0.01):
    """
    Generates a malformed version of the given file by corrupting random bytes.
    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to save the malformed file.
        corruption_level (float): Percentage of bytes to corrupt in the file.
    """
    with open(input_file, "rb") as f:
        data = bytearray(f.read())  # Load the file as a mutable byte array

    # Calculate the number of bytes to corrupt
    num_corruptions = int(len(data) * corruption_level)
    for _ in range(num_corruptions):
        # Choose a random byte position and corrupt it
        pos = random.randint(0, len(data) - 1)
        data[pos] = random.randint(0, 255)

    # Save the malformed file
    with open(output_file, "wb") as f:
        f.write(data)
    print(f"Malformed file created: {output_file}")

def process_folder(input_folder, output_folder, corruption_level=0.01):
    """
    Process all video and audio files in a folder to create malformed files.
    Args:
        input_folder (str): Path to the input folder.
        output_folder (str): Path to the output folder.
        corruption_level (float): Percentage of bytes to corrupt in the files.
    """
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            # Get the file extension
            _, ext = os.path.splitext(file_name)
            ext = ext.lower()

            # Only process common video and audio file formats
            if ext in [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".mp3", ".wav", ".flac", ".ogg", ".aac", ".webm", ".3gp"]:
                input_file = os.path.join(root, file_name)
                output_file = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_malformed{ext}")

                # Generate a malformed file
                generate_malformed_file(input_file, output_file, corruption_level)

if __name__ == "__main__":
    process_folder(INPUT_FOLDER, OUTPUT_FOLDER, corruption_level=0.02)
