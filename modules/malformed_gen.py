import random

def create_malformed_file(input_file: str, output_file: str):
    with open(input_file, "rb") as f: #read original .mp4 as byte array
        data = bytearray(f.read())
    
    print(f"Original file size: {len(data)} bytes")

    # Perform mutations on the byte array to corrupt the file
    for _ in range(10):  # Perform 10 random mutations
        index = random.randint(0, len(data) - 1)  # Choose a random position
        data[index] = random.randint(0, 255)      # Replace with a random byte

    # Write the mutated byte array to a new file
    with open(output_file, "wb") as f:
        f.write(data)
    
    print(f"Malformed file written to: {output_file}")

input_file = "A:/PROJECTS/VLC-Media-Player-Fuzzing-Framework/modules/test_play.mp4"
output_file = "modules/malformed_sample.mp4"
create_malformed_file(input_file, output_file)
