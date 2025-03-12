    //    First create a class for the box

#include <wx/button.h>
#include <wx/statline.h>
class [PROJECT_NAME]Dialog: public wxDialog
{
    public:
        [PROJECT_NAME]Dialog(wxDialog *dlg, const wxString& title);
        ~[PROJECT_NAME]Dialog();

    protected:
        enum
        {
            idBtnQuit = 1000,
            idBtnAbout
        };
        wxStaticText* m_staticText1;
        wxButton* BtnAbout;
        wxStaticLine* m_staticline1;
        wxButton* BtnQuit;

    private:
        void OnClose(wxCloseEvent& event);
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        DECLARE_EVENT_TABLE()
};

    //   Create event table

BEGIN_EVENT_TABLE([PROJECT_NAME]Dialog, wxDialog)
    EVT_CLOSE([PROJECT_NAME]Dialog::OnClose)
    EVT_BUTTON(idBtnQuit, [PROJECT_NAME]Dialog::OnQuit)
    EVT_BUTTON(idBtnAbout, [PROJECT_NAME]Dialog::OnAbout)
END_EVENT_TABLE()

    //     Create dialog box object from class aboce

[PROJECT_NAME]Dialog::[PROJECT_NAME]Dialog(wxDialog *dlg, const wxString &title)
    : wxDialog(dlg, -1, title)
{
    this->SetSizeHints(wxDefaultSize, wxDefaultSize);
    wxBoxSizer* bSizer1;
    bSizer1 = new wxBoxSizer(wxHORIZONTAL);
    m_staticText1 = new wxStaticText(this, wxID_ANY, wxT("Welcome To\nwxWidgets"), wxDefaultPosition, wxDefaultSize, 0);
    m_staticText1->SetFont(wxFont(20, 74, 90, 90, false, wxT("Arial")));
    bSizer1->Add(m_staticText1, 0, wxALL|wxEXPAND, 5);
    wxBoxSizer* bSizer2;
    bSizer2 = new wxBoxSizer(wxVERTICAL);
    BtnAbout = new wxButton(this, idBtnAbout, wxT("&About"), wxDefaultPosition, wxDefaultSize, 0);
    bSizer2->Add(BtnAbout, 0, wxALL, 5);
    m_staticline1 = new wxStaticLine(this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxLI_HORIZONTAL);
    bSizer2->Add(m_staticline1, 0, wxALL|wxEXPAND, 5);
    BtnQuit = new wxButton(this, idBtnQuit, wxT("&Quit"), wxDefaultPosition, wxDefaultSize, 0);
    bSizer2->Add(BtnQuit, 0, wxALL, 5);
    bSizer1->Add(bSizer2, 1, wxEXPAND, 5);
    this->SetSizer(bSizer1);
    this->Layout();
    bSizer1->Fit(this);
}

    //    Add in destructor and exit commands

[PROJECT_NAME]Dialog::~[PROJECT_NAME]Dialog()
{
}

void [PROJECT_NAME]Dialog::OnClose(wxCloseEvent &event)
{
    Destroy();
}

void [PROJECT_NAME]Dialog::OnQuit(wxCommandEvent &event)
{
    Destroy();
}


