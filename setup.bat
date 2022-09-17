if exist build rd /q /s build
call gradlew eclipse --no-daemon
call gradlew genEclipseRuns --no-daemon
for %%I in (.) do set PROJNAME=%%~nxI
del %PROJNAME%-Client.launch
del %PROJNAME%-Server.launch
del %PROJNAME%-Data.launch
ren runClient.launch %PROJNAME%-Client.launch
ren runServer.launch %PROJNAME%-Server.launch
ren runData.launch %PROJNAME%-Data.launch
call gradlew processResources --no-daemon