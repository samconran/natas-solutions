# Appends jpg's "magic number" to the start of
# a file to bypass php's exif_imagetype function

file=$(cat $1);
echo -n -e '\xFF\xD8\xFF\xE0' > $1;
echo $file >> $1;
