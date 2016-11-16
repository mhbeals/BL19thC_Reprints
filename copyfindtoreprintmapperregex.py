# Import libraries
import fileinput
import re

# Set initial variables
end_year = 1900 # Set to last year plus one
year = 1800 # Set to first year
month = 1 # Set to first month of first year

# For each year that is less than the end year
while year < end_year:
    
    # For each month that is before October
    while month < 10:
        
        # create a file
        filename = str(year) + "_0" + str(month) + ".txt"
        
        # open the input file
        myfile = fileinput.FileInput(str(year) + "_0" + str(month) + ".tsv")
        
        # empty the write string
        string = ''
        
        # for every line in my input file
        for line in myfile:
            
            # Regex the line
            string += re.sub(r'\tI:\\BL_TXTS\\18[0-9]0s\\18[0-9]{2}\\[0-9]{2}\\([0-9]{4}).([0-9]{2}).([0-9]{2})_([A-Za-z\- \']+)_([A-Z0-9]+).txt\tI:\\BL_TXTS\\18[0-9]0s\\18[0-9]{2}\\[0-9]{2}\\([0-9]{4}).([0-9]{2}).([0-9]{2})_([A-Za-z\- \']+)_([A-Z0-9]+).txt',r'\t\1\t\2\t\3\t\4\t\1.\2.\3_\4_\5\t\6\t\7\t\8\t\9\t\6.\7.\8_\9_\10', line.rstrip())
            
            # End the line
            string += '\n'
        
        # convert the string into output string
        output = str(filename)
        
        # open the output file
        text_file = open(output, "w")
        
        # write to the output file
        text_file.write(string)
        
        # close the output file
        text_file.close()
        
        # increase the month count by one
        month += 1
        
    # If October to December, do as above but with change to filename to not include 0    
    while month < 13:
        filename = str(year) + "_" + str(month) + ".txt"
        myfile = fileinput.FileInput(str(year) + "_" + str(month) + ".tsv")
        string = ''
        for line in myfile:
            string += '\n'
            string += re.sub(r'\tI:\\BL_TXTS\\18[0-9]0s\\18[0-9]{2}\\[0-9]{2}\\([0-9]{4}).([0-9]{2}).([0-9]{2})_([A-Za-z\- \']+)_([A-Z0-9]+).txt\tI:\\BL_TXTS\\18[0-9]0s\\18[0-9]{2}\\[0-9]{2}\\([0-9]{4}).([0-9]{2}).([0-9]{2})_([A-Za-z\- \']+)_([A-Z0-9]+).txt',r'\t\1\t\2\t\3\t\4\t\1.\2.\3_\4_\5\t\6\t\7\t\8\t\9\t\6.\7.\8_\9_\10', line.rstrip())
        output = str(filename)
        text_file = open(output, "w")
        text_file.write(string)
        text_file.close()
        month += 1
        
    # If month is 13, reset month to one    
    while month == 13:
        month = 1
    
    # Add a year to the current year
    year += 1
