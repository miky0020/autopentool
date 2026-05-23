import argparse
from orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(
        description='AutoPenTool — Automated Penetration Testing Framework'
    )
    parser.add_argument('--target', required=True, help='Target IP or domain')
    parser.add_argument('--scan', choices=['recon', 'web', 'full'], default='recon', help='Scan type')
    parser.add_argument('--output', choices=['pdf', 'json'], default='pdf', help='Output format')
    args = parser.parse_args()

    print(f"\n[*] AutoPenTool Starting...")
    print(f"[*] Target  : {args.target}")
    print(f"[*] Scan    : {args.scan}")
    print(f"[*] Output  : {args.output}\n")

    o = Orchestrator(args.target, args.scan, args.output)
    o.run()

if __name__ == '__main__':
    main()
