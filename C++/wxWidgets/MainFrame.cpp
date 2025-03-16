#include "MainFrame.h"
#include <wx/wx.h>

enum IDs {       // Enum for IDs of controls
    BUTTON_ID = 2
};

wxBEGIN_EVENT_TABLE(MainFrame, wxFrame)                
    EVT_BUTTON(BUTTON_ID, MainFrame::OnButtonClicked)   // Event table to process events
wxEND_EVENT_TABLE()

MainFrame::MainFrame(const wxString& title): wxFrame(nullptr, wxID_ANY, title){
    wxPanel* panel = new wxPanel(this);

    wxButton* button = new wxButton(panel, BUTTON_ID, "Tit", wxPoint(100,200), wxDefaultSize);

    CreateStatusBar();

}

void MainFrame::OnButtonClicked(wxCommandEvent& evt){    // function to display text on button click
    wxLogStatus("Button Clicked");
}
