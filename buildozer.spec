[app]
title = أفضل حاسبة تداول
package.name = tradingapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,ttf,otf,png,jpg,json
source.include_patterns = *.ttf, *.otf, *.jpg, *.png, *.json
version = 1.0

icon.filename = %(source.dir)s/icon.png

requirements = python3,kivy,requests

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.minapi = 21
android.api = 31
android.ndk = 25b
android.ndk_path = /home/lnabegha/android-ndk-r25b
android.archs = arm64-v8a

android.gradle_dependencies = androidx.appcompat:appcompat:1.4.1

android.debug = 1
