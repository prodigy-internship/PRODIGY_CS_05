from colorama import init, Fore, Style

# Initialize colorama (for Windows terminal compatibility)
init(autoreset=True)

def display_packet(info):
    protocol = info['protocol'].upper()

    # Assign color per protocol
    color = {
        "DNS": Fore.BLUE,
        "HTTP": Fore.GREEN,
        "TCP": Fore.CYAN,
        "ICMP": Fore.MAGENTA,
        "ARP": Fore.YELLOW,
        "TLS": Fore.RED,
        "SSH": Fore.LIGHTBLUE_EX,
        "UDP": Fore.LIGHTMAGENTA_EX,
        "DHCP": Fore.LIGHTCYAN_EX,
        "WIFI": Fore.LIGHTYELLOW_EX
    }.get(protocol, Fore.WHITE)

    # Display packet with color
    print(f"{info['timestamp']} {color}{protocol.ljust(6)}{Style.RESET_ALL} ", end='')
    print(f"{info.get('src_mac', ''):17} → {info.get('dst_mac', ''):17}")
    print(f"    {info.get('src', ''):15} → {info.get('dst', ''):15} {info['info']}")
    print("-" * 80)
