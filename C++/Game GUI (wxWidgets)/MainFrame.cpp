#include "MainFrame.h"
#include <wx/wx.h>
#include <wx/event.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/imagjpeg.h>
#include <wx/splitter.h>


MainFrame::MainFrame(const wxString& title): wxFrame(nullptr, wxID_ANY, title){


  wxSplitterWindow* splitter = new wxSplitterWindow(this, wxID_ANY, wxDefaultPosition,
                                                              wxDefaultSize,
                                                              wxSP_BORDER | wxSP_LIVE_UPDATE);
  wxPanel* left = new wxPanel(splitter);
  wxPanel* right = new wxPanel(splitter);
  left->SetBackgroundColour(wxColor(145,60,2));
  right->SetBackgroundColour(wxColor(240,224,97));
  splitter->SetMinimumPaneSize(50);
  splitter->SplitVertically(left,right);

  /*    INSTEAD OF SPLITTER JUST USE 2 PANELS
  wxPanel *panel1 = new wxPanel(this, wxID_ANY);
        panel1->SetBackgroundColour(*wxRED);

        wxPanel *panel2 = new wxPanel(this, wxID_ANY);
        panel2->SetBackgroundColour(*wxBLUE);

        wxBoxSizer *sizer = new wxBoxSizer(wxHORIZONTAL);
        sizer->Add(panel1, 1, wxEXPAND | wxALL, 5);
        sizer->Add(panel2, 1, wxEXPAND | wxALL, 5);

        this->SetSizer(sizer);
        this->SetSize(400, 200);
        this->Centre();

  */







  wxStaticText* staticText = new wxStaticText(left, wxID_ANY, "Select a game");
  staticText->SetForegroundColour(*wxWHITE);
  staticText->SetBackgroundColour(*wxBLACK);

  wxButton* blackJackButton = new wxButton(left, wxID_ANY, "Blackjack");
  blackJackButton->Bind(wxEVT_BUTTON, &MainFrame::onBlackjackButtonClicked, this);
  blackJackButton->Bind(wxEVT_ENTER_WINDOW, &MainFrame::onMouseOver,this);
  blackJackButton->Bind(wxEVT_LEAVE_WINDOW, &MainFrame::onMouseOver,this);

  wxButton* hangmanButton = new wxButton(left, wxID_ANY, "Hangman");
  hangmanButton->Bind(wxEVT_BUTTON, &MainFrame::onHangmanButtonClicked, this);
  hangmanButton->Bind(wxEVT_ENTER_WINDOW, &MainFrame::onMouseOver,this);
  hangmanButton->Bind(wxEVT_LEAVE_WINDOW, &MainFrame::onMouseOver,this);

  wxButton* ticButton = new wxButton(left, wxID_ANY, "Tic Tac Toe");
  ticButton->Bind(wxEVT_BUTTON, &MainFrame::onTicButtonClicked, this);
  ticButton->Bind(wxEVT_ENTER_WINDOW, &MainFrame::onMouseOver,this);
  ticButton->Bind(wxEVT_LEAVE_WINDOW, &MainFrame::onMouseOver,this);

  wxBoxSizer* sizerLeft = new wxBoxSizer(wxVERTICAL);

  sizerLeft->AddStretchSpacer(0);
  sizerLeft->Add(staticText, 0, wxALL, 10);
  sizerLeft->AddSpacer(1);
  sizerLeft->Add(blackJackButton, 0, wxALL, 10);
  sizerLeft->AddSpacer(1);
  sizerLeft->Add(hangmanButton, 0, wxALL, 10);
  sizerLeft->AddSpacer(1);
  sizerLeft->Add(ticButton, 0, wxALL, 10);
  sizerLeft->AddStretchSpacer(1);
  left->SetSizerAndFit(sizerLeft);

  CreateStatusBar();

}

// Events

void MainFrame::onBlackjackButtonClicked(wxCommandEvent& evt){

}

void MainFrame::onHangmanButtonClicked(wxCommandEvent& evt){
}

void MainFrame::onTicButtonClicked(wxCommandEvent& evt){
}

void MainFrame::onMouseOver(wxMouseEvent& evt){
    if(evt.GetEventType() == wxEVT_ENTER_WINDOW) {
        wxButton* evtt = (wxButton*)evt.GetEventObject();
        wxString label = evtt->GetLabel();
        wxLogStatus("Play " + label);

    }
    else if (evt.GetEventType() == wxEVT_LEAVE_WINDOW){
        wxLogStatus("");
    }


}
