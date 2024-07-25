**To make the one click cleaner file -->**


1. Save the Script <br>
Save your Python script to a file named clean_temp_folders.py. <br>

2. Install PyInstaller <br>
If you haven’t already installed PyInstaller, open a command prompt or terminal and run: <br>
<br>
      pip install pyinstaller <br>
<br>
<br>
3. Create the Executable <br>
Navigate to the directory where you saved clean_temp_folders.py and run the following command:<br>
<br>
      pyinstaller --onefile clean_temp_folders.py <br>
<br>
   <br>
This command tells PyInstaller to package your script into a single executable file. PyInstaller will create a dist directory where the executable will be located. <br>
<br>
5. Locate the Executable <br>
After PyInstaller finishes running, you’ll find your executable file in the dist folder inside your script’s directory. The file will be named clean_temp_folders.exe. <br>
 <br>
6. Create a Desktop Shortcut <br>
Locate the Executable: <br>
Go to the dist folder where the executable is located. <br>
<br>
Create a Shortcut: <br>
<br>
Right-click on the clean_temp_folders.exe file. <br>
Select "Create shortcut." <br>
Drag the shortcut to your desktop or another convenient location. <br>
6. Test the Executable <br>
Double-click the desktop shortcut to ensure that the executable runs as expected and clears the temporary folders. <br>
