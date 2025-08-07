#!/usr/bin/env python3

import argparse
import signal
import sys
import os

from sniffer.capture import start_capture
from sniffer.ethics import print_ethical_warning

def signal_handler(sig, frame):
    print("\n[!] Capture stopped by user.")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)

    # Display ethical warning and prompt
    print_ethical_warning()

    # Root check
    if os.geteuid() != 0:
        print("[!] Requires root privileges. Run with sudo.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Comprehensive Network Protocol Analyzer")
    parser.add_argument("-i", "--interface", help="Network interface")
    parser.add_argument("-f", "--filter", default="", help="BPF filter (e.g., 'tcp', 'port 80')")
    parser.add_argument("-c", "--count", type=int, default=0, help="Packet count (0 = unlimited)")

    args = parser.parse_args()

    if not args.interface:
        from scapy.all import get_if_list
        print("[*] Available interfaces:")
        for iface in get_if_list():
            print(f"  - {iface}")
        args.interface = input("[?] Select interface: ")

    start_capture(args.interface, args.filter, args.count)

if __name__ == "__main__":
    main()
