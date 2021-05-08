@echo off
taskkill /f /t /im TPS.exe
start /d "D:\app\map_matching\map_city_matching\bus_map_matching" TPS.exe /online 
exit
