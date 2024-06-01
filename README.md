Itay Barzelai

Magshimim Assignment - Python Coding Exercise

For the task I was given, I decided upon writing two classes to accommodate the methods I needed:

- HttpDownloader: For downloading files using the HTTP protocol (using a GET request and then saving the response content within a file).
- PdfAnalyzer: For taking an existing file and extracting information from it (and potentially manipulating it).

I made this design choice to make two distinct classes to make this system more versatile (you can easily add another class to support another protocol, such as FTP, or write a new class to support another file format, such as mp4) and to spread the code, thus making it more manageable.

Then, I made two test files to test the two aspects of the process, the generic one of downloading the file, and the specific one to the pdf format.

Tests:

- Test if status code == 200
- Test for a “File not found” (404 code) error
- Test for a “Can’t be reached” situation
- Test whether the file has been saved correctly
- Test if the author is correct
- Test if the title is correct
- Test if the length of the document is correct
- Test if the creation date is correct
- Test if the file has the correct extension in its name
- Test if the file is a valid pdf file
