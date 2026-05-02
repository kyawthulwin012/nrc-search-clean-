[app]
title = NRC Search App
package.name = nrcsearch
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xlsx

version = 1.0

requirements = python3,kivy,pandas,openpyxl

orientation = portrait

android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
