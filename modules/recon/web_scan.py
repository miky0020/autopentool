import subprocess

def run_nikto(target):
    print(f"    Running Nikto on {target}...")
    findings = []
    try:
        result = subprocess.run(
            ['nikto', '-h', f'http://{target}', '-nointeractive'],
            capture_output=True, text=True, timeout=120
        )
        for line in result.stdout.splitlines():
            if '+ ' in line:
                findings.append({
                    'target': target,
                    'module': 'nikto',
                    'finding': line.strip()
                })
    except Exception as e:
        print(f"    [!] Nikto error: {e}")
    print(f"    Found {len(findings)} web issues.")
    return findings
