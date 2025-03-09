#include <windows.h>
#include <iostream>
#include <conio.h>

int main () {
  
    const wchar_t *file = L"PATH TO PIC(S)";
    getch();
    int ret = SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, (void *)file, SPIF_UPDATEINIFILE);
    std::cout << ret << std::endl;
    getch();
}
