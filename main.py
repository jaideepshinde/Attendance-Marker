import pandas as pd
import os
def filereader(name):
    ext=name.split('.')[-1]
    if ext=='xlsx':
        p=pd.read_excel(name)
        return p
    elif ext=='csv':
        p=pd.read_csv(name)
        return p
    else:
        print(file)
        print("Invalid File format!")
        quit()
if __name__ == '__main__':
    finalAttendence={}
    namefile=os.listdir('Names')[0]

    Names=filereader(os.path.join('Names',namefile))
    Names=set(map(str.strip,Names['Display Name']))
    nameslist=list(Names)

    namewithid={}
    i=1
    for name in nameslist:
        namewithid[name]=i
        i+=1
    finalAttendence['FullName']=nameslist
    #read attendence sheets
    attendencefiles = os.listdir('AttendenceSheets')

    for file in attendencefiles:
        attendence=filereader(os.path.join('AttendenceSheets',file))
        presentstudents=set(map(str.strip,attendence['Full Name']))
        date=str(attendence['Timestamp'][0]).split(',')[0]
        presentValid=Names.intersection(presentstudents)
        datecol=[]
        for n in nameslist:
            if n in presentValid:
                datecol.append('P')
            else:
                datecol.append('A')
        finalAttendence[date]=datecol
    fin=pd.DataFrame.from_dict(finalAttendence)
    fin.to_csv('MonthAttendence.csv')











