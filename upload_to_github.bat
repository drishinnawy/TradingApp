@echo off
echo بدء رفع مشروعك إلى GitHub...

:: تغيير المسار إلى مجلد المشروع
cd /d C:\Users\Alnabegha\TradingApp

:: إنشاء ملف .gitignore تلقائياً
echo # Buildozer > .gitignore
echo .buildozer/ >> .gitignore
echo bin/ >> .gitignore
echo *.apk >> .gitignore
echo. >> .gitignore
echo # Python >> .gitignore
echo __pycache__/ >> .gitignore
echo *.pyc >> .gitignore
echo *.pyo >> .gitignore
echo *.pyd >> .gitignore
echo *.log >> .gitignore
echo. >> .gitignore
echo # Backup files >> .gitignore
echo *.bak >> .gitignore
echo *.swp >> .gitignore
echo *.swo >> .gitignore
echo *.tmp >> .gitignore
echo. >> .gitignore
echo # macOS >> .gitignore
echo .DS_Store >> .gitignore
echo. >> .gitignore
echo # Windows >> .gitignore
echo Thumbs.db >> .gitignore
echo ehthumbs.db >> .gitignore
echo Desktop.ini >> .gitignore

:: تهيئة git وربطه بالمستودع
git init
git remote remove origin 2>nul
git remote add origin https://github.com/drishinnawy/TradingApp.git

:: إضافة الملفات
git add .

:: عمل commit
git commit -m "رفع ملفات المشروع مع .gitignore"

:: إعادة تسمية الفرع إلى main ودفعه
git branch -M main
git push -u origin main --force

echo -------------------------------------------
echo ✅ تم رفع الملفات بنجاح إلى GitHub!
echo افتح الرابط: https://github.com/drishinnawy/TradingApp/actions لمتابعة بناء APK
pause
