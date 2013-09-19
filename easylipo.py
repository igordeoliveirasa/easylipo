import os
import fnmatch

create_argument = ""
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.a'):
        create_argument += file + " "
        print file

os.system("lipo -create %s -output %s" % (create_argument, "libMachineIdentificatoriOS.a"))
