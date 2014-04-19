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


(define (set? lst)
  ;Allows us to trace the function set?;
  (trace set?)
  (cond
       ((null? lst) #t)
       ((= 1 (length lst)) #t)
       (else (for/list ([i lst])
             (* i i)))
             ;(member? i lst)))
  ))
  

  
  
     
     

  
       
  

  
  
  
  
  
  
  
    


 

  