---------------------------------SIZERS---------------------------------

Sizers control how panels and contrls act when dimensions of the window changes

When adding mutliple panels to a 2nd sizer you need to have a proportion and wxEXPAND to the panels AND 
to the second sizer

            wxBoxSizer* sizer = new wxBoxSizer(wxVERTICAL);

            wxBoxSizer* sizer2 = new wxBoxSizer(wxHORIZONTAL);
          
            sizer2->Add(panel2, 2, wxEXPAND);
            sizer2->Add(panel3, 1, wxEXPAND);
          
            sizer->Add(sizer2, 1, wxEXPAND); // Sizer 2 ges added to sizer 1. Proportionality 
          
            this->SetSizerAndFit(sizer);


  CANNOT DO this->SetSizerAndFit() TO MULTIPLE SIZERS, JUST ONE. ANY ADDITIONAL SIZERS MUST BE 
    ADDED TO ANOTHER SIZER.
        

