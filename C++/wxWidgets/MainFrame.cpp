#include "MainFrame.h"
#include <wx/wx.h>


MainFrame::MainFrame(const wxString& title): wxFrame(nullptr, wxID_ANY, title){

    // Insert controls here
    
}

void MainFrame::OnButtonClicked(wxCommandEvent& evt){    // function to display text on button click
    wxLogStatus("Button Clicked");
}
