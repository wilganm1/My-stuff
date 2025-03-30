----------------------------------------SIZERS----------------------------------------

Sizers control how panels, buttons, etc. act when dimensions of the window changes
Panels do not change size when the window expands or contracts withouth sizers.

Panels must be associated with the frame then added to a sizer later.
                        wxPanel* panel = new wxPanel(this, wxID_ANY);
                        wxBoxSizer* sizer = new wxBoxSizer(wxVERTICAL);

                        sizer->Add(panel, 1, wxEXPAND);

To have multiple sizers in one frame add a sizer to another sizer

                        wxBoxSizer* sizer = new wxBoxSizer(wxVERTICAL);
                        wxBoxSizer* sizer2 = new wxBoxSizer(wxHORIZONTAL);
                        sizer1->Add(sizer2, 1, wxEXPAND);

When adding mutliple panels to a 2nd sizer you need to have a proportion and wxEXPAND to 
the panels AND to the second sizer

            wxBoxSizer* sizer = new wxBoxSizer(wxVERTICAL);

            wxBoxSizer* sizer2 = new wxBoxSizer(wxHORIZONTAL);
          
            sizer2->Add(panel2, 2, wxEXPAND);
            sizer2->Add(panel3, 1, wxEXPAND);
          
            sizer->Add(sizer2, 1, wxEXPAND); // Sizer 2 ges added to sizer 1. Proportionality 
          
            this->SetSizerAndFit(sizer);


  CANNOT DO this->SetSizerAndFit() TO MULTIPLE SIZERS, JUST ONE. ANY ADDITIONAL SIZERS MUST BE 
    ADDED TO ANOTHER SIZER.

When putting a panel inside another panel with a sizer, first define nested panel as a child of
its parent panel
                                            |
                    /* child */             v // parent
            wxPanel* panel3 = new wxPanel(panel2, wxID_ANY, wxDefaultPosition, wxDefaultSize);
                                            ^
                                            |  
  Then add panel 1 & 2 to sizer 1
                      wxBoxSizer* sizer = new wxBoxSizer(wxVERTICAL);
                      sizer->Add(panel1, 1, wxEXPAND | wxALL, 10);
                      sizer->Add(panel2, 1, wxEXPAND | wxALL, 10);

  Then create a 2nd sizer, add panel 3 to it, then Set sizer 2 to panel2

                      wxBoxSizer* sizer2 = new wxBoxSizer(wxHORIZONTAL);
                      sizer2->Add(panel3, 1, wxEXPAND | wxALL, 10);
                      panel2->SetSizerAndFit(sizer2);
                                              
                     this->setSizerAndFit(sizer);


Center one sizer inside another.

                    wxBoxSizer* sizer2 = new wxBoxSizer(wxVERTICAL);
                    wxBoxSizer* sizer3 = new wxBoxSizer(wxHORIZONTAL);  // CENTERING
                    sizer3->Add(panel3, 0, wxALIGN_CENTER);
                    sizer2->Add(sizer3, 1, wxALIGN_CENTER | wxALL, 10);
                    panel2->SetSizerAndFit(sizer2);

----------------------------------------SPLITERS----------------------------------------
Splitters are like automatic sizers that split  2+ panels with an adjustable borders between them.

Splitters are controls like panels, and are treated like them.

          wxSplitterWindow* splitter = new wxSplitterWindow(this, wxID_ANY, wxDefaultPosition,
                                                              wxDefaultSize,
                                                              wxSP_BORDER | wxSP_LIVE_UPDATE);
        
          wxPanel* left = new wxPanel(splitter);
          wxPanel* right = new wxPanel(splitter);
        
          left->SetBackgroundColour(wxColor(145,60,2));
          right->SetBackgroundColour(wxColor(240,224,97));
        
          splitter->SetMinimumPaneSize(200);
        
          splitter->SplitVertically(left,right);

If you want multiple spiltters you need to make the 2nd splitter a child of the 1st.

         wxSplitterWindow* splitter = new wxSplitterWindow(this, wxID_ANY, wxDefaultPosition, wxDefaultSize,
                                                    wxSP_BORDER | wxSP_LIVE_UPDATE);
      
         wxSplitterWindow* splitter2 = new wxSplitterWindow(splitter, wxID_ANY, wxDefaultPosition, wxDefaultSize,
                /* Child of splitter1 */                   wxSP_BORDER | wxSP_LIVE_UPDATE);
      
      
         wxPanel* panel1 = new wxPanel(splitter);
         wxPanel* panel2 = new wxPanel(splitter2); //child of splitter 2
         wxPanel* panel3 = new wxPanel(splitter2); // child of splitter 2
      
         panel1->SetBackgroundColour(wxColor(145,60,2));
         panel2->SetBackgroundColour(wxColor(240,224,97));
         panel3->SetBackgroundColour(wxColor(0,12,177));
      
         splitter2->SplitHorizontally(panel2,panel3); 
      
         splitter->SplitVertically(panel1, splitter2); // Splits between panel and splitter

An easy way to think of splitters is to think of them as a panel made up of 2 individual panels.
