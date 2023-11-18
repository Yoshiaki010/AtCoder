@echo off
setlocal
echo START
set num=0
set h=
echo %h%
goto first

:first
echo NOW NUM:%num%
if %num%==0 (
  goto end
) else (
  goto serch
)
:serch
echo GET FILENAME
set f=%CD%
echo FILENAME=%f%
goto change

:change
echo RENAME
goto move

:move
echo MOVE TO %1
set /a num=num-1
goto first

:end
echo END