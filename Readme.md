# StudyBud

**StudyBud** is a web application designed to facilitate collaborative study sessions. Users can create and join study rooms, discuss topics, and exchange messages.

## Description

StudyBud allows users to:
- Create and manage study rooms
- Join existing study rooms
- Participate in discussions within rooms
- Send and receive messages

## Installation

To set up StudyBud on your local machine, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sanjayleo35/Django.git
    cd Django
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment:**

    - On macOS/Linux:

        ```bash
        source env/bin/activate
        ```

    - On Windows:

        ```bash
        env\Scripts\activate
        ```

4. **Install the project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Your application will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

- **Creating a Room:**
  - Navigate to the room creation page.
  - Fill in the room details, including the topic and description.
  - Submit the form to create the room.

- **Joining a Room:**
  - Browse or search for existing rooms.
  - Join a room as a participant to start engaging in discussions.

- **Messaging:**
  - Once inside a room, send messages to communicate with other participants.

## Contributing

We welcome contributions to StudyBud! If you have suggestions or improvements, please follow these steps:

1. **Fork the repository**
2. **Create a new branch:**

    ```bash
    git checkout -b feature-branch
    ```

3. **Make your changes and commit:**

    ```bash
    git commit -am 'Add new feature'
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature-branch
    ```


## Acknowledgments

- Django framework for providing a robust foundation for web development.
- Any libraries or tools that helped in the development process.
