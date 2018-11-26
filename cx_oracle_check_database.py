import sys
import subprocess
import cx_Oracle
time = subprocess.Popen('ps -ef|grep pmon|grep `echo $ORACLE_SID`|wc -l',shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = time.communicate()
#print output
if (int(output)) == 0:
	print "Seems database is down. printign the last few lines of alert log"
	alert = subprocess.Popen('tail 20f /svw/svw_app/oracle/diag/rdbms/svwsbx1b/SVWSBX1B/trace/alert_SVWSBX1B.log',shell=True, stdout=subprocess.PIPE)
	alertlog = alert.communicate()
	print alertlog
	connection = cx_Oracle.connect("/", mode = cx_Oracle.SYSDBA | cx_Oracle.PRELIM_AUTH)
	#print output
	connection.startup()
	connection = cx_Oracle.connect("/", mode = cx_Oracle.SYSDBA)
	cursor = connection.cursor()
	cursor.execute("alter database mount")
	cursor.execute("alter database open")
        print "started the database"
else:
	print "Database is running fine"
exit()
