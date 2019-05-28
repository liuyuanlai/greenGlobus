#!/usr/bin/env python
with open("flist_uc2null", "w") as f:
	for i in range(48):
		s = "ftp://192.5.87.32:12334/home/cc/data/48/file" + str(i) + " ftp://192.5.87.33:12334/dev/null\r\n"
		f.write(s)

		
	
