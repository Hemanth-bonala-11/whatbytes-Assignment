# Django Project Setup

Follow these steps to set up a virtual environment, install the necessary packages, and start the Django server.

---

## Step 1: Create a Virtual Environment

First, make sure you have `virtualenv` installed. If not, install it with:

```bash
pip install virtualenv
```

Now, create a virtual environment named `myenv`:

```bash
python -m venv myenv
```

Activate the virtual environment:

- **For Windows**:
  ```bash
  .\myenv\Scripts\activate
  ```
- **For macOS/Linux**:
  ```bash
  source myenv/bin/activate
  ```

---

## Step 2: Install Required Packages

Install all the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Step 3: Migrate Tables and Run the Django Server

Create Tables in database:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver
```

Now, your server should be up and running at `http://127.0.0.1:8000`.

---

