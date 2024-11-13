@echo off
echo hello desktop > "%USERPROFILE%\Desktop\desktop.txt"

echo hello download > "%USERPROFILE%\Downloads\download.txt"



move "%USERPROFILE%\Desktop\desktop.txt" "%USERPROFILE%\Downloads"
move "%USERPROFILE%\Downloads\download.txt" "%USERPROFILE%\Desktop"


mkdir "%USERPROFILE%\Desktop\NewFolder"

netstat > "%USERPROFILE%\Desktop\netstat_output.txt"

findstr ":80 " "%USERPROFILE%\Desktop\netstat_output.txt" > nul
if %errorlevel% equ 0 (
    echo Port 80 is active.
) else (
    echo Port 80 is not active.
)

del "%USERPROFILE%\Desktop\desktop.txt"
del "%USERPROFILE%\Downloads\download.txt"
del "%USERPROFILE%\Desktop\netstat_output.txt"

echo process complete
pause
