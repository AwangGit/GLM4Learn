@echo off

setlocal
set LOCAL_REPO=D:\Project\Shared_packages
set REQUIREMENTS_FILE=requirements.txt

:: 确保本地仓库中有所有依赖项
pip download -d %LOCAL_REPO% -r %REQUIREMENTS_FILE%

:: 从本地仓库安装依赖项
pip install --no-index --find-links=file:///D:/Project/Shared_packages -r %REQUIREMENTS_FILE%

endlocal
pause
