import os

LOG_FILE = "logs/packet_log.txt"
LOG_HEADER = (
    "Timestamp         | Protocol | Source IP         → Destination IP    | Info\n"
    + "-" * 80 + "\n"
)

def get_tcp_flags(tcp):
    flags = []
    if tcp.flags & 0x01: flags.append("FIN")
    if tcp.flags & 0x02: flags.append("SYN")
    if tcp.flags & 0x04: flags.append("RST")
    if tcp.flags & 0x08: flags.append("PSH")
    if tcp.flags & 0x10: flags.append("ACK")
    if tcp.flags & 0x20: flags.append("URG")
    if tcp.flags & 0x40: flags.append("ECE")
    if tcp.flags & 0x80: flags.append("CWR")
    return f"[{' '.join(flags)}]" if flags else ""

def log_packet(info, logfile=LOG_FILE):
    """Append formatted packet info to log file with headers and labels."""
    try:
        os.makedirs("logs", exist_ok=True)

        # Add header if file is empty or doesn't exist
        if not os.path.exists(logfile) or os.path.getsize(logfile) == 0:
            with open(logfile, "w") as f:
                f.write(LOG_HEADER)

        # Append formatted log line
        with open(logfile, "a") as f:
            line = (
                f"{info['timestamp']:18} | {info['protocol']:<8} | "
                f"{info.get('src', ''):<17} → {info.get('dst', ''):<17} | "
                f"{info['info']}\n"
            )
            f.write(line)

    except Exception as e:
        print(f"[!] Failed to write to log: {e}")
