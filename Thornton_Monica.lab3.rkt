;Tells DrRacket the language we are using (Scheme);
#lang scheme

;Tells DrRacket that we want to enable tracing;
(require racket/trace)

#|
 ######################################## 
 #  CSCI 305 - Programming Lab #3		
 #										
 #  Monica Thornton			
 #  monicasuethornton@gmail.com			
 #
 # A program that contains a variety of different functions, 
 # used to learn and demonstrate functional programming. 
 #  
 ######################################## 
|#


#|Defines a function named f that given a list of numbers
  (either integer or float) will increment that number by 1.
  The function takes as its argument a list named lst.
|#
(define (f lst)
  ;Allows us to trace the function f;
  ;(trace f);
  
  ;Checks if lst is null (in other words, have we processed all values in lst yet?);
  (if (null? lst)
      ;If lst is empty, creates an empty list;
      ' ()
      #| Else, if lst is not empty - constructs a new list (via a recursive call to f), which contains the values in 
         the old list incremented by 1.|#
      (cons (+ 1 (car lst)) (f(cdr lst)))))

#|Defines a function named member? that given a list
  will search the list to determine if an element e 
  (provided by the user) is a part of that list.
  The function takes as its argument the target value e, 
  and the list to be searched lst.
|#
(define (member? e lst)
  ;Allows us to trace the function member?;
  ;(trace member?);
  
  ;A series of checks to determine whether e is in the list ;
  (cond 
       #|Checks if the list is empty, both to avoid an error if the user provides an empty list 
         initially, and to stop the recursive calls if the entire list is checked and the target element is 
         not found. Returns #f in either case. 
       |#
       ((null? lst) #f)
       ;Checks if the target is the first value in the list, if so returns #t to indicate element was in list.;
       ((eqv? e (car lst)) #t)
       #|If the list was not empty, and the target value was not the first item, recursively calls member? on the remainder 
         of the list to determine if the target value occurs later in the list. With this default condition, no truth value
         is returned.
       |#
       (else (member? e (cdr lst)))
     )
  )

#|Defines a function named set? that given a list
  (either chars, strings, ints or floats) will determine if the list is
  a well formed set - a set with no duplicates. The function takes as its 
  argument a list named lst.
|#
(define (set? lst)
  ;Allows us to trace the function set?;
  ;(trace set?);
  
  ;the following is a series of conditionals to determine if lst is a well-formed set;
  (cond
       ;Returns true if lst is null, because a null list contains no duplicates; 
       ((null? lst) #t)
       ;Returns true if lst is just 1 element long, because it could not have any duplicates; 
       ((= 1 (length lst)) #t)      
       ;If lst is greater than 1, we need to check for duplicates;
       (else  
        #|Because the duplicate value (if it exists) could appear anywhere in the 
          list, we loop through the list to check for duplicate values. Our member?
          function (used to check for duplicate entries) requires a element to check
          for and a list of elements to check - so we run the check with each element 
          of the list.
        |#
          ;Sets an iterator i (initialized to 0, to use in iterating through the list;
          (let loop ([i 0])
           
          ;Checks if it is our first time through the list (that is, if i = 0);  
          (when (> i 0) 
              ;If it is not the first time through the list, removes the first element (which has already been checked)
              (set! lst (cdr lst)))
            
            #|Checks if there are elements remaining in the list (if there are not, entire list has been searched for duplicates).
              Once there are no elements remaining in the list, we break out of the loop.
            |#
            (unless (equal? 0 (+ 1(length lst)))
                    ;Series of conditions to test for duplicate values in the list;
                    (cond
                         ;If the list is null, return true - we have not found a duplicate in the list;
                         ((null? lst) #t)
                      
                         #|Calls the member? function above to determine if the first element of the list is present
                           in the remaining part of the list. If it is, and the member? function returns true - we 
                           return a value of false, because that means we have found a duplicate entry.
                         |#
                         ((equal? (member? (car lst)(cdr lst)) #t) #f)
                         
                         #|If we have not found a duplicate entry using the first value in the list, we repeat the loop
                           because that is no guarantee that a duplicate entry does not occur later in the list. We increment
                           i and run the loop again.
                         |#
                         (else (loop (+ i 1)))
                      )
              )
            )
          )
       )
  )
      
  

  

  
  
     
     

  
       
  

  
  
  
  
  
  
  
    


 

  