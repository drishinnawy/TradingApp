#!/bin/bash

# التأكد من أن Buildozer وPython 3 مثبتان
echo "🔧 التأكد من تثبيت المتطلبات..."
sudo apt update
sudo apt install -y python3 python3-pip unzip git zip openjdk-17-jdk
pip3 install --upgrade pip
pip3 install buildozer cython

# تفعيل Buildozer
echo "⚙️ بدء بناء ملف APK..."
buildozer android debug

# التحقق من نجاح البناء
if [ -f "bin/*.apk" ]; then
    echo "✅ تم بناء ملف APK بنجاح!"
    ls -lh bin/*.apk
else
    echo "❌ فشل في بناء ملف APK. تحقق من الأخطاء في المخرجات."
fi
