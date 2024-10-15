
# Morning Greetings Package

## Objective
The objective of this Python package is to automate the process of sending personalized "Good Morning" messages to a list of friends. 
The package breaks down the task into distinct modules, each responsible for managing contacts, generating messages, simulating sending messages, and logging histories.

---

## Features
1. **Manage contacts**: Add, remove, and get a list of friends with their contact details and preferred message time.
2. **Generate Messages**: Automatically generate personalized "Good Morning" messages for each friend.
3. **Simulate Sending Messages**: Print out the message to simulate sending it to the friend.
4. **Log Messages**: Log the sent messages with a timestamp for tracking purposes.

---

## Installation
To install the `morning_greetings` package, follow these steps:

1. Clone this repository or download the package as a zip file.
    ```bash
    git clone https://github.com/snow-sagene/morning_greetings.git
    ```
2. Navigate into the package directory:
    ```bash
    cd morning_greetings
    ```
3. Install the package using pip:
    ```bash
    pip install .
    ```

---

## How to Use
After installing the package, you can use it by simply running the main script (`main.py`). Below is an example of how to use it:

 **Run the Main Script**:
    Run the `main.py` script to automate the entire process:
    ```bash
    python main.py
    ```

---

## Error Handling
main.py has error handling in place. 
- When there is an error while executing, it will print a warning message.

---

## Logging
All actions, including message generation and sending, are logged to `message_log.txt`, which records the timestamp and contact details.

---

## Package Structure
```bash
├── morning_greetings/
│   ├── contact_manager.py  # Manage contacts
│   ├── message_generator.py # Generate personalized messages
│   ├── message_sender.py   # Simulate sending messages
│   ├── logger.py           # Log sent messages
│   ├── main.py             # Main script for automation
│   └── __init__.py         # Package initializer
│
├── setup.py                # Installation setup script
├── message_log.txt         # Log file
└── README.md               # Documentation



