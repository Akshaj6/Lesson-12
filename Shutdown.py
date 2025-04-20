import os
shutdown = input("Do you wish to shutdown the system(Yes or No)?\n")
if shutdown == "No":
    exit()
else:
    os.system("shutdown /s /t 1")