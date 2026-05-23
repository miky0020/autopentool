import subprocess

def run_subdomain(domain):
    print(f"    Enumerating subdomains for {domain}...")
    findings = []
    try:
        result = subprocess.run(
            ['theHarvester', '-d', domain, '-b', 'bing', '-l', '50'],
            capture_output=True, text=True, timeout=60
        )
        for line in result.stdout.splitlines():
            if '.' in line and domain in line:
                findings.append({
                    'target': domain,
                    'module': 'subdomain_enum',
                    'finding': f'Subdomain: {line.strip()}'
                })
    except Exception as e:
        print(f"    [!] Subdomain enum error: {e}")
    print(f"    Found {len(findings)} subdomains.")
    return findings
