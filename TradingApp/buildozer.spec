[app]

title = أفضل حاسبة تداول
package.name = tradingapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,ttf,otf,png,jpg,json
source.include_patterns = Cairo-Regular.ttf

version = 1.0

requirements = python3,kivy==2.1.0,kivymd,requests,matplotlib,kivy_garden.matplotlib,android,cython

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a, arm64-v8a

android.debug = 1
