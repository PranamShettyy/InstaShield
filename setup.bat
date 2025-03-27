
pip install mitmproxy
pip install nudenet 
pip install flask 
msg * "please read carefully."
cls
echo 'we are instaling a ssl certificate on your system'
@echo off
set /p choice=Do you want to continue? (Y/N): 

if /i "%choice%"=="Y" (
    echo You chose to continue.
    certutil.exe -addstore root mitmproxy-ca-cert.cer
) else if /i "%choice%"=="N" (
    echo You chose to exit.
    exit /b
) else (
    echo Invalid choice. Please enter Y or N.
    pause
    goto :start
)

python hacka.py