[app]

title = أفضل حاسبة تداول
package.name = tradingapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,ttf,otf,png,jpg,json
source.include_patterns = *.ttf, *.otf, *.jpg, *.png, *.json

version = 1.0

requirements = kivy==2.1.0,kivymd,requests,matplotlib,kivy_garden.matplotlib,cython==0.29.36,pillow

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.minapi = 21
android.api = 31
android.ndk = 25b
android.archs = arm64-v8a

android.gradle_dependencies = com.android.support:support-v4:28.0.0

android.debug = 1
