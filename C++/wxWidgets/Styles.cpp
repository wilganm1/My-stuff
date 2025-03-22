Styles change the look of objects in wxWidgets including: color, borders, fonts, alignment, etc.

Style parameters usually go after the size parameter and on CodeBlocks is highlighted by long style = 0
  
{
    // STATIC TEXT
  wxALIGN_CENTRE_HORIZONTAL  // Aligns static text in center horizontally

    // SLIDER
  wxSL_VALUE_LABEL    //  Displays current value in a slider
  
  // TEXT CONTROL 
  wxTE_PASSWORD       // Turns text into dots, like password entry
  
    // GAUGE
  wxGA_VERTICAL      //  Vertical gauge. Change wxSize so y is bigger than x

  // CHOICE BOX
  wxCB_SORT          //  Sort box in alphabetical order 
  
 // SPIN BOX
  wxSP_WRAP          //  Spin box can go wrap back around to 0 or 100
  
  // LIST BOX
  wxLB_MULTIPLE      //  Can select multiple items in list box  

 // RADIO BOX
  majorDim = 1       //  Lays out boxes vertically
    OR
 majorDim = n, wxRA_SPECIFY_ROWS   // n is the number of choices you have, style makes them vetical.

// DATE PICKER
  wxDP_DROPDOWN    // Uses a default calendar to select date
  
