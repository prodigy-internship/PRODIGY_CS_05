from scapy.all import *
from datetime import datetime
from sniffer.utils import get_tcp_flags

def get_protocol_info(packet):
    info = {
        'timestamp': datetime.now().strftime("%H:%M:%S.%f")[:-3],
        'protocol': 'UNKNOWN',
        'src': '',
        'dst': '',
        'info': ''
    }

    if Ether in packet:
        info['src_mac'] = packet[Ether].src
        info['dst_mac'] = packet[Ether].dst

    if ARP in packet:
        info.update({
            'protocol': 'ARP',
            'src': packet[ARP].psrc,
            'dst': packet[ARP].pdst,
            'info': f"{'Request' if packet[ARP].op == 1 else 'Reply'} for {packet[ARP].pdst}"
        })
        return info

    if IP in packet:
        info['src'] = packet[IP].src
        info['dst'] = packet[IP].dst

        if TCP in packet:
            info.update({
                'protocol': 'TCP',
                'info': f"{packet[TCP].sport} → {packet[TCP].dport} {get_tcp_flags(packet[TCP])}"
            })

            if packet[TCP].sport in [80, 443] or packet[TCP].dport in [80, 443]:
                if Raw in packet:
                    try:
                        http_data = packet[Raw].load.decode('utf-8', 'ignore')
                        if "HTTP" in http_data:
                            info['protocol'] = 'HTTP'
                            info['info'] = http_data.splitlines()[0]
                    except:
                        pass
                if packet[TCP].dport == 443:
                    info['protocol'] = 'TLS'
                    info['info'] = "Encrypted HTTPS Session"

            elif packet[TCP].dport == 22 or packet[TCP].sport == 22:
                info['protocol'] = 'SSH'
                info['info'] = "SSH Session"

            elif packet[TCP].dport == 53 or packet[TCP].sport == 53:
                info['protocol'] = 'DNS'
                info['info'] = "DNS Query (TCP)"

        elif UDP in packet:
            info.update({
                'protocol': 'UDP',
                'info': f"{packet[UDP].sport} → {packet[UDP].dport}"
            })

            if DNS in packet:
                try:
                    qname = packet[DNS].qd.qname.decode()
                    info['protocol'] = 'DNS'
                    info['info'] = f"Query: {qname}"
                except:
                    pass

            elif packet[UDP].dport in [67, 68]:
                info['protocol'] = 'DHCP'
                info['info'] = "DHCP Message"

        elif ICMP in packet:
            info.update({
                'protocol': 'ICMP',
                'info': f"Type: {packet[ICMP].type} Code: {packet[ICMP].code}"
            })

        elif IGMP in packet:
            info.update({
                'protocol': 'IGMP',
                'info': f"Type: {packet[IGMP].type}"
            })

    elif Dot11 in packet:
        info.update({
            'protocol': 'WiFi',
            'info': f"Type: {packet[Dot11].type} Subtype: {packet[Dot11].subtype}"
        })

    return info
