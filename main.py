import ffmpeg
import os

# Define input and output folders
input_folder = './'
output_folder = './cleaned'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Shows file being processed
        print(f"Processing: {filename}...")

        try:
            (
                ffmpeg
                .input(input_path)
                # vf for scale, an for audio, metadata for rotational thing
                .output(output_path, vf='scale=-1:480', an=None, metadata='s:v:0 rotate=0')
                .overwrite_output() # Overwrites if file exists
                .run(quiet=True)
            )
        except ffmpeg.Error as e:
            print(f"Error processing {filename}: {e.stderr}")

print("All videos have been processed")