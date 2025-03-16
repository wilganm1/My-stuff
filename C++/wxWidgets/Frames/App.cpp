/***************************************************************
 * Name:      [PROJECT NAME]App.cpp
 * Purpose:   Code for Application Class
 * Author:     ()
 * Created:   2025-03-12
 * Copyright:  ()
 * License:
 **************************************************************/

#ifdef WX_PRECOMP
#include "wx_pch.h"
#endif

#ifdef __BORLANDC__
#pragma hdrstop
#endif //__BORLANDC__

#include "[PROJECT NAME]App.h"
#include "[PROJECT NAME]Main.h"

IMPLEMENT_APP([PROJECT NAME]App);

bool [PROJECT NAME]App::OnInit()
{
    [PROJECT NAME]Frame* frame = new [PROJECT NAME]Frame(0L, _("wxWidgets Application Template"));
    frame->SetIcon(wxICON(aaaa)); // To Set App Icon
    frame->Show();
    
    return true;
}
