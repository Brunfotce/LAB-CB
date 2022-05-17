import subprocess

file= open("dnscache.txt","w")
content= str(subprocess.run(["ipconfig", "/displaydns"],capture_output=True))
file.write(content)
file.close()
