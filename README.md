# natas-solutions

Repo of random scripts I've written whilst doing Over The Wire's Natas challenges. These aren't pretty, or very efficient, but they get the job done.

* brute_15.py is a python script written for level 15 which brute forces the password for user 'natas16' via an SQL injection into their username existence checker. It uses the responses from injecting a `AND password LIKE BINARY '[attempt]%'` to continually build up the 32-digit password.

* Following a similar line of thought, brute_16.py brute forces for the user 'natas17', this time using the response gained from a command injection into their dictionary.txt searcher. My logic here, since the backend checked against special characters but left `$` and `( )` untouched, was to follow the search word with `$(grep ^[attempt] /etc/natas_webpass/natas17)`. If the backend's dictionary grep returned results for the search term, the attempt failed. If the password did start with the attempt, there would be no results, since the dictionary would then search for `[search_term][password]`.

* Continuing the injection trend, brute_17.py is a modification of 15. This time, no information is returned, making it tricky to check the success of the injected queries. However, by making use of the SLEEP keyword in SQL, we can delay the query and time the response. By injecting the following SQL: `natas18" AND password LIKE BINARY '[attempt]%' AND SLEEP(1) #` we know that the query will ignore the SLEEP fucntion if the password has not matched `LIKE BINARY '[attempt]%'`. However, if the request takes over 1 second, we can tell that the password has matched. From this basis, the script mimicks 15 in building up a 32 char password. The `#` is there to comment out the rest of the backend's SQL.

* Moving away from injection, brute_18.py is a script that brute forces the correct value of the PHPSESSID cookie, since this is used (ineptly) in the backend to verify admin access. We know, from the php code made available to us, that the ID is somewhere in the range 1 - 640, which makes this perfectly do-able.

* brute_19.py is an extension of the above, however level 19 attempts to obfuscate things a little by appending the username to the session ID and encoding the whole thing in hex. So, this script simply runs the same brute force attack as 18, but encodes each [ [attempt]-admin] in hex.

* jpegify is just a shell script that appends the 'magic number' of a jpg to a file of your choosing. This was used for level 13, where the backend used php's `exif_imagetype` function to check the file upload, ensuring it was a jpg. By appending these bytes to the front of the file, the function is tricked into accepting any file, including the php script I uploaded, which I could then access and execute, returning the password for user 'natas14'
