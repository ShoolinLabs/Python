
import xlwt,xlrd
from xlutils.copy import copy
import os.path
data=0
name=0

if(os.path.isfile("sagar.xls")==False):
    rb=xlwt.Workbook()
    sheet=rb.add_sheet("1")
    #sheet1=rb.add_sheet("2")
    
    rb.save("sagar.xls")


    

def submit(data):

   
        

    b1= xlrd.open_workbook('sagar.xls', 'r')
    s1 = b1.sheet_by_index(0)

    rowx=s1.nrows                   # s1.nrows = tells about the no. of rows in the sheet s1
    colx=s1.ncols                   # s1.ncols = tells about the no. of cols in the sheet s1
    print "rows",rowx
    print"cols",colx
    b2 = copy(b1)                   # creates a writeable copy
    sheet1 = b2.get_sheet(0)        # get a first sheet
   
    sheet1.write(rowx,0,data)
    sheet1.write(rowx,1,name)

    b2.save("sagar.xls")
    
   
    
for i in range(10):
    """
------------------------------------------------
    #take the data from the ultrasonic
    and save it in the variable data which is
    already declared so, just read values from
    ultrasonic and save it in data
    and also remove the line written below
    summit(i) and call it with your data
    
------------------------------------------------
    
    """
       
    submit(i)
    
