/* Events are things that happen within the GUI that can be responded to.

- Event handlers
When things happend they must be handled by the mainframe then implemented. Event handlers
need to be bound to button that controls them.*/

Write this code in the mainframe.h file inside the mainframe class: 

    private:
      void [NameOfMethod](wxCommandEvent& evt); // good practice is to name methods after function
      // example: void OnButtonClicked
    //Add whatever other events here

Then back in the mainframe.cpp file write this code to define the event handler outside the mainframe:

     void MainFrame::[NameOfMethod](wxCommandEvent& evt){
        wxLogStatus("Button Clicked");
    }

- Binding the command to the control
  Easy way to bind events to their handlers is to use the Bind() function

    wxButton* button = new wxButton(panel, wxID_ANY, "Title", wxPoint(100,200), wxDefaultSize);

    button->Bind(wxEVT_BUTTON, &MainFrame::[NameOfMethod], this); // Binds event to handle

    CreateStatusBar();   //  Shows event

    button->Unbind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this); // Unbinds event


---------------EVENT PROPOGATION----------------
Event propogation is the idea that events are handled not by a specific control (button), but 
by the panel/frame the control is in.


                                 ___________________
                                 |                 |
                                 |      Frame      |
                                 |_________________|
                                          
                                         /|\
                                        / | \
                                          |
                     ____________________________________________
                     |                                          |
                     |                  Panel                   |
                     |__________________________________________|
                             /|\                         /|\
                            / | \                       / | \
                              |                           |
                    ___________________          ___________________      
                    |                 |          |                 |
                    |      Button 1   |          |     Button 2    |
                    |_________________|          |_________________|
  

 - All you have to do is use the this keyword when binding a control:

      this->Bind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this);  // binds to panel

- If you want separate events for each button, create their own event handles.

              MainFrame.h file
     private:
        void OnAnyButtonClicked(wxCommandEvent& evt);
        void OnButton1Clicked(wxCommandEvent& evt);
        void OnButton2Clicked(wxCommandEvent& evt);

              MainFrame.cpp file

    void MainFrame::OnAnyButtonClicked(wxCommandEvent& evt){
        wxLogStatus("Button Clicked");
        evt.Skip();      <-- This skips the current-level binding and moves it up a level

    void MainFrame::OnButton1Clicked(wxCommandEvent& evt){
        wxLogStatus("Button Clicked");

            now bind button1 to the event handle

    button1->Bind(wxEVT_BUTTON, &MainFrame::OnButton1Clicked, this);


--------------MOUSE EVENTS--------------
Events that happend with the mouse: moving, clicking, holding,

       // MainFrame.h
  private:
    void OnMouseEvent(wxMouseEvent& evt);

      // in MainFrame.cpp

void MainFrame::MouseEvent(wxMouseEvent& evt){
    // whatever
}
 //  https://docs.wxwidgets.org/3.0/classwx_mouse_event.html

--------------KEYBOARD EVENTS--------------
Events that use keyboard. Press or release keys.

      // MainFrame.h
  private:
      void OnKeyEvent(wxKeyEvent& evt);

      // in MainFrame.cpp

  control->Bind(wxEVT_[], &MainFraime::OnKeyEvent, this);
            // KEY_DOWN, KEY_UP, KEY_CHAR

  void MainFrame::OnKeyEvent(wxKeyEvent& evt){
      wxChar keyChar = evt.GetUnicodeKey();   //
      wxLogStatus("Key Event %c", keyChar);
  }

   evt.GetEventType()   // checks what event type happens. Use for if statements

https://docs.wxwidgets.org/3.0/classwx_key_event.html

