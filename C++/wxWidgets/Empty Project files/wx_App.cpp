/***************************************************************
 * Name:      wx_testApp.cpp
 * Purpose:   Code for Application Class
 * Author:     ()
 * Created:   2025-03-11
 * Copyright:  ()
 * License:
 **************************************************************/

#ifdef WX_PRECOMP
#include "wx_pch.h"
#endif

#ifdef __BORLANDC__
#pragma hdrstop
#endif //__BORLANDC__

#include "wx_testApp.h"
#include "wx_testMain.h"

IMPLEMENT_APP(wx_testApp);

bool wx_testApp::OnInit()
{
    
    wx_testDialog* dlg = new wx_testDialog(0L, _("wxWidgets Application Template"));
    dlg->SetIcon(wxICON(aaaa)); // To Set App Icon
    dlg->Show();
    return true;
}
