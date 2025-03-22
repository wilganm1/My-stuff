#include <wx/spinctrl.h>

/*  These control have to be within the main frame class inside the MainFrame.cpp file, or whatever it's called. NOT the App.cpp file


 If you don't want a specific size just use wxDefaultSize

 Avoid using wxDefaultPosition because it will send it to the top left corner.

 Using -1 for value of wxSize just makes it the default size */

{
    wxPanel* panel = new wxPanel(this); // Creates a panel to put in controls freely
            // this keyword refers to the Frame class it belongs to

    wxButton* button = new wxButton(panel, wxID_ANY, "Gook", wxPoint(x,y), wxSize(width, height)); // Button

    wxCheckBox* checkBox = new wxCheckBox(panel, wxID_ANY, "TITLE", wxPoint(x, y)); // multiple choice check boxes

    wxStaticText* staticText = new wxStaticText(panel, wxID_ANY, "TITLE", wxPoint(x, y)); //permanent text

    wxTextCtrl* textCtrl = new wxTextCtrl(panel, wxID_ANY, "TITLE", wxPoint(x,y)); // Type in text

    wxSlider* slider = new wxSlider(panel, wxID_ANY, 25, 0, 100, wxPoint(x, y)); // Horizontal slider

    wxGauge* gauge = new wxGauge(panel, wxID_ANY, 100, wxPoint(x, y)); // progress bar
    gauge->SetValue(50);   // sets initial value of progress bar. Not percentage based

    wxArrayString choices; // drop down menu choices
    choices.Add("A");
    choices.Add("B");
    choices.Add("C");

    wxChoice* choice = new wxChoice(panel, wxID_ANY, wxPoint(x, y), wxSize(100, -1), choices); // drop down menu
    choice->Select(0); //  sets default choice that appears in box

    wxSpinCtrl* spinCtrl = new wxSpinCtrl(panel, wxID_ANY, "TITLE" wxPoint(x, y); // Click increment/decrement value

    wxListBox* listBox = new wxListBox(panel, wxID_ANY, wxPoint(x, y), wxSize(width, -1), choices); // Box of text in a vertical list

    wxColourPickerCtrl* colorPick = new wxColourPickerCtrl(panel, wxID_ANY, wxColour(*wx[COLOR]);
                        // colors available: BLACK, BLUE, CYAN, GREEN, YELLOW, LIGHT GREY, RED, WHITE



 

    wxRadioBox* radioBox = new wxRadioBox(panel, wxID_ANY, "TITLE", wxPoint(x, y), wxDefaultSize, choices); // single choice check box
}
