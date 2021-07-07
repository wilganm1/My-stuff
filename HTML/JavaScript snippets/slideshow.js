 <!-- Slideshow container -->
<div class="slideshow-container">
 <div class="mySlides fade">
    <img src="math.jpg" style="width:100%"></div>   //insert as many images as you want
 <div class="mySlides fade">
    <img src="eye.jpg" style="width:100%"></div>
 <div class="mySlides fade">
    <img src="computer_science.jpg" style="width:100%"></div>
 <div class="mySlides fade">
    <img class="mySlides fade" src="periodic_table.jpg" style="width:100%"></div>
</div>

<script>
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;        //index variable
  var slides = document.getElementsByClassName("mySlides");
      /*this syntax retrives the images within the same document. 
        The images need the same class */
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";}
    /* This is the looping function that tells the function showSlides
       to move onto the next index within the images array */
  slideIndex++;  //This causes the next image to actually show.
  if (slideIndex > slides.length) {slideIndex = 1}
      /*This tells the function showSlides to reset to the first image
            once the last image is shown */
 slides[slideIndex-1].style.display = "block";
 dots[slideIndex-1].className += " active";
 setTimeout(showSlides, 2000); //change image every 2 seconds
}                            //1000 = 1 second
 </script>

/* CSS for the slideshow */

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
