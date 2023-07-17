# SPH Platform-Eng Test

requirement.txt ? 
Develop on linux first for compatibility
Test on GCP Cloud Run 
Error handling? 

Using a programming language of your choice, implement a long-running process that:
• Accepts a csv file containing a list of up to 1000 urls with names at startup. - csv format must have no space between columns
• The process should pull all these urls every 10 minutes to check their HTTP status.
• The process should also bind a local port, to provide a summary of monitoring status in the past hour in any suitable format.
• Containerise the application
A sample of the CV file might include:

Deployment Task
Provide a solution in the form of code using Terraform to deploy the containerised application you have written above to a cloud provider of your choice. Your solution should include setting up the cloud provider account so that the application can be deployed.

References 
Get CSV to array: https://stackoverflow.com/questions/58174752/how-to-convert-columns-from-a-csv-file-into-arrays-in-python-with-the-first-valu
CSV column error (space between comma): https://www.geeksforgeeks.org/how-to-fix-keyerror-in-pandas/
How to loop in: https://www.w3schools.com/python/python_for_loops.asp
How to handle errors in: https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
Add elements in to array: https://stackoverflow.com/questions/22740512/store-a-value-in-an-array-inside-one-for-loop