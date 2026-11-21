-----Qt Creator tips-----

Qt is used to create Graphical User Interfaces (GUIs) that allow
users to interact with programs.

The main widget of a program is the window. Should only have 1 per 
application. All of widgets are "children" of the window


--Set up main window--
#include "mainwindow.h"
#include <QApplication>
#include <QWidget>

// Include header files for application components.
// ...

int main(int argc, char *argv[])
{
    QApplication [APP NAME](argc, argv);
    MainWindow [NAME OF MAIN WINDOW];  *** or you can use QWidget [name]

   [[[[[ ALL OTHER STUFF GOES HERE ]]]]]]]]

    [NAME OF MAIN WINDOW].show()
    return [APP NAME].exec();
}


--widgets--
Widgets are things that allow the user to interact with program. Text boxes,
buttons, scrollers, status bars, etc.

All widgets must have a #include <header> when using in file

MUST CREATE AND SET IT AS A CHILD OF A PARENT

   -coding:     
	 [WidgetClass] *[name of object] = new [WidgetClass]([text], &[name of parent])

    -Example: a button
           #include <QPushButton>
           QPushButton *button = new QPushButton("Press me", &window);

QCheckBox - Checkbox with a text label

QComboBox - Combines a button with a dropdown list

QCommandLinkButton - Vista style command link button

QDateEdit - Widget for editing dates based on the QDateTimeEdit widget

QDateTimeEdit - Widget for editing dates and times

QDial - Rounded range control (like a speedometer or potentiometer)

QDoubleSpinBox - Spin box widget that takes doubles

QFocusFrame - Focus frame which can be outside of a widget's normal paintable area

QFontComboBox - Combobox that lets the user select a font family

QLCDNumber - Displays a number with LCD-like digits

QLabel - Text or image display

QLineEdit - One-line text editor

QMenu - Menu widget for use in menu bars, context menus, and other popup menus

QProgressBar - Horizontal or vertical progress bar

QPushButton - Button user pushes

QRadioButton - Radio button with a text label

QScrollArea - Scrolling view onto another widget

QScrollBar - Vertical or horizontal scroll bar

QSizeGrip - Resize handle for resizing top-level windows

QSlider - Vertical or horizontal slider

QSpinBox - Spin box widget. Lets you choose between various values

QTabBar - Tab bar, e.g. for use in tabbed dialogs

QTabWidget - Stack of tabbed widgets

QTimeEdit - Widget for editing times based on the QDateTimeEdit widget

QToolBox - Column of tabbed widget items

QToolButton - Quick-access button to commands or options, usually used inside a QToolBar

QWidget - The base class of all user interface objects
