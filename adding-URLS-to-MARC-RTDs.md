# Batch replacing URLs in Aleph MARC records for retrospective electronic theses and dissertations
CC-BY Kelly Thompson 2015

## Step 1. Generate list of Aleph IDs and URLs for record pull

**1.1**	Log in to the DR website with administrator credentials.  Navigate to the "Manage Theses/Dissertations" page.  

**1.2**	Generate two metadata reports:

>**1.2.1**	Under "Batch revise Excel", generate a spreadsheet of current descriptive metadata.

>**1.2.2**	Under "Administrator report", generate a spreadsheet of current metadata, including technical metadata (this is the report from which you can draw the URLs).

**1.3**	Combine necessary data from these spreadsheets to gather a list of Aleph IDs and URLs.  Make sure that you are including in your batch only those records for which you have not previously updated the URL in the MARC record.  It will probably be helpful for you later on if your data has headers that correspond to MARC fields.  Save this file as tab separated .txt for later use.

**1.4**	Send the list of only the Aleph IDs to Systems Administrator, and they will send you back a batch of MARC records in the .mrc format.  Double check for blank rows before sending!

## Step 2. Convert from machine-readable to human-readable MARC

**2.1**	Save the .mrc file from Systems Admin to your computer.

**2.2**	Open MarcEdit.  Select the "MARC tools" function.

**2.3**	Select the .mrc file from Eric as the "Input File" using the file browse function.  Create an output file with extension .mrk using the browse function as well.

**2.4**	Double check that the "MarcBreaker" function is selected in the interface, and click the "Execute" button.  Once completed, click "Close".  

## Step 3. Generate skeleton MARC records from your DR data reports

**3.1**	Open the "Delimited Text Translator" function in MarcEdit.  Select your .txt file from Step 1.3 as the "Source File".   This should have two columns: Aleph ID and URL.  Use the browse function to create your output file.  Ensure that the delimiter selected in the drop-down matches that used to create your .txt file (Ex: tab).  Click the "Next" button.

**3.2**	Map your spreadsheet columns to output MARC fields.  This is why it is essential to have headers on your data in Step 1.3.

>**3.2.1**	Mapping example:  My "Field 1" is the spreadsheet column with the URL in it.  In the Select: drop-down, I choose "Field 1".  In the "Map to:" box I enter 856$u for the 856 field, subfield $u.  For indicators I enter "41".  I then click the "Add Argument" button.  

>**3.2.2**	Repeat mapping for all fields.  Map the Aleph ID to the 999$a \\ field.  

**3.3**	Once you have mapped all of your columns to fields, hit the "Finish" button.  You can double check your file at this point to make sure things look how you think they should.

## Step 4. Remove old URLs from MARC records from Aleph

**4.1**	Open the .mrk from Eric in MarcEditor.  To double check whether each record has an 856 field yet, go to the Reports tab and select "Field Count".  This may or may not be the same as the number of records, and that is okay.  Double check also whether each record has a 999 field.  This number should always match the number of records and is essential for a successful record merge in the next steps.

**4.2**	If your data already has 856 fields you don"t want (ours had old ProQuest fields we wanted to remove), delete them.  Go to the "Tools" tab and select "Add/Delete Field". In the "Field" drop down enter 856.  Leave the "Field Data" box blank.  Click the "Delete Field" button.  The dialog box which pops up should indicate how many 856 fields the function deleted.  Hopefully this matches the number of 856 fields present in Step 4.1.

## Step 5. Merge Aleph MARC records with skeleton DR data MARC records

**5.1**	Open the "Merge Records" function in MarcEdit.  Select as your "Source" the file with Aleph data, select as the "Merge" file your skeleton DR data records, and use the browse function to create a new "save" file.  Enter "999" for in the "Record identifier" box.  Click the "Next =>" button.

**5.2**	On the next screen, you should have the option to select the radio button next to "Merge selected fields".  Click "Next =>".  

**5.3**	Enter 856 in the "Select Field" box, click the green arrow pointing right (?) to add this field to the "Merge fields" box, then click "Next =>".

**5.4**	Click "Close" and double check your file to make sure that the merge was successful. Use the "Reports"""Field Count" function to ensure that the number of records matches the number of 856 and 999 fields.  

**5.5**	Convert back to .mrc file type using "MarkMaker" function, then send your file to Systems Admin for upload to Aleph.
