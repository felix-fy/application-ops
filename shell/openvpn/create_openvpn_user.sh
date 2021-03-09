#!/bin/bash
rsa_path="/root/openvpn-ca"
cd ${rsa_path}
source vars 
for iname in `cat /root/shell/openvpn_user.txt`;do
/usr/bin/expect << EOF
spawn bash build-key-pass --batch client_${iname}
set timeout 9
expect {
         -timeout 8
         "Enter PEM pass phrase"  { send ${iname}\r;exp_continue }
         "Verifying - Enter PEM pass phrase"  { send ${iname}\r;exp_continue }
}
expect eof
EOF
mkdir -p /root/openvpn_crt/${iname}
cp ${rsa_path}/keys/ca.crt /root/openvpn_crt/${iname}/ca_szw.crt
cp ${rsa_path}/keys/ta.key /root/openvpn_crt/${iname}/ta_szw.key
cp ${rsa_path}/keys/client_${iname}.crt /root/openvpn_crt/${iname}/
cp ${rsa_path}/keys/client_${iname}.key /root/openvpn_crt/${iname}/
cp ${rsa_path}/sutpc_szw.ovpn /root/openvpn_crt/${iname}/
sed -i "s/first/${iname}/g" /root/openvpn_crt/${iname}/sutpc_szw.ovpn
done
