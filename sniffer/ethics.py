import sys

ETHICAL_WARNING = """
╔═════════════════════════════════════════════════════════════════════════════╗
║                    ETHICAL PACKET SNIFFER - KALI LINUX                      ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ WARNING: This tool is for educational purposes only.                        ║
║                                                                             ║
║ LEGAL REQUIREMENTS:                                                         ║
║  • You MUST have explicit permission to monitor the network                 ║
║  • You MUST only analyze networks you own/administrate                      ║
║  • You MUST NOT capture traffic on public/unauthorized networks             ║
║  • You MUST NOT capture sensitive personal information                      ║
║                                                                             ║
║ By continuing, you accept full responsibility for your actions.             ║
╚═════════════════════════════════════════════════════════════════════════════╝
"""

def print_ethical_warning():
    print(ETHICAL_WARNING)
    response = input("Do you understand and accept these terms? (yes/no): ")
    if response.lower() != 'yes':
        print("[!] You must accept the terms to use this tool.")
        sys.exit(0)
    print()
