Chat Bot
This is a simple chat bot implemented in Python that interacts with users by answering questions based on a predefined knowledge base. The chat bot uses fuzzy string matching to find the closest match to the user's input question and provides an appropriate response.

Features
Question Matching: Utilizes fuzzy string matching to find the best match for user input questions.
Knowledge Base: Stores questions and answers in a JSON file for easy retrieval and updating.
Interactive: Allows users to teach the chat bot new responses for questions it doesn't know.
Usage
Installation: Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/chat-bot.git
Dependencies: Ensure you have Python 3 installed on your system. Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Running the Chat Bot: Run the chat_bot.py script:

bash
Copy code
python chat_bot.py
Interaction: Start interacting with the chat bot by typing your questions. Type quit to exit.
