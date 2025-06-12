#!/bin/bash

# تثبيت cmake المطلوب لإنشاء ملف APK
sudo apt update
sudo apt install -y cmake

# تفعيل البيئة الافتراضية
source venv/bin/activate

# تنفيذ أمر buildozer لإنشاء ملف APK
buildozer -v android debug
