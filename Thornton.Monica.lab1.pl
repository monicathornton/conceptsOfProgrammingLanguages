######################################### 	
#    CSCI 305 - Programming Lab #1		
#										
#  Monica Thornton			
#  monicasuethornton@gmail.com			
#										
#########################################

# Replace the string value of the following variable with your names.
my $name = "Monica Thornton";
# I did not work with a partner on this lab
# my $partner = "<Replace with your partner's name>";

print "CSCI 305 Lab 1 submitted by $name.\n\n";

# Checks for the argument, fail if none given
if($#ARGV != 0) {
    print STDERR "You must specify the file name as the argument.\n";
    exit 4;
}

# Opens the file and assign it to handle INFILE
open(INFILE, $ARGV[0]) or die "Cannot open $ARGV[0]: $!.\n";

# variable definitions
my $title;     				# scalar variable to hold song titles
my $count;	   				# scalar variable to keep track of the number of song titles (for testing purposes)	
my $index;	   				# scalar variable used to iterate through the array 	
my @words;	   				# an array variable containing all of the individual words in a song title 	
my %bigrams = {};			# a hash variable to hold all of the bigrams created from the text file
my %frequencyBigrams = {};	# a hash variable used to hold the frequency with which each of the bigrams occur

# This loops through each line of the file
while($line = <INFILE>) {

	# This prints each line - for testing purposes
	# print $line;
	
	# Keeps track of how many song titles there are - for testing purposes - increments for each song title
	# $count++;
	
	# The below series of 3 if statements trims the extra information from the song title using a regex match, 
	# leaving just the title at the end of the series of ifs
	# The outermost if trims everything before the first <SEP>, saving the trimmed text from $line in the variable title
	if($line =~ m/<SEP>(.*?)$/) {
		$title = $1;		
	# The second if trims everything between the first and second <SEP>, saving the newly trimmed text back in the $title variable
		if($title =~ m/<SEP>(.*?)$/) {
			$title = $1;	
		  # The third if further trims the title, leaving us with only the song title 		
			if($title =~ m/<SEP>(.*?)$/) {
			$title = $1."\n";	
			}
		}		
	}
	
	# The below series of 14 if statements use a regex match to remove everything after a specified character is found, 
	# to remove superfluous text from the title	
	# Removes everything encountered in the title after a left parenthesis is found (left paren is escaped)
	if ($title =~ m/^(.*?)\(/) {
		$title = $1."\n";	
	}
	# Removes everything encountered in the title after a left bracket is found (left bracket is escaped)
	if ($title =~ m/^(.*?)\[/) {
		$title = $1."\n";	
	}
	# Removes everything encountered in the title after a left curly brace is found (left curly brace is escaped)
	if ($title =~ m/^(.*?)\{/) {
		$title = $1."\n";	
	}	

	# Removes everything encountered in the title after a forward slash is found (forward slash is escaped)
	if ($title =~ m/^(.*?)\\/) {
		$title = $1."\n";	
	}		
	# Removes everything encountered in the title after a back slash is found (back slash is escaped)
	if ($title =~ m/^(.*?)\//) {
		$title = $1."\n";	
	}	

	# Removes everything encountered in the title after a underscore is found
	if ($title =~ m/^(.*?)_/) {
		$title = $1."\n";	
	}		
	
	# Removes everything encountered in the title after an em-dash is found
	if ($title =~ m/^(.*?)-/) {
		$title = $1."\n";	
	}			
	
	# Removes everything encountered in the title after a colon is found
	if ($title =~ m/^(.*?):/) {
		$title = $1."\n";	
	}			
	
	# Removes everything encountered in the title after a double quote is found
	if ($title =~ m/^(.*?)"/) {
		$title = $1."\n";	
	}	
	
	# Removes everything encountered in the title after a single left quote is found (single quote is escaped)
	if ($title =~ m/^(.*?)\`/) {
		$title = $1."\n";	
	}

	# Removes everything encountered in the title after a plus sign is found (plus sign is escaped)
	if ($title =~ m/^(.*?)\+/) {
		$title = $1."\n";	
	}

	# Removes everything encountered in the title after an equal sign is found
	if ($title =~ m/^(.*?)=/) {
		$title = $1."\n";	
	}

	# Removes everything encountered in the title after an asterisk is found (asterisk is escaped)
	if ($title =~ m/^(.*?)\*/) {
		$title = $1."\n";	
	}

	# Removes everything encountered in the title after the string "feat." is found
	if ($title =~ m/^(.*?)feat./) {
		$title = $1."\n";	
	}
	
	# The below series of 12 if statements evaluates the titles for punctuation marks using a reg ex match, and removes them from the title
	# Removes any question marks from the title (question mark is escaped)
	if ($title =~ m/^(.*?)\?/g) {
		$title =~ s/\?+//g;
	}
	
	# Removes any inverted question marks from the title
	if ($title =~ m/^(.*?)¿/g) {
		$title =~ s/¿+//g;
	}	
	
	# Removes any exclamation points from the title
	if ($title =~ m/^(.*?)!/g) {
		$title =~ s/!+//g;
	}	

	# Removes any inverted exclamation points from the title
	if ($title =~ m/^(.*?)¡/g) {
		$title =~ s/¡+//g;
	}		
	
	# Removes any periods from the title (periods are escaped)
	if ($title =~ m/^(.*?)\./g) {
		$title =~ s/\.+//g;
	}		
	
	# Removes any semicolons from the title (semi-colons are escaped)
	if ($title =~ m/^(.*?)\;/g) {
		$title =~ s/\;+//g;
	}		
	
	# Removes any ampersands from the title
	if ($title =~ m/^(.*?)&/g) {
		$title =~ s/&+//g;
	}		
	
	# Removes any dollar signs from the title (dollar signs are escaped)
	if ($title =~ m/^(.*?)\$/g) {
		$title =~ s/\$+//g;
	}			
	
	# Removes any at symbols from the title (at symbols are escaped)
	if ($title =~ m/^(.*?)\@/g) {
		$title =~ s/\@+//g;
	}			

	# Removes any percent signs from the title
	if ($title =~ m/^(.*?)%/g) {
		$title =~ s/%+//g;
	}	

	# Removes any pound signs from the title
	if ($title =~ m/^(.*?)#/g) {
		$title =~ s/#+//g;
	}	

	# Removes the pipe from the title (pipe is escaped)
	if ($title =~ m/^(.*?)\|/g) {
		$title =~ s/\|+//g;
	}		
	
	# Filter out song titles with non-English characters using regex matching
	if ($title =~ m/^[a-zA-Z0-9' ]*$/) {
		#if a song title has all valid characters, accept it
		$title = $title;
	} else {
		# If a song title has invalid (non-English) characters, reject it and decrement the count (count commented out, just for testing purposes)
		$title = "";
	    #$count--;     
	}
	
	# Converts the title text to all lower case characters
	$title =~ tr/A-Z/a-z/;

	# Prints the song titles - for testing purposes	
	# print $title;
	
	# Splits the title into a series of words (space delimited), places those words in an array 	
	@words = split(/\s+/,$title);
  
	# Builds a bigram (a series of two adjacent words) for each adjacent word pair using the words in the title
	# The first for loop loads the bigrams hash with bigrams from the song title
	for ($index = 0; $index < $#words; $index++) {
		$bigrams[$index] = $words[$index]." ".$words[$index + 1];
	}
	# The second for loop checks to see if the bigram constructed above is already in the hash, and increments accordingly, storing results 
	# in the frequencyBigrams hash
	for ($index = 0; $index < $#words; $index++) {	
		if (!exists($frequencyBigrams{$bigrams[$index]})) {
			$frequencyBigrams{$bigrams[$index]} = 1;
		} else {
			$frequencyBigrams{$bigrams[$index]}++;
		}
	}
	#end while
}      

	foreach $bigrams (sort keys %frequencyBigrams) {
		@bigrams = split(/\s+/,$bigrams);

		#if ($bigrams[0] eq "love") {	
		#if ($bigrams[0] eq "sad") {
		if ($bigrams[0] eq "happy") {
			++$count;
			print "$bigrams ----- count $frequencyBigrams{$bigrams} ---- repeat: $count\n";

		}
	}


	
	
  # Prints the number of song titles, for testing purposes
  #print $count."\n";	

 
# Close the file handle
close INFILE; 

# At this point (hopefully) you will have finished processing the song 
# title file and have populated your data structure of bigram counts.
print "File parsed. Bigram model built.\n\n";


# User control loop
print "Enter a word [Enter 'q' to quit]: ";
$input = <STDIN>;
chomp($input);
print "\n";	
while ($input ne "q"){
	# Replace these lines with some useful code
	 
	


	
	
	
	print "Not yet implemented.  Goodbye.\n";
	$input = 'q';
}

# MORE OF YOUR CODE HERE....