# fileSorter
Program Architecture Overview
Input Directories:

sourceDir: Directory where unorganized files are stored.
Destination directories (destDirSFX, destDirMusic, destDirImage, destDirDocuments, destDirVideo): Store organized files by category.
File Type Categorization:

Lists of supported file extensions for images, videos, audio, and documents.
Special handling for small audio files or those containing "SFX" in the name.
Core Functions:

makeUnique(): Ensures unique filenames by appending a counter if duplicates exist.
moveFile(): Moves files to the correct destination, resolving name conflicts.
onCleaner(): Main driver function scanning and categorizing files.
File Checkers (checkAudioFiles(), checkVideoFiles(), checkImageFiles(), checkDocumentFiles()):
Match file extensions and direct files to their appropriate folders.
Logging:

Records each moved file for tracking and debugging.
Process Flow:

Scan source directory.
Identify and categorize files.
Ensure unique names if duplicates exist.
Move files to their designated folders.
