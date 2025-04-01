#include "MainFrame.h"
#include <wx/wx.h>
#include <wx/event.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/imagjpeg.h>
#include <wx/splitter.h>


MainFrame::MainFrame(const wxString& title): wxFrame(nullptr, wxID_ANY, title){

  wxInitAllImageHandlers();

  wxSplitterWindow* splitter = new wxSplitterWindow(this, wxID_ANY, wxDefaultPosition,
                                                              wxDefaultSize,
                                                              wxSP_BORDER | wxSP_LIVE_UPDATE);
  wxPanel* left = new wxPanel(splitter);
  wxPanel* right = new wxPanel(splitter);
  left->SetBackgroundColour(wxColor(145,60,2));
  right->SetBackgroundColour(wxColor(240,224,97));
  splitter->SetMinimumPaneSize(50);
  splitter->SplitVertically(left,right);


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

  wxBoxSizer* sizer = new wxBoxSizer(wxVERTICAL);

  sizer->AddStretchSpacer(0);
  sizer->Add(staticText, 0, wxALL, 10);
  sizer->AddSpacer(1);
  sizer->Add(blackJackButton, 0, wxALL, 10);
  sizer->AddSpacer(1);
  sizer->Add(hangmanButton, 0, wxALL, 10);
  sizer->AddSpacer(1);
  sizer->Add(ticButton, 0, wxALL, 10);
  sizer->AddStretchSpacer(1);
  left->SetSizerAndFit(sizer);

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
