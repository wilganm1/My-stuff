/***************************************************************
 * Name:      wx_testMain.h
 * Purpose:   Defines Application Frame
 * Author:     ()
 * Created:   2025-03-11
 * Copyright:  ()
 * License:
 **************************************************************/

#ifndef WX_TESTMAIN_H
#define WX_TESTMAIN_H

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include "wx_testApp.h"


#include <wx/button.h>
#include <wx/statline.h>
class wx_testDialog: public wxDialog
{
    public:
        wx_testDialog(wxDialog *dlg, const wxString& title);
        ~wx_testDialog();

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

#endif // WX_TESTMAIN_H
