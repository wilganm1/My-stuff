------------------------------------BASICS------------------------------------
jQuery is lightweight library to make writing JavaScript easier

You can either download jQuery as a JavaScirpt file or get it from Google.

  From CDN: 
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head> 

 All jQuery code must be within a document function.
 
    $(document).ready(function(){
    // jQuery methods go here...
     }); 

Syntax:   $("selector").action()
            -$ access jQuery;
            -selector finds the elements;
            -action() is what is performed
 A selector can be any HTML tag, id, class name.
           
-Events:
  All events have this syntax: 
                  $("selector").event(function(){
                      // action here;
                  });
      .click();
      .dblclick();
      .mouseenter();    //same as hover
      .mouseleave();
      .hover();
      .mousedown();    //any mouse button clicked
      .mouseup();     //mouse released   
        


 -Effects. Things that are done to stuff.;
      They can refer to other HTML elements OR can refer to
      the tag that is selected using
            $("selector").action(function(){
              :$(this).(~~~);});
    List of effects:
      .hide();
      .show();
      .toggle();
      .fadeIn();
      .fadeOut();
      .fadeToggle();
      .fadeTo(speed, opacity);
      .slideDown();
      .slideUp();
      .slideToggle();   //both slide up & down
      .animate({params}, speed)            //params can be stuff like height, opacity, etc
      .


    
    
    
    
