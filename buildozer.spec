[app]
title = أفضل حاسبة تداول
package.name = tradingapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,ttf,otf,png,jpg,json
source.include_patterns = *.ttf, *.otf, *.jpg, *.png, *.json
source.exclude_patterns = **/tests/*, **/test_*, **/lib2to3/tests/*
version = 1.0

# ضع اسم الأيقونة هنا إذا كان لديك أيقونة (إلا فاحذف السطر أو تجاهله)
icon.filename = %(source.dir)s/icon.png

# المتطلبات الأساسية لمشروعك
requirements = python3,kivy,kivymd,arabic_reshaper,python-bidi

# صلاحيات التطبيق
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# إصدارات وأدوات الأندرويد
android.minapi = 21
android.api = 31
android.ndk = 25b
android.ndk_path = /home/lnabegha/android-ndk-r25b
android.archs = arm64-v8a

# مكتبات جريدل إضافية (يمكنك حذفها إذا لم تكن بحاجة لها)
android.gradle_dependencies = androidx.appcompat:appcompat:1.4.1

android.debug = 1
