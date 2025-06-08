@echo off
echo بدء رفع مشروعك إلى GitHub...

:: تغيير المسار إلى مجلد المشروع
cd /d C:\Users\Alnabegha\TradingApp

:: تهيئة المشروع كـ git repo (إن لم يكن مهيأً)
git init

:: ربط المستودع البعيد
git remote remove origin 2>nul
git remote add origin https://github.com/drishinnawy/TradingApp.git

:: إضافة جميع الملفات
git add .

:: عمل commit بالرسالة
git commit -m "رفع ملفات المشروع"

:: رفع الملفات إلى GitHub - الفرع الرئيسي
git branch -M main
git push -u origin main --force

echo -------------------------------------------
echo ✅ تم رفع الملفات بنجاح إلى GitHub!
echo افتح الرابط: https://github.com/drishinnawy/TradingApp/actions لمتابعة بناء APK
pause
