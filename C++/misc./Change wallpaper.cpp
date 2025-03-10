#include <windows.h>
#include <iostream>
#include <chrono>

int main () {
    const wchar_t* pics[] = {L"", L"", L""}; // <-- PATH TO PICS. Have to enter each one manually
    int i;
    while (1) {             //optional. Makes it infinite
      for (i=0; i < 5; i++){
          SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, (void *)pics[i], SPIF_UPDATEINIFILE);
          Sleep(1000);  // in milliseconds.
          };
    }
    return 0:
};
