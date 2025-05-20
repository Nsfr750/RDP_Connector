# RDP Connector

A modern, user-friendly RDP connection manager for Windows and Linux systems.

## Features

- 🌐 Connect to Windows RDP sessions from Linux or Windows
- 🔐 Secure password handling with show/hide option
- 📝 Connection history tracking
- 📊 Modern ttk-based GUI with improved styling
- 📋 Save and load connection configurations
- 📚 Comprehensive error handling and status feedback
- 📱 Support for multiple RDP connection methods

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- xfreerdp (for Linux RDP connections)

### Windows Requirements

- Python 3.x
- tkinter (usually included with Python)
- Windows Remote Desktop Protocol (built-in)

### Linux Requirements

- Python 3.x
- tkinter (usually included with Python)
- xfreerdp (for RDP connections)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Nsfr750/RDP_Connector.git
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Windows

1. Ensure Python 3.x is installed
2. Run the application:
```bash
python rdp.py
```

### Linux

1. Install xfreerdp:
```bash
sudo apt-get install xfreerdp
```

2. Run the application:
```bash
python3 rdp.py
```

## Configuration

The application uses a configuration file (`rdp_config.json`) to store:
- Connection history
- Saved connections
- User preferences

## Support

- [GitHub](https://github.com/Nsfr750/RDP_Connector)
- [Patreon](https://www.patreon.com/Nsfr750)
- [Discord](https://discord.gg/q5Pcgrju)
- [Buy Me a Coffee](https://paypal.me/3dmega)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the FreeRDP project for their excellent RDP implementation
- Special thanks to the Python community for their fantastic libraries and tools