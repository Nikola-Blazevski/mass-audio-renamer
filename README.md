# mass-audio-renamer

To use this script simply write the path for the root directory
with the path to the root directory containing the ".m4a", ".wav", 
and ".flac" files you want to convert, and then run the script in 
a terminal window on Linux. Make sure that you have FFmpeg 
installed on your system before running this script.

This script uses the os.walk method to loop through all directories 
and subdirectories under the specified root directory. For each 
directory, the script loops through every file and checks if the file 
extension is ".m4a", ".wav", or ".flac". If it is, it uses FFmpeg to 
convert the file to ".mp3" format, and then deletes the original file.

As before, the script uses single quotes around the file paths in the 
FFmpeg command to handle directory names with spaces. Note that this 
script will modify files in subdirectories as well as in the root directory.
