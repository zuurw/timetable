@echo off
title tableTimes
type graphics.txt
:menu
            REM Makes a variable called M which will go to other pages based on input
        ECHO/
        ECHO --------------------------------------------------------------------
        ECHO Configure the timetable before use! Configure the timetable before use!
        ECHO --------------------------------------------------------------------
        ECHO/
        ECHO 1. Launch tableTimes
        ECHO 2. Set up tableTimes 
        ECHO 3. Reset tableTimes
        ECHO 4. Github page
        ECHO 5. 
        ECHO.
            REM Makes a input field that sets the variable M.
    SET /P M=Type your number of choice then press enter.
            REM Goes to label based on the input
        IF %M%==1 GOTO
        IF %M%==2 GOTO
        IF %M%==3 GOTO 
        IF %M%==4 GOTO 
        IF %M%==5 GOTO EXIT