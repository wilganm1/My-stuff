Events are things that happen within the GUI that can be responded to.

- Event handlers
When things happend they must be handled by the mainframe then implemented. Event handlers
need to be bound to button that controls them.

Write this code in the mainframe.h file inside the mainframe class:

  private:
    void OnButtonClicked(wxCommandEvent& evt);   // When button is clicked
    void OnSliderChanged(wxCommandEvent& evt);   // when slider is changed
    void OnTextChanged(wxCommandEvent& evt);    // when text changes in box
    //Add whatever other events here

Then back in the mainframe.cpp file write this code to define the event handler in the mainframe:

 void MainFrame::OnButtonClicked(wxCommandEvent& evt){
    wxLogStatus("Button Clicked");
}

- Binding the command to the control
Easy way to bind events to their handlers is to use the Bind() function

    wxButton* button = new wxButton(panel, wxID_ANY, "Title", wxPoint(100,200), wxDefaultSize);

    button->Bind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this); // Binds event to handle

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

              Header file
     private:
        void OnAnyButtonClicked(wxCommandEvent& evt);
        void OnButton1Clicked(wxCommandEvent& evt);
        void OnButton2Clicked(wxCommandEvent& evt);

              .cpp file

    void MainFrame::OnAnyButtonClicked(wxCommandEvent& evt){
        wxLogStatus("Button Clicked");
        evt.Skip();      <-- This skips the current-level binding and moves it up a level

    void MainFrame::OnButton1Clicked(wxCommandEvent& evt){
        wxLogStatus("Button Clicked");

            now bind button1 to the event handle

    button1->Bind(wxEVT_BUTTON, &MainFrame::OnButton1Clicked, this);


--------------MOUSE EVENTS--------------
Events that happend with the mouse: moving, clicking, holding,

        in header file
  private:
    void OnMouseEvent(wxMouseEvent& evt);
  
