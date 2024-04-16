# Honeypot and IP Logger System

This project consists of two main components: a `Honeypot web application` and an `IP Logger`, designed to enhance cybersecurity measures through simulation of vulnerabilities and logging web interactions on public networks.

[![Python][python-badge]][python-link]
[![Django][django-badge]][django-link]
[![Visual Studio Code][vscode-badge]][vscode-link]
[![Git][git-badge]][git-link]
[![JSON][json-badge]][json-link]

![Sample][Sample]

## Usage

To run the project execute the following command:

```powershell
pip install -r requirements.txt
```

Navigate to the project directory and execute the following command:

```powershell
python manage.py runserver main.py
```

## Feature of Honeypot
- `Simulated Vulnerabilities:` Emulates various network services to attract cyber attackers.
- `Data Collection:` Gathers insights on attack patterns and techniques.
- `Real-Time Interaction:` Monitors and logs activities in real-time using a Django-based interface.
- `Education and Training:` Serves as a practical educational tool for understanding cyber attacks.

## Feature of IP Logger
- `Traffic Logging:` Records detailed information about user interactions, including IP addresses, user agent strings, and more.
- `Geolocation Tracking:` Tracks the geographic location of web visitors.
- `Real-Time Alerts:` Sends notifications for specific trigger events such as repeated login failures.

## Getting Started
- Installation: Ensure OpenCannary is configured properly. Clone the repository from GitHub.
- Run `python manage.py migrate` to set up the database.
- Configuration: Use the Django admin panel to configure honeypot services and view logs.


## Team

  <a href = "https://github.com/amulifts"><img src = "https://avatars.githubusercontent.com/u/49828737?v=4" width="144"></a>
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

<!-- Badge links -->
[python-badge]: https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white
[django-badge]: https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white
[vscode-badge]: https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white
[git-badge]: https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white
[json-badge]: https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white

<!-- Link definitions -->
[python-link]: https://www.python.org
[django-link]: https://www.djangoproject.com
[vscode-link]: https://code.visualstudio.com/
[git-link]: https://git-scm.com/
[json-link]: https://www.json.org/json-en.html

[Sample]: ./sample/sample.gif
