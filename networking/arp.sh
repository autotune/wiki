# arp converts destination ip addresse to mac address on source server
# Address                  HWtype  HWaddress           Flags Mask            Iface

show_arp(){
    arp -ev
}


show_arp
