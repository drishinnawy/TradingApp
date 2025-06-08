
[app]

title = StockTradingApp
package.name = stockapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 0.1
requirements = python3,kivy,arabic_reshaper,python-bidi
orientation = portrait

fullscreen = 1

# إدراج الخطوط
android.allow_backup = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.bootstrap = sdl2
android.ndk_api = 21
copy_libs = 1
