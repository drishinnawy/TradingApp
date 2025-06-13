[app]
title = أفضل حاسبة تداول
package.name = tradingapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,ttf,otf,png,jpg,json
source.include_patterns = *.ttf, *.otf, *.jpg, *.png, *.json

version = 1.0

requirements = python3,kivy,requests

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.minapi = 21
android.api = 31
android.ndk = 27
android.archs = arm64-v8a

android.gradle_dependencies = androidx.appcompat:appcompat:1.4.1

android.debug = 1
android.entrypoint = org.kivy.android.PythonActivity
