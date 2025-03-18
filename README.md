# StaticBuilder

StaticBuilder is my personal Python project that helps me generate a static webpage for my GitHub Pages accounts. The project processes a collection of JSON and Markdown files, which contain raw data about your website, and outputs a fully functional static webpage ready for deployment. This generator uses HTML, JavaScript, and Tailwind CSS for styling and layout.

The generated webpage includes:
- A **Hero Main Page**
- An **About Me** Page
- A **Blog Search** feature
- A **Blog Page** for easy management and display of blog content
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IliyaBadri/StaticBuilder.git
   cd StaticBuilder
   ```

2. Install the required dependencies (which is only markdown):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate the static webpage, simply run the `main.py` script. This will generate a website according to the configuration inside the `/media` directory.

```bash
python3 main.py
```

This will generate the static page and serve a test server on your machine.

The output is stored inside the `/static` directory.

## Contributing

If you'd like to contribute to StaticBuilder, feel free to open issues or pull requests. This is an open-source project, and contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Tailwind CSS**: A utility-first CSS framework used for styling.
- **GitHub Pages**: Free hosting platform for the static website.
