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
my $input;					# scalar variable used to hold a word entered by the user
my $titleLength;            # scalar variable used to keep track of the number of words in the song title 
my $songTitle;			    # scalar variable used to keep track of a song title that we will construct using the bigrams  
my @words;	   				# an array variable containing all of the individual words in a song title 
my @stopWords;				# an array variable containing all of the stop words	
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
	
	# Remove the specified stop words using regex substitution on word boundaries
	$title =~ s/\b(?:a|an|and|by|for|from|in|of|on|or|out|the|to|with)\b//g;

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

 # Prints the number of song titles, for testing purposes
 #print $count."\n";	

 # Close the file handle
 close INFILE; 

 # Song title file processed, and data structure populated with bigrams and bigram counts. Prints message for user to let them know.
 print "File parsed. Bigram model built.\n\n";

 # User control loop
 print "Enter a word [Enter 'q' to quit]: ";
 # Saves the user entered word into a variable named input
 $input = <STDIN>;
 # remove the newline character
 chomp($input);
 print "\n";
 # Run the below loop while the user has not indicated that they would like to quit by entering q
 while ($input ne "q"){
	# As there are no words in the constructed song title yet, sets this variable equal to 0
	$titleLength = 0;
	# As there are no words in the constructed song title yet, sets this variable equal to the empty string
	$songTitle = "";
	
	# If the probable song title we are constructing contains no words, take the following steps
	if ($titleLength == 0) {
		# Store the result of the mcw function (which gets the most common word following the word $input) in a variable
		$bigramWord = mcw($input);
		# Use that variable, along with the input value from the user, to construct the first two words of your title
		$songTitle = $input." ".$bigramWord;
		# Increment the length of the title string twice, to account for both the input word and its matching bigram word
		$titleLength++;	
		$titleLength++;
	}
	
	# Keeps adding words up to the song title, up to the cap of 20 words in the title (indexing starts at 0)
	while($titleLength <= 19) {
		# If the result of using the most common word function on the current value of the bigramWord variable is not the empty string 
		if (mcw($bigramWord) ne ""){
			# Append the new value returned from most common word function to the existing song title
			$songTitle = $songTitle." ".mcw($bigramWord);
			# Update the value of the bigram word variable
			$bigramWord = mcw($bigramWord);
			# Increment the length of the title string
			$titleLength++;	
		} else {
		# If the result of using the most common word function was the empty string, decrement the length of the title by one  
			$titleLength--;
			# Break out of the while loop
			last;
		}
	}
	# Print the song title
	print "Probable song title given the word $input: \n$songTitle\n";
	
	# Gets the count of the number of words in the song title - for testing purposes 
	# print "The song is $titleLength word(s) long\n";
	
	# User control loop
	print "\nEnter a word [Enter 'q' to quit]: ";
	# Saves the user entered word into a variable named input
	$input = <STDIN>;
	# remove the newline character
	chomp($input);
	print "\n";
	
	}
	# Prints the message that they are leaving the program 
	print "You have chosen to quit the program.  Goodbye.\n";


	# A function to take a word as an argument, and return the word that most follows the chosen word in the dataset
	sub mcw() 
	{
		# The argument for the function, provided at the function call
		my $inputWord = $_[0];
		
		# A variable to keep track of the largest number of times a bigram appears (with the first word of the bigram given by $inputWord),
		# initialized to 0, so that the first time a value greater than 0 is encountered, the appropriate if branch is taken
		$biggestNumOccurences = 0;
	
			# Goes through every bigram in the hash of hashes 
			foreach $bigrams (sort keys %frequencyBigrams) {
				# Splits the bigrams into individual words, stored as an array
				@bigrams = split(/\s+/,$bigrams);
				
				# Checks if the first word of the bigram is equal to the input word, if so, examines the word following the input word
				if ($bigrams[0] eq $inputWord) {
					# Keeps track of the number of bigrams beginning with the input word - for testing purposes
					# ++$count;
					
					# Stores the second word of the bigram in the variable nextWord
					$nextWord = $bigrams[1];
				# Prints the entire list of bigrams for the given word - for testing purposes
				# print "the nextWord is $nextWord which occurs $frequencyBigrams{$bigrams} times\n";	

					# If the number of times the bigram occurs is larger than the previously largest bigram
					if ($frequencyBigrams{$bigrams} > $biggestNumOccurences) {
						# Mark the second word of this bigram as the most frequent
						$mostFrequentNextWord = $nextWord;
						# Make the number of occurrences the new biggest
						$biggestNumOccurences = $frequencyBigrams{$bigrams};
					} # If the number of times the bigram occurs is equal to the currently largest bigram 
					 elsif ($frequencyBigrams{$bigrams} == $biggestNumOccurences) {
						my $range = 10;
						# Gets a random integer from the range set in the variable above
               	        my $random_number = int(rand($range));
						# If this integer is greater than or equal to 4, consider this the most frequently occurring bigram
						if ($randomNumber >= 4) {
							$mostFrequentNextWord = $nextWord;					
						} 
						# If the integer is greater than 4, leave the most frequently occuring bigram as it was originally, do not reset 
					}
				}	
			}
			
		
		# The following 3 print statements print out information on the bigrams - for testing purposes 
		# print "bigrams for $input \n";
		# print "the most frequent next word is ---$mostFrequentNextWord --- which occurs --- $biggestNumOccurences --- times\n";
		# print "$inputWord has $count bigrams\n";
		return $mostFrequentNextWord;
		#end mcw function
	}