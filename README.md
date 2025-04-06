# 📚 ReadHub API

ReadHub is a RESTful API for a **book management system**, allowing users to register, log in, manage books, create reading lists, organize books within those lists, and more.

---

## 🚀 Tech Stack

- **Backend**: Django, Django REST Framework  
- **Authentication**: JWT (Simple JWT)  
- **Database**: PostgreSQL  
- **Testing**: Pytest  
- **API Style**: RESTful  
---

## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/Sidharth-Chirathazha/ReadHub-API.git

2. Create a virtual environment

python -m venv env
source env/bin/activate  # For Linux/macOS
# OR
env\Scripts\activate     # For Windows

3. Install dependencies

pip install -r requirements.txt

4. Set up environment variables
Create a .env file in the project root and add the following:

SECRET_KEY=Your Django Secret Key
DEBUG=True(For development)/False(For Production)
DATABASE_URL=postgres://{DB_USERNAME}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}

5. Run migrations

cd readhub
python manage.py migrate

6. Start the development server

python manage.py runserver


🔑 Authentication
This project uses JWT (JSON Web Tokens) for secure user authentication.

Access tokens are required for most API endpoints.

Use the /api/auth/login/ endpoint to get access and refresh tokens.


📮 API Endpoints

🧍 User Authentication
Method	Endpoint	Description
POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Log in user and return JWT tokens
POST	/api/auth/logout/	Log out user (requires refresh token)
POST	/api/auth/token/refresh/	Refresh access token using refresh token
PATCH	/api/auth/update-profile/	Update user profile (username, firstname, lastname)

Example Register Request:
{
  "username": "user25",
  "email": "user@xyz.com",
  "password": "user123",
  "confirm_password": "user123"
}


📚 Book Management
Method	Endpoint	Description
POST	/api/book/books/	Create a book
GET	/api/book/books/	Get all books
GET	/api/book/books/{bookId}/	Get details of a single book
DELETE	/api/book/books/{bookId}/	Delete a book
PATCH	/api/book/books/{bookId}/	Update a book

Example Create Book Request:
{
  "title": "Harry Potter",
  "authors": [{"name": "JK Rowling"}],
  "genre": "Novel series",
  "publication_date": "1999-06-10",
  "description": "Sample description."
}


📝 Reading List Management
Method	Endpoint	Description
POST	/api/reading-list/reading-lists/	Create a reading list
GET	/api/reading-list/reading-lists/	Get user's reading lists
DELETE	/api/reading-list/reading-lists/{readingListId}/	Delete a reading list

Example Create Reading List Request:
{
  "title": "My List",
  "description": "My favorite books"
}


📥 Reading List Items
Method	Endpoint	Description
POST	/api/reading-list/reading-lists/{readingListId}/add-book/	Add book to reading list
DELETE	/api/reading-list/reading-lists/{readingListId}/remove-book/{readingListItemId}/	Remove book from reading list
PATCH	/api/reading-list/reading-lists/{readingListId}/rearrange-items/	Reorder items in a reading list

Example To Add Book to Reading List Request:
{
  "book": {bookId}
}

Example For Rearranging Reading List Items Request:
{
  "items": [
    {"id": {readingListItem1Id}, "order": 1},
    {"id": {readingListItem2Id}, "order": 2}
  ]
}


📁 Folder Structure

readhub/
├── base/
├── books/
├── readhub/
├── readinglists/
├── users/
├── manage.py
├── .env
├── .gitignore
├── pytest.ini
├── requirements.txt
README.md

🙌 Contributions
Feel free to fork and contribute! Pull requests are welcome.

📬 Contact
For any queries, reach me at: sidharthchirathazha@gmail.com





