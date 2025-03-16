Events are things that happen within the GUI that can be responded to.

Events need IDs to keep track of what happens.


enum IDs {               // Must be positive
  BUTTON_ID = 2;         // Can't be 0 or 1
};
                                        // ID
wxButton* button = new wxButton(panel, BUTTON_ID, "Tit", wxPoint(100,200), wxDefaultSize);

- Event handlers
When things happend they must be handled by the mainframe then implemented. Event handlers
need to be bound to button that controls them. Do this by making an event table.

Do write this code in the mainframe.h file inside the mainframe class:

  private:
    void OnButtonClicked(wxCommandEvent& evt);
    wxDECLARE_EVENT_TABLE();

Then back in the mainframe.cpp file write this code:

  void void MainFrame::OnButtonClicked(wxCommandEvent& evt){
    wxLogStatus("Button Clicked");
}

Back in the MainFrame.cpp file, begin the event table

  wxBEGIN_EVENT_TABLE([event table class], [base class])
     EVT_BUTTON(BUTTON_ID, MainFrame::OnButtonClicked)
  wxEND_EVENT_TABLE()
  
