# AutoPenTool

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Automated Penetration Testing Framework built with Python, Docker, and Kali Linux.

## Features
- Nmap port and service discovery
- Subdomain enumeration (theHarvester, Amass)
- Web scanning with Nikto
- Metasploit RPC integration
- SQLMap automation
- Risk scoring engine
- CVE lookup via NVD API
- PDF report generation
- Optional Flask web dashboard

## Requirements
- Kali Linux 2024.x
- Python 3.10+
- Docker and Docker Compose
- 4GB RAM minimum

## Installation

git clone https://github.com/youruser/autopentool.git
cd autopentool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker build -t autopentool-kali -f docker/Dockerfile.kali .

## Usage

python cli.py --target 192.168.1.1 --scan recon --output pdf
python cli.py --target 192.168.1.1 --scan full --output pdf
python cli.py --target 192.168.1.1 --scan web --output json

## Project Structure

autopentool/
├── cli.py
├── orchestrator.py
├── requirements.txt
├── modules/
│   ├── recon/
│   │   ├── nmap_scan.py
│   │   ├── subdomain_enum.py
│   │   └── web_scan.py
│   └── exploit/
│       ├── msf_rpc.py
│       └── sqlmap_runner.py
├── db/
├── report/
├── docker/
└── screenshots/

## Roadmap

- [x] Project structure and CLI
- [x] Nmap scanner module
- [x] Subdomain enumeration
- [x] Nikto web scanner
- [x] SQLite results database
- [x] PDF report generation
- [x] Metasploit RPC integration
- [ ] Telegram alert system
- [ ] REST API
- [ ] Shodan integration
- [ ] Multi-target batch scanning

## Disclaimer

This tool is for educational purposes and authorized security testing only.
Do NOT use against systems you do not own or have explicit permission to test.
The author takes no responsibility for misuse or damage caused by this tool.

## Author

Mikhaynu Marma
GitHub: https://github.com/miky0020
