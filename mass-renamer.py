import os

root_directory = input('\nEnter the file directory that \nyou want to convert .m4a, .wav, .flac to .mp3 in: ')

for root, dirs, files in os.walk(root_directory):
    for filename in files:
        if filename.endswith((".m4a", ".wav", ".flac")):
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, os.path.splitext(filename)[0] + ".mp3")
            os.system(f"ffmpeg -i '{old_path}' '{new_path}'")
            os.remove(old_path)
print("\nDONE ALL!")
