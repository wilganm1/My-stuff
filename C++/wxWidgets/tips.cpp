---------------------------------SIZERS---------------------------------

Sizers control how panels and buttons, etc. act when dimensions of the window changes

Panels must be associated with the frame then added to a sizer later.

To have multiple sizers in one frame add a sizer to another sizer

                        sizer1->add(sizer2, 1, wxEXPAND);

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

When putting a panel inside another panel, first define nested panel as a child of its parent panel
                                            |
                                            v
            wxPanel* panel3 = new wxPanel(panel2, wxID_ANY, wxDefaultPosition,
                                            ^
                                            |

            

