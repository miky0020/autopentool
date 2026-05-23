from db.database import init_db, save_finding
from modules.recon.nmap_scan import run_nmap
from modules.recon.subdomain_enum import run_subdomain
from modules.recon.web_scan import run_nikto
from modules.scoring import score_finding

class Orchestrator:
    def __init__(self, target, scan_type, output_format):
        self.target = target
        self.scan_type = scan_type
        self.output_format = output_format
        self.results = []
        init_db()

    def run(self):
        print("[*] Starting scan pipeline...\n")

        if self.scan_type in ['recon', 'full']:
            print("[+] Running Nmap...")
            self.results += run_nmap(self.target)

            print("[+] Running subdomain enumeration...")
            self.results += run_subdomain(self.target)

        if self.scan_type in ['web', 'full']:
            print("[+] Running Nikto web scan...")
            self.results += run_nikto(self.target)

        for r in self.results:
            r['severity'] = score_finding(r['finding'])
            save_finding(r)

        print(f"\n[*] Scan complete. {len(self.results)} findings saved.")

        if self.output_format == 'pdf':
            from report.report_gen import generate_pdf
            generate_pdf(self.results, self.target, 'report/output.pdf')
            print("[*] PDF report saved to report/output.pdf")
