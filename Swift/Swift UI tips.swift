import SwiftUI

struct ContentView: View {
  var body: some View {
    
     //insert code here
    
   }
}

To add in stuff to the view it must be a recognized SwiftUI element such as:
       Text()
       Button()
       Image()

 -Modifiers. These change characteristics of the elements.
     .background(Color.green)
     .font(12)
 
  SwiftUI has preprogrammed modifiers for every single element.

-Stacking stuff in a frame.
    
   -VStack. Stacks multiple elements into one single frame vertically.
   -HStack. Horizontally stacks elements.
   -ZStack. Stacks things on top of each other.
