@echo off
title Push to GitHub - Pranav Sutar 3D Portfolio
echo ========================================================
echo   Pushing Pranav Sutar 3D Portfolio to branch portfolio-3d
echo   Repository: https://github.com/pranavsutar/pranavsutar.git
echo   Branch:     portfolio-3d
echo ========================================================
echo.

:: 1. Ensure remote URL is set to Pranav's repository
echo [1/4] Ensuring remote origin is set to pranavsutar.git...
git remote set-url origin https://github.com/pranavsutar/pranavsutar.git

:: 2. Ensure on portfolio-3d branch
echo [2/4] Ensuring on branch portfolio-3d...
git checkout -B portfolio-3d

:: 3. Stage all files
echo [3/4] Staging files...
git add -A

:: 4. Commit
git commit -m "feat: customize 3D portfolio for Pranav Sutar with Cyber Jade & Obsidian Emerald palette"

:: 5. Push to GitHub
echo.
echo [4/4] Pushing to GitHub on branch 'portfolio-3d'...
git push -u origin portfolio-3d

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo   SUCCESS! Pushed to GitHub on branch 'portfolio-3d'.
    echo.
    echo   Repository link:
    echo   https://github.com/pranavsutar/pranavsutar/tree/portfolio-3d
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo   Push encountered an error. Please check your credentials or network.
    echo ========================================================
)
