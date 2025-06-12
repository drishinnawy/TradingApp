@echo off
echo بدء رفع مشروعك إلى GitHub...

:: الانتقال إلى مجلد المشروع
cd /d C:\Users\Alnabegha\TradingApp

:: إنشاء ملف .gitignore
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

:: إنشاء ملف README.md
echo # TradingApp 📈 > README.md
echo. >> README.md
echo تطبيق حاسبة تداول بسيط مبني باستخدام Python و Kivy، يتيح للمستخدمين حساب الأرباح والخسائر في الأسهم بطريقة سهلة وسريعة. >> README.md
echo. >> README.md
echo ## 🚀 الميزات >> README.md
echo - إدخال رأس المال وسعر الشراء والبيع وعدد الأسهم >> README.md
echo - حساب الربح/الخسارة بدقة >> README.md
echo - واجهة رسومية باستخدام Kivy >> README.md
echo - جاهز للبناء على Android باستخدام Buildozer >> README.md
echo. >> README.md
echo ## 🛠️ المتطلبات >> README.md
echo - Python 3.10 >> README.md
echo - Kivy >> README.md
echo - Buildozer (لإنشاء ملف APK) >> README.md
echo. >> README.md
echo ## 📦 طريقة البناء (Android) >> README.md
echo ^^^ >> README.md
echo buildozer android debug >> README.md
echo ^^^ >> README.md
echo. >> README.md
echo بعد انتهاء البناء، ستجد ملف APK في مجلد bin/. >> README.md
echo. >> README.md
echo ## 🧾 ملاحظات >> README.md
echo - تم تضمين خط Cairo لدعم اللغة العربية. >> README.md
echo - التطبيق يدعم الواجهة من اليمين لليسار (RTL). >> README.md
echo - مناسب للمستثمرين في السوق السعودي أو غيره. >> README.md
echo. >> README.md
echo ## 📲 الحالة الحالية >> README.md
echo ✅ جاهز للتجريب >> README.md
echo 📦 جاري اختبار نسخة APK على GitHub Actions >> README.md

:: تهيئة Git ودفع الملفات
git init
git remote remove origin 2>nul
git remote add origin https://github.com/drishinnawy/TradingApp.git
git add .
git commit -m "رفع ملفات المشروع مع .gitignore و README"
git branch -M main
git push -u origin main --force

echo -------------------------------------------
echo ✅ تم رفع كل الملفات إلى GitHub بنجاح!
echo افتح الرابط: https://github.com/drishinnawy/TradingApp/actions لتحميل APK بعد البناء.
pause
