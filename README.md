# Movie Recommendation System

## Description
This project is a movie recommendation system built using Python and Streamlit. It uses machine learning techniques to suggest movies based on user input, employing natural language processing and cosine similarity to find similar movies.

## Features
- User-friendly web interface
- Movie recommendations based on user input
- Information about the project and its creator
- Easy navigation between home and recommendation pages

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Steps

1. Clone the repository:
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

3. Install the required packages:

4. Ensure you have the following files in your project directory:
- `app.py`: The main Streamlit application
- `movie_recommender.sav`: The saved model file
- `movies.csv`: The dataset containing movie information

## Usage

1. Run the Streamlit app:

2. Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).

3. Navigate through the app:
- Home page: Learn about the project and its creator
- Get Recommendations: Enter a movie name and receive recommendations

## Project Structure

movie-recommendation-system/
│
├── app.py # Main Streamlit application
├── movie_recommender.sav # Saved model file
├── movies.csv # Dataset with movie information
├── requirements.txt # List of Python dependencies
└── README.md # Project documentation

## Customization

To personalize the app:
1. Open `app.py` in a text editor.
2. Locate the `home_page()` function.
3. Update the "About Me" section with your information.

## Troubleshooting

- If you encounter a `FileNotFoundError`, ensure that `movie_recommender.sav` is in the same directory as `app.py`.
- For any import errors, verify that all required packages are installed by running `pip install -r requirements.txt`.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` file for more information.

## Contact

Your Name - ksujivarma2003@gmail.com

Project Link: [ https://github.com/Sujit-2003/Movie-Recommendation-System-using-Machine-Learning-with-Python-](https://github.com/Sujit-2003/Movie-Recommendation-System-using-Machine-Learning-with-Python-)