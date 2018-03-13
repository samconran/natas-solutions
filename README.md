# natas-solutions

Repo of random scripts I've written whilst doing Over The Wire's Natas challenges

* brute_15.py is a python script written for level 15 which brute forces the password for user 'natas16' via an SQL injection into their username existence checker. It uses the responses from injecting a `AND password LIKE BINARY '[attempt]%'` to continually build up the 32-digit password.

* Following a similar line of thought, brute_16.py brute forces for the user 'natas17', this time using the response gained from a command injection into their dictionary.txt searcher. My logic here, since the backend checked against special characters but left `$` and `( )` untouched, was to following the search word with `$(grep ^[attempt] /etc/natas_webpass/natas17)`. If the backend's dictionary grep returned results for the search term, the attempt failed. If the password did start with the attempt, there would be no results, since the dictionary would then search for `[search_term][password]`.

* jpegify is just a shell script that appends the 'magic number' of a jpg to a file of your choosing. This was used for level 13, where the backend used php's `exif_imagetype` function to check the file upload, ensuring it was a jpg. By appending these bytes to the front of the file, the function is tricked into accepting anything uploaded, including the php script I uploaded, which I could then access and execute, returning the password for user 'natas14'
