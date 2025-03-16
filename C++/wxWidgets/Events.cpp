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

Then back in the mainframe.cpp file write this code to define the command in the mainframe:

 void MainFrame::OnButtonClicked(wxCommandEvent& evt){
    wxLogStatus("Button Clicked");
}

- Binding the command to the control
Easy way to bind events to their handlers is to use the Bind() function

    wxButton* button = new wxButton(panel, wxID_ANY, "Title", wxPoint(100,200), wxDefaultSize);

    button->Bind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this); // Binds event to handle

    CreateStatusBar();   //  Shows event

   button->Unbind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this); // Unbinds event

  
