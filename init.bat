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
        ECHO
        ECHO
        ECHO 
        ECHO  
        ECHO 
        ECHO.
            REM Makes a input field that sets the variable M.
    SET /P M=Type your number of choice then press enter.
            REM Goes to label based on the input
        IF %M%==1 GOTO launchrequirements
        IF %M%==2 GOTO configbot
        IF %M%==3 GOTO resetbot
        IF %M%==4 GOTO about
        IF %M%==5 GOTO EXIT