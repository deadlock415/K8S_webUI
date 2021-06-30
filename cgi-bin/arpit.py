#!/usr/bin/python3

print("content-type:text/html")

print()


import subprocess
import cgi
form=cgi.FieldStorage()
cmd=form.getvalue("q")
output=subprocess.getoutput("{} --kubeconfig=admin.conf".format(cmd))
print(output)
#x=subprocess.getoutput()
#print(x)


