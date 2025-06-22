# User Story to Test Case Converter (Flask Web App)

A simple web app that converts user stories into structured test cases.

## How to Run

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## Input Example

```
As a user, I want to log in so that I can access my dashboard
```

## Output Example

```
Test Case:
Title: To log in
Role: user
Precondition: user is logged in (if required)
Action: To log in
Expected Result: I can access my dashboard
```