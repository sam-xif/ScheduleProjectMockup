@echo off

rem A script to run the server with Visual Studio's configuration

set DJANGO_EXECUTABLE_NAME=manage.py
set PYTHON_BIN=env\Scripts
set INTERPRETER=python

rem Temporary set PATH
set PATH_STORE=%PATH%
set PATH=%CD%\%PYTHON_BIN%;%PATH%

echo %CD%

if "%1"=="run" (
	echo Running %DJANGO_EXECUTABLE_NAME%...
	%INTERPRETER% %DJANGO_EXECUTABLE_NAME% runserver
)

if "%1"=="shell" (
	echo Starting shell...
	cmd
)

if "%1"=="help" (
	echo Use the option "run" to run the server
	echo Use the option "shell" to start a shell from which to configure the server
)

rem Restore PATH
set PATH=%PATH_STORE%