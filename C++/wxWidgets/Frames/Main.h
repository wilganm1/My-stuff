/***************************************************************
 * Name:      [PROJECT NAME]Main.h
 * Purpose:   Defines Application Frame
 * Author:     ()
 * Created:   2025-03-12
 * Copyright:  ()
 * License:
 **************************************************************/

#ifndef [PROJECT NAME]MAIN_H
#define [PROJECT NAME]MAIN_H

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include "[PROJECT NAME]App.h"

class [PROJECT NAME]Frame: public wxFrame
{
    public:
        [PROJECT NAME]Frame(wxFrame *frame, const wxString& title);
        ~[PROJECT NAME]Frame();
    private:
        enum
        {
            idMenuQuit = 1000,
            idMenuAbout
        };
        void OnClose(wxCloseEvent& event);
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        DECLARE_EVENT_TABLE()
};


#endif // [PROJECT NAME]MAIN_H
