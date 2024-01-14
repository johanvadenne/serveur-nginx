@ECHO OFF
ECHO Starting PHP FastCGI...
set PATH=.\PHP;%PATH%
.\RunHiddenConsole.exe .\PHP\php-cgi.exe -b 127.0.0.1:9000