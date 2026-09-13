# 🧠 Dementia Care Chatbot

An AI-powered, emotion-aware conversational assistant designed to provide personalized and supportive interactions for people with dementia.

The chatbot maintains daily conversation history, detects the user's emotional state, and generates context-aware responses based on both the current conversation and previous interactions.

## 🌟 Features

* 🤖 **AI-Powered Chatbot**
  Provides natural and supportive conversational responses.

* ❤️ **Emotion-Aware Responses**
  Detects emotional states such as sadness, loneliness, and neutral emotions and adapts responses accordingly.

* 💬 **Conversation Memory**
  Stores daily conversations so that relevant conversational context can be maintained across interactions.

* 📅 **Daily Conversation Summarization**
  Generates a daily summary containing interaction counts, emotional patterns, and important emotional moments.

* 🧠 **Context-Aware Responses**
  Uses previous conversations and detected emotions to provide more personalized responses.

* 👵 **Dementia-Care Focused**
  Designed to provide companionship and conversational support in a simple and accessible way.

* 🧩 **Modular Architecture**
  The system separates emotion detection, memory management, response generation, summarization, and chatbot control into individual modules.

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │      User Input      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Emotion Detector   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Memory Module      │
                    │ Daily Conversation   │
                    │      History         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Prompt Builder     │
                    │ Context + Emotion +  │
                    │ Conversation History │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Model Handler     │
                    │   AI Response Model  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Response Controller  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Chatbot Response  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Daily Summarizer     │
                    └──────────────────────┘
```

## 📁 Project Structure

```text
dementia_care/
│
├── app.py
├── emotion_detector.py
├── memory_module.py
├── model_handler.py
├── prompt_builder.py
├── response_controller.py
├── summarizer.py
├── requirements.txt
├── .gitignore
│
└── data/
    └── Conversation and daily memory data
```

### Module Description

| File                     | Purpose                                                 |
| ------------------------ | ------------------------------------------------------- |
| `app.py`                 | Main application and chatbot interface                  |
| `emotion_detector.py`    | Detects the emotional state from user messages          |
| `memory_module.py`       | Stores and retrieves conversation history               |
| `model_handler.py`       | Handles interaction with the AI model                   |
| `prompt_builder.py`      | Builds context-aware prompts                            |
| `response_controller.py` | Controls and manages chatbot responses                  |
| `summarizer.py`          | Generates daily conversation and emotion summaries      |
| `requirements.txt`       | Python dependencies                                     |
| `.gitignore`             | Prevents unnecessary/private files from being committed |

## 🔄 How It Works

The chatbot follows a multi-stage conversational process:

### 1. User Interaction

The user enters a message through the chatbot interface.

### 2. Emotion Detection

The message is analyzed to identify the user's emotional state.

For example:

```text
User:
"I am feeling lonely."

Detected emotion:
lonely
```

### 3. Conversation Memory

The interaction is stored with information such as:

* Timestamp
* User message
* Chatbot response
* Detected emotion

This allows the system to maintain a history of daily conversations.

### 4. Context Construction

The system combines:

```text
Current User Message
        +
Detected Emotion
        +
Previous Conversation Context
```

to create a more personalized prompt.

### 5. AI Response Generation

The AI model generates a response based on the user's message, emotional state, and available conversational context.

### 6. Daily Summarization

At the end of the day, the system can summarize the conversation and identify emotional patterns.

Example:

```text
Daily Summary — 2026-05-01

Total interactions: 4
Dominant emotional state: lonely

Emotion breakdown:
- neutral: 1
- lonely: 2
- sad: 1
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jency899/Dementia-care-chatbot.git
```

### 2. Navigate to the project

```bash
cd Dementia-care-chatbot
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Run the main application using:

```bash
python app.py
```

If the project uses a framework such as Streamlit, run:

```bash
streamlit run app.py
```

## 🧠 Example Interaction

```text
User:
I am feeling lonely.

Emotion:
lonely

Chatbot:
It means a lot that you shared that with me. I'm here to listen.
```

The interaction can then be stored in the conversation memory for future contextual responses.

## 🔐 Privacy Considerations

The chatbot may store conversation history and emotional information to provide personalized interactions.

For real-world deployment, conversation data should be:

* Stored securely
* Protected using appropriate access controls
* Anonymized where possible
* Encrypted when appropriate
* Collected only with appropriate user consent

**Do not use real patient or personally identifiable conversation data in a public GitHub repository.**

## ⚠️ Disclaimer

This project is intended as a research and assistive conversational system.

It is **not a replacement for professional medical care, diagnosis, or treatment**. Responses generated by an AI system should not be treated as medical advice.

For real-world dementia care deployment, the system should be evaluated with appropriate clinical, ethical, privacy, and safety considerations.

## 🚀 Future Enhancements

Potential future improvements include:

* 🔊 Voice-based interaction
* 🗣️ Speech-to-text and text-to-speech
* 👨‍👩‍👧 Caregiver dashboard
* 📊 Long-term emotional trend analysis
* 🔔 Medication and appointment reminders
* 🌐 Multilingual support
* 🧠 Improved long-term memory
* 🔒 Stronger privacy and encryption
* 📱 Mobile application
* 🚨 Safety-aware escalation for concerning conversations

## 🎯 Project Goal

The goal of **Dementia Care Chatbot** is to explore how emotion-aware artificial intelligence and conversational memory can be combined to create more personalized, supportive, and context-aware interactions for people with dementia.



