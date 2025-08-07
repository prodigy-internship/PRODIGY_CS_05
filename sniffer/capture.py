from scapy.all import sniff
from sniffer.handler import get_protocol_info
from sniffer.display import display_packet
from sniffer.utils import log_packet

def start_capture(interface, filter_exp, count):
    """Start packet capture and handle each packet."""

    print(f"[*] Starting capture on {interface} with filter: '{filter_exp}'")
    print("[*] Press CTRL-C to stop capture\n")

    def packet_handler(pkt):
        try:
            info = get_protocol_info(pkt)
            display_packet(info)
            log_packet(info)  # 👈 Logs each packet to file
        except Exception as e:
            print(f"[!] Error processing packet: {str(e)}")

    try:
        sniff(
            iface=interface,
            prn=packet_handler,
            filter=filter_exp,
            store=False,
            count=count
        )
    except Exception as e:
        print(f"[!] Capture error: {str(e)}")
