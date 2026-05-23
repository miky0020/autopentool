import subprocess

def run_nmap(target):
    print(f"    Scanning {target} with Nmap...")
    findings = []
    try:
        result = subprocess.run(
            ['nmap', '-sV', '-O', '--open', '-T4', target],
            capture_output=True, text=True, timeout=120
        )
        for line in result.stdout.splitlines():
            if '/tcp' in line or '/udp' in line:
                findings.append({
                    'target': target,
                    'module': 'nmap',
                    'finding': line.strip()
                })
    except Exception as e:
        print(f"    [!] Nmap error: {e}")
    print(f"    Found {len(findings)} open ports.")
    return findings
