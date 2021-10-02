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
     Element()
       .background(Color.green)
       .font(12)
       .foregroundColor(Color. )
       .frame(width: x, height: y)
  SwiftUI has preprogrammed modifiers for every single element.

-Stacking. Think of these like frames.
    
   -VStack. Stacks multiple elements into one single frame vertically.
   -HStack. Horizontally stacks elements.
   -ZStack. Stacks things on top of each other.


Get max width & height of child element possible.
         .frame(maxWidth: .infinity,
                maxHeight: .infinity)

//  Add navigation buttons at top right corner
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {     //Need to add this to have a navigation bar
            Text("SwiftUI").  //This can be anything.
                .toolbar {
                    ToolbarItemGroup(placement: .navigationBarTrailing) {
                        Button("+") {
                            print("about tapped!")
                        }
                    }
                }
            
        }
    }
}
