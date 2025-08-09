**Slipher** is an educational YouTube filter designed to save students the time weast searching youtube but not getting what they wanted and from youtube rabit whole.

## Current Status

- The core idea and project structure have been established.
- Initial research on YouTube APIs and filtering techniques is complete.
- Basic UI/UX wireframes have been drafted.
- Early prototype for video search and filtering is in progress.

## Accomplishments

- Set up the project repository and development environment.
- Defined the main features and user stories.
- Integrated basic YouTube video search functionality.
- Implemented preliminary filtering logic to improve search relevance.

## Next Steps

- Enhance filtering algorithms for better educational content discovery.
- Develop a user-friendly interface.
- Add user authentication and personalization features.
- Conduct user testing and gather feedback.
- Prepare for initial release and documentation.

## Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Django
- **Database:** PostgreSQL
- **APIs:** YouTube Data API v3
- **Styling:** Custom CSS

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/slipher.git
    cd slipher
    ```

2. **Set up a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Configure database and API keys:**
    - Update your database settings and YouTube API key directly in the Django `settings.py` file.

4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the app:**
    - Open [http://127.0.0.1:8000](http://localhost:8000) in your browser.

