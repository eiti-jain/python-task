import MySQLdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file',type=argparse.FileType('r'))
args = parser.parse_args()
f= args.file.readlines()
f.remove('\n')
print(f)
mydb=MySQLdb.connect(host="localhost",user="root",password="very_strong_password",database="employees")
mycursor=mydb.cursor()
for i in range(len(f)):
    sql="INSERT INTO my(id,name,dept,salary)VALUES(%s,%s,%s,%s)"
    arr=f[i].split(',')
    val=(int(arr[0]),arr[1],arr[2],int(arr[3]))
    mycursor.execute(sql,val)
    mydb.commit()
