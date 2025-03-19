from os import scandir, rename  # Import functions to scan directories and rename files
from os.path import exists, join, splitext  # Import functions to check file existence, join paths, and split extensions
from shutil import move  # Import move function to relocate files

import logging  # Import logging module to log information

# Directories to categorize files
sourceDir = ""          # Source directory where the files are located
destDirSFX = ""         # Destination directory for sound effects (small audio files)
destDirMusic = ""       # Destination directory for music (large audio files)
destDirImage = ""       # Destination directory for image files
destDirDocuments = ""   # Destination directory for document files
destDirVideo = ""       # Destination directory for video files

# List of image file extensions to identify image files
imageExtensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

# List of video file extensions to identify video files
videoExtensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

# List of audio file extensions to identify audio files
audioExtensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

# List of document file extensions to identify document files
documentExtensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

def makeUnique(dest, name):
    filename, extension = splitext(name)  # Split the filename and its extension
    counter = 1  # Initialize a counter to create unique filenames

    # Loop to generate a unique filename if the file already exists
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"  # Append a counter to the filename
        counter += 1  # Increment the counter

    return name  # Return the unique filename

def moveFile(dest, entry, name):
    # Check if the file already exists in the destination
    if exists(f"{dest}/{name}"):
        uniqueName = makeUnique(dest, name)  # Create a unique name if needed
        oldName = join(dest, name)  # Get the existing file path
        newName = join(dest, uniqueName)  # Define the new unique file path
        rename(oldName, newName)  # Rename the existing file to avoid overwriting
    move(entry, dest)  # Move the file to the destination folder

def onCleaner():
    # Scan the source directory and process each entry (file)
    with scandir(sourceDir) as entries:
        for entry in entries:
            name = entry.name  # Get the filename
            checkAudioFiles(entry, name)  # Check if it's an audio file
            checkVideoFiles(entry, name)  # Check if it's a video file
            checkImageFiles(entry, name)  # Check if it's an image file
            checkDocumentFiles(entry, name)  # Check if it's a document file

def checkAudioFiles(entry, name):
    # Iterate through audio extensions and check if the file matches
    for audioExtension in audioExtensions:
        if name.endswith(audioExtension) or name.endswith(audioExtension.upper()):
            # Determine if it's a sound effect or a regular music file
            if entry.stat().st_size < 10_000_000 or "SFX" in name:  # Files less than 10 MB or with "SFX" in the name
                dest = destDirSFX
            else:
                dest = destDirMusic
            moveFile(dest, entry, name)  # Move the audio file to the appropriate directory
            logging.info(f"Moved audio file: {name}")  # Log the action

def checkVideoFiles(entry, name):
    # Iterate through video extensions and check if the file matches
    for videoExtension in videoExtensions:
        if name.endswith(videoExtension) or name.endswith(videoExtension.upper()):
            moveFile(destDirVideo, entry, name)  # Move the video file
            logging.info(f"Moved video file: {name}")  # Log the action

def checkImageFiles(entry, name):
    # Iterate through image extensions and check if the file matches
    for imageExtension in imageExtensions:
        if name.endswith(imageExtension) or name.endswith(imageExtension.upper()):
            moveFile(destDirImage, entry, name)  # Move the image file
            logging.info(f"Moved image file: {name}")  # Log the action

def checkDocumentFiles(entry, name):
    # Iterate through document extensions and check if the file matches
    for documentExtension in documentExtensions:
        if name.endswith(documentExtension) or name.endswith(documentExtension.upper()):
            moveFile(destDirDocuments, entry, name)  # Move the document file
            logging.info(f"Moved document file: {name}")  # Log the action