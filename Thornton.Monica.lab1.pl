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
#my $partner = "<Replace with your partner's name>";

print "CSCI 305 Lab 1 submitted by $name.\n\n";

# Checks for the argument, fail if none given
if($#ARGV != 0) {
    print STDERR "You must specify the file name as the argument.\n";
    exit 4;
}
# Opens the file and assign it to handle INFILE
open(INFILE, $ARGV[0]) or die "Cannot open $ARGV[0]: $!.\n";

# variable definitions
my $title;     # scalar variable to hold song titles
my $count;	   # scalar variable to keep track of the number of song titles (for testing purposes)	
my $word; 	   # scalar variable to keep track of a particular word
my $index;	   # scalar variable used to iterate through the array 	
my @words;	   # an array variable containing all of the individual words in a song title 	
my %hashOfHashes;
my $hashRef;

# This loops through each line of the file
while($line = <INFILE>) {

	# This prints each line. You will not want to keep this line.
	#print $line;
	
	# Keeps track of how many song titles there are - for testing purposes - increments for each song title
	#$count++;
	
	# The below series of 3 if statements trims the extra information from the song title, leaving just the title
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
	
	# The below series of 14 if statements remove everything after a specified character is found, to remove superfluous text from the title	
	# Removes everything encountered in the title after a left parenthesis is found
	if ($title =~ m/^(.*?)\(/) {
		$title = $1."\n";	
	}
	# Removes everything encountered in the title after a left bracket is found
	if ($title =~ m/^(.*?)\[/) {
		$title = $1."\n";	
	}
	# Removes everything encountered in the title after a left curly brace is found
	if ($title =~ m/^(.*?)\{/) {
		$title = $1."\n";	
	}	

	# Removes everything encountered in the title after a forward slash is found
	if ($title =~ m/^(.*?)\\/) {
		$title = $1."\n";	
	}		
	# Removes everything encountered in the title after a back slash is found
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
	
	# Removes everything encountered in the title after a single left quote is found
	if ($title =~ m/^(.*?)\`/) {
		$title = $1."\n";	
	}

	# Removes everything encountered in the title after a plus sign is found
	if ($title =~ m/^(.*?)\+/) {
		$title = $1."\n";	
	}

	# Removes everything encountered in the title after an equal sign is found
	if ($title =~ m/^(.*?)=/) {
		$title = $1."\n";	
	}

	# Removes everything encountered in the title after an asterisk is found
	if ($title =~ m/^(.*?)\*/) {
		$title = $1."\n";	
	}

	# Removes everything encountered in the title after an asterisk is found
	if ($title =~ m/^(.*?)feat./) {
		$title = $1."\n";	
	}
	
	# The below series of 12 if statements evaluates the titles for punctuation marks, removes them from the title
	# Removes any question marks from the title
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
	
	# Removes any periods from the title
	if ($title =~ m/^(.*?)\./g) {
		$title =~ s/\.+//g;
	}		
	
	# Removes any semicolons from the title
	if ($title =~ m/^(.*?)\;/g) {
		$title =~ s/\;+//g;
	}		
	
	# Removes any ampersands from the title
	if ($title =~ m/^(.*?)&/g) {
		$title =~ s/&+//g;
	}		
	
	# Removes any dollar signs from the title
	if ($title =~ m/^(.*?)\$/g) {
		$title =~ s/\$+//g;
	}			
	
	# Removes any at symbols from the title
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

	# Removes the pipe from the title
	if ($title =~ m/^(.*?)\|/g) {
		$title =~ s/\|+//g;
	}		
	
	# Filter out song titles with non-English characters
	if ($title =~ m/^[a-zA-Z0-9' ]*$/) {
		#if song titles have all valid characters, accept
		$title = $title;
	} else {
		#if has invalid characters, reject and decrement count
		$title = "";
	#	$count--;
	}
	
	#converts the title text to all lower case characters
	$title =~ tr/A-Z/a-z/;

	# Prints the song titles - for testing purposes	
	#print $title;
	
	#keep track of word pair counts in a hash of hashes	
	$hashRef = \%hashOfHashes;
		foreach (split('\s', $title)){
			$hashRef->{$_} = {};        
    		$hashRef = $hashRef->{$_};  
	}

	foreach $hashRef (sort keys %hashOfHashes) {
	       print "$hashref: $hashOfHashes{$hashRef}\n";
    }
	
#	}
#	for ($index = 0; $index < $#words; $index++) {
#		if (!exists($frequency_bigrams{$bigrams[$index]})) {
#			$frequency_bigrams{$bigrams[$index]} = 1;
#		} else {
#			$frequency_bigrams{$bigrams[$index]}++;
#		}
#	}
	
	
	
	
	

	# Prints the number of song titles, for testing purposes
	#print $count."\n";	
	
	
	#while ( <> ) {
     #next unless s/^(.*?):\s*//;
     #$who = $1;
     #$rec = {};
     #$HoH{$who} = $rec;
     #for $field ( split ) {
     #    ($key, $value) = split /=/, $field;
     #    $rec->{$key} = $value;
 }

print Dumper \%hashOfHashes;

 
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