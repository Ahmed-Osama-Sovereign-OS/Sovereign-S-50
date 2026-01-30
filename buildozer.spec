[app]
title = Sovereign S1100
package.name = sovereign.monster.s1100
package.domain = org.ahmed.osama
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1100.0.0

requirements = python3,kivy,kivymd,psutil,numpy,requests,certifi
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, ACCESS_FINE_LOCATION, QUERY_ALL_PACKAGES, PACKAGE_USAGE_STATS, CAMERA, RECORD_AUDIO, BLUETOOTH_ADMIN

android.archs = arm64-v8a
android.api = 33
android.minapi = 21
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
