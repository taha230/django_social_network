# Django Social Network

A REST API social network backend built with Django and Django REST Framework. Includes user registration, JWT auth, posts, comments, likes, and friendship (friend requests).

## Tech Stack

- **Django** 4.2
- **Django REST Framework**
- **djangorestframework-simplejwt** (JWT authentication)

## Project Structure

| App        | Description                                      |
|-----------|---------------------------------------------------|
| `accounts` | User registration and auth (JWT). Users are represented with **extra fields** via a `Profile` (phone, country, avatar) and optional `Device` tracking (device type, OS, model, app version). |
| `posts`   | Posts, comments, and likes                       |
| `friendship` | User list, friend requests, accept, friends list |

## API Endpoints

Base URL: `/api/` (unless noted).  
Auth: use JWT in header: `Authorization: Bearer <access_token>` where required.

---

### Authentication (`accounts`)

| Method | Endpoint            | Auth | Description                    |
|--------|---------------------|------|--------------------------------|
| POST   | `/api/register/`    | No   | Register a new user           |
| POST   | `/api/token/`       | No   | Obtain JWT access + refresh   |
| POST   | `/api/token/refresh/` | No | Refresh access token          |

---

### Posts (`posts`)

| Method | Endpoint                      | Auth | Description                          |
|--------|-------------------------------|------|--------------------------------------|
| POST   | `/api/post/`                  | No*  | Create a post                        |
| GET    | `/api/post/<post_pk>/`        | No*  | Get a single post (own post)         |
| GET    | `/api/posts-list/`            | No   | List all active posts                |
| GET    | `/api/post/<post_pk>/comments/` | Yes | List approved comments for a post    |
| POST   | `/api/post/<post_pk>/comments/` | Yes | Add a comment on a post              |
| GET    | `/api/post/<post_pk>/likes/`   | Yes | Get like count for a post            |
| POST   | `/api/post/<post_pk>/likes/`   | Yes | Like a post                          |

\* Views may use `IsAuthenticated`; check `posts/views.py` for current setup.

---

### Friendship (`friendship`)

All friendship endpoints require authentication.

| Method | Endpoint                    | Description                              |
|--------|-----------------------------|------------------------------------------|
| GET    | `/api/friendship/users-list/`   | List users (optional `?q=` for search)   |
| POST   | `/api/friendship/request/`      | Send friend request (body: `user` id)   |
| GET    | `/api/friendship/requests-list/`| List pending requests to current user   |
| POST   | `/api/friendship/accept/`       | Accept friend request (body: `user` id) |
| GET    | `/api/friendship/friends/`      | List accepted friends                   |

---

### Admin

| URL              | Description        |
|------------------|--------------------|
| `/admin/`        | Django admin site  |

## Setup

1. Clone and create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   ```

2. Install dependencies:

   ```bash
   pip install -r requirments.txt
   ```

3. Copy local settings and configure:

   ```bash
   cp social_network/local_settings.py.example social_network/local_settings.py
   ```

4. Run migrations and server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## License

Private / educational use.

## 👤 Author

**Taha Hamedani**  
📧 [taha.hamedani8@gmail.com](mailto:taha.hamedani8@gmail.com)  

