
For /F "tokens=1* delims==" %%A IN (gradle.properties) DO (
    IF "%%A"=="modid" set modid=%%B
)

cd src\main\resources
ren modid.mixins.json %modid%.mixins.json
cd data
ren modid %modid%
cd ../assets
ren modid %modid%
cd ../../../..