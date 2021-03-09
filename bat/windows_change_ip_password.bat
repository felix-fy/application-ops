net user administrator %1
netsh interface ip set address name="Ethernet0" static %2 255.255.255.0 10.3.4.254 1
