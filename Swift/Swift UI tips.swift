import SwiftUI

struct ContentView: View {
  var body: some View {
    
     //insert code here
    
   }
}


To add in stuff to the view it must be a recognized SwiftUI element such as:
          Text()
          Button()

 -modifiers. These change characteristics of the elements.
     .background(Color.green)
     .font(12)
 
  SwiftUI has preprogrammed modifiers for every single elements


-Stacking stuff in a frame.
    
   -Vstack. Stacks multiple elements into one single frame vertically.
   -Hstack. Horizontally stacks elements.
