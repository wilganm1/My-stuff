#include <wx/spinctrl.h>
#include <wx/clrpicker.h>
#include <wx/datectrl.h>
#include <wx/fontpicker.h>

/*  These control have to be within the main frame class inside the MainFrame.cpp file, or whatever it's called. NOT the App.cpp file


 If you don't want a specific size just use wxDefaultSize

 Avoid using wxDefaultPosition because it will send it to the top left corner.

 Using -1 for value of wxSize just makes it the default size */

{
    wxPanel* panel = new wxPanel(this); // Creates a panel to put in controls freely
            // this keyword refers to the Frame class it belongs to
// BUTTON
    wxButton* button = new wxButton(panel, wxID_ANY, "Gook", wxPoint(x,y), wxSize(width, height));
 
// CHECK BOX
    wxCheckBox* checkBox = new wxCheckBox(panel, wxID_ANY, "TITLE", wxPoint(x, y)); 

// STATIC TEXT
    wxStaticText* staticText = new wxStaticText(panel, wxID_ANY, "TITLE", wxPoint(x, y)); 

// TEXT CONTROL
    wxTextCtrl* textCtrl = new wxTextCtrl(panel, wxID_ANY, "TITLE", wxPoint(x,y));

// SLIDER
    wxSlider* slider = new wxSlider(panel, wxID_ANY, 25, 0, 100, wxPoint(x, y)); 
 
// GAUGE (PROGRESS BAR)
    wxGauge* gauge = new wxGauge(panel, wxID_ANY, 100, wxPoint(x, y), wxDefaultSize, wxGA_SMOOTH); 
    gauge->SetValue(n);   // sets initial value of progress bar. Not percentage based

// DROP DOWN MENU
    wxArrayString choices; // drop down menu choices
    choices.Add("A");
    choices.Add("B");
    choices.Add("C");

    wxChoice* choice = new wxChoice(panel, wxID_ANY, wxPoint(x, y), wxSize(100, -1), choices); 
    choice->Select(0); //  sets default choice that appears in box

// RADIO BOX
    wxRadioBox* radioBox = new wxRadioBox(panel, wxID_ANY, "TITLE", wxPoint(x, y), wxDefaultSize, choices);

// SPIN CONTROL
    wxSpinCtrl* spinCtrl = new wxSpinCtrl(panel, wxID_ANY, "TITLE" wxPoint(x, y);

// LIST BOX
    wxListBox* listBox = new wxListBox(panel, wxID_ANY, wxPoint(x, y), wxSize(width, -1), choices);
 
// COLOR PICKER
    wxColourPickerCtrl* colourPicker = new wxColourPickerCtrl(panel, wxID_ANY, wxColour(*wx[COLOR]);
                        // colors available: BLACK, BLUE, CYAN, GREEN, YELLOW, LIGHT GREY, RED, WHITE

// DATE PICKER
    wxDatePickerCtrl* datePicker = new wxDatePickerCtrl(panel, wxID_ANY, wxDefaultDateTime, wxPoint(x, y), wxDefaultSize);

// FONT PICKER
    wxFontPickerCtrl* FontPicker = new wxFontPickerCtrl(panel, wxID_ANY, wxNullFont, wxPoint(x, y), wxDefaultSize);
 
// SCROLL BAR
    wxScrollBar* scrollBar = new wxScrollBar(panel, wxID_ANY, wxPoint(x, y), wxDefaultSize, wxSB_HORIZONTAL);

// FILE PICKER
    wxFilePickerCtrl* filePickerCtrl = new wxFilePickerCtrl(panel, wxID_ANY, wxString([default path shown. if blank replace this with wxEMPTYSTRING]), wxString("Select File"), wxFileSelectorDefaultWildcardStr, wxPoint(x, y), wxDefaultSize);
 
// DIRECTORY PICKER
    wxDirPickerCtrl* dirPickerCtrl = new wxDirPickerCtrl(panel, wxID_ANY);

// MENU
    wxMenuBar* menuBar = new wxMenuBar;
    wxMenu* fileMenu = new wxMenu;
    menuBar->Append(fileMenu,_("&File")); // Creates "File" item

    wxMenu* editMenu = new wxMenu;
    menuBar->Append(editMenu,_("&Edit")); // Creates "Edit" item

    // Add options to menu itesm
    fileMenu->Append(wxID_NEW);
    fileMenu->Append(wxID_OPEN);
    fileMenu->AppendSeparator();
    fileMenu->Append(wxID_SAVE);
    fileMenu->Append(wxID_SAVEAS);
    fileMenu->Append(wxID_EXIT);

    // Custom Menu item
    fileMenu->Append(wxID_ANY,_("&[NAME]\t[SHORTCUT]"));

    // Create Submenu
    wxMenu* subMenu = new wxMenu;
    subMenu->Append(wxID_CUT);
    fileMenu->AppendSubMenu(subMenu,_("Sub Menu"));

 
}
