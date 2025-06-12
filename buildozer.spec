[app]

title = أفضل حاسبة تداول
package.name = tradingapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,ttf,otf,png,jpg,json
source.include_patterns = Cairo-Regular.ttf

version = 1.0

requirements = python3,kivy==2.1.0,kivymd,requests,matplotlib,kivy_garden.matplotlib,numpy,cython==0.29.36

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.minapi = 21
android.api = 31
android.ndk = 25b
android.archs = arm64-v8a

android.debug = 1