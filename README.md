# GUI Password Generator

![Password Generator](assets/password-generator-3.webp)

A secure and user-friendly password generator application built with Python and Streamlit, offering multiple password generation options.

## Table of Contents
- [Project Description](#project-description)
- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Project Description
This GUI Password Generator is a web-based application that allows users to generate different types of passwords based on their needs. It supports random passwords with customizable character sets, memorable passwords using dictionary words, and numeric PINs.

## Project Structure
```
GUI-Password-Generator/
├── assets/
│   └── password-generator-3.webp
├── data/
│   └── eff_large_wordlist.txt
├── src/
│   ├── main.py
│   └── password_generator.py
├── requirements.txt
└── README.md
```

## Features
- Three password generation modes:
  - **Random Password**: Customizable length and character sets (uppercase, numbers, symbols)
  - **Memorable Password**: Word-based passwords using EFF's large wordlist
  - **PIN**: Numeric PIN codes of configurable length
- User-friendly web interface
- Copy to clipboard functionality
- Password strength indication
- Adjustable password parameters

## Requirements
The project requires Python 3.7+ and the following packages:
```
streamlit==1.48.1
```


## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/GUI-Password-Generator.git
cd GUI-Password-Generator
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the application:
```bash
streamlit run src/main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Select the desired password type:
   - Random: Choose length and character types
   - Memorable: Select number of words and capitalization
   - PIN: Choose PIN length

4. Click "Generate Password" to create a new password

## Contributing
Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Author
### Mohammadreza Naseri
- GitHub: [@themohammadreza](https://github.com/themohammadreza)
- Email: [@Contact-Me](themohammadreza2006@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.