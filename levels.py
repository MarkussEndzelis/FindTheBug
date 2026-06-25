levels = [
    {
        "id": 1,
        "difficulty": "easy",
        "type": "click",
        "description": "A simple login form. Something is wrong with one of the buttons.",
        "app": "login",
        "bug_element": "login_btn",
        "bug_text": "The login button says Logout instead of Login",
        "keywords": ["logout", "button", "login"]
    },
    {
        "id": 2,
        "difficulty": "easy",
        "type": "type",
        "description": "A calculator. Try adding some numbers.",
        "app": "calculator",
        "bug_text": "The calculator shows 2+2=5",
        "keywords": ["wrong", "answer", "result", "five", "5", "math"]
    },
    {
        "id": 3,
        "difficulty": "easy",
        "type": "click",
        "description": "A signup form. Find whats wrong.",
        "app": "signup",
        "bug_element": "price_label",
        "bug_text": "The price is showing as negative",
        "keywords": ["price", "negative", "minus"]
    },
    {
        "id": 4,
        "difficulty": "medium",
        "type": "type",
        "description": "A countdown timer. Something is off.",
        "app": "timer",
        "bug_element": "total_label",
        "bug_text": "The timer counts up instead of down",
        "keywords": ["up", "counts up", "wrong direction", "increasing"]
    },
    {
        "id": 5,
        "difficulty": "medium",
        "type": "click",
        "description": "A shopping cart. Check the total.",
        "app": "cart",
        "bug_element": "total_label",
        "bug_text": "The total is calculated wrong",
        "keywords": ["total", "wrong", "price", "calculation"]
    },
    {
        "id": 6,
        "difficulty": "medium",
        "type": "type",
        "description": "A signup form. Try signing up with a short password.",
        "app": "signup2",
        "bug_element": "signup_btn",
        "bug_text": "The form accepts passwords that are only 1 character long",
        "keywords": ["password", "short", "1", "one", "character", "validation"]
    },
    {
        "id": 7,
        "difficulty": "medium",
        "type": "type",
        "description": "A progress bar. Something looks wrong.",
        "app": "progress",
        "bug_element": "progress_bar",
        "bug_text": "The progress bar goes backwards",
        "keywords": ["backwards", "reverse", "wrong", "decreasing"]
    },
    {
        "id": 8,
        "difficulty": "hard",
        "type": "type",
        "description": "A login form. Try logging in.",
        "app": "login2",
        "bug_text": "The password field shows the text instead of hiding it",
        "keywords": ["password", "visible", "shown", "hidden", "dots", "text"]
    },
    {
        "id": 9,
        "difficulty": "hard",
        "type": "click",
        "description": "A volume slider. Something is subtle.",
        "app": "volume",
        "bug_element": "volume_label",
        "bug_text": "The slider goes 0-10 but the label shows 0-100",
        "keywords": ["label", "100", "10", "wrong", "number", "display"]
    },
    {
        "id": 10,
        "difficulty": "hard",
        "type": "type",
        "description": "A dark mode toggle. Toggle it and see what happens.",
        "app": "darkmode",
        "bug_text": "Dark mode makes the screen brighter instead of darker",
        "keywords": ["bright", "brighter", "light", "wrong", "opposite"]
    },
]