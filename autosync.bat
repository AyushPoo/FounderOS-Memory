cd /d F:\Work\FounderOS

git add .

git diff --cached --quiet
IF %ERRORLEVEL%==0 (
    echo No changes to commit
) ELSE (
    git commit -m "vault auto update %date% %time%"
    git push origin main
)