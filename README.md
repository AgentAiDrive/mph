# My Parent Helpers

Run using Streamlit.

## Usage

Install dependencies and start the Streamlit app:

```bash
pip install -r requirements.txt
streamlit run main.py
```

The application expects an OpenAI API key configured in
`.streamlit/secrets.toml` under the `openai_key` setting:

```toml
[secrets]
openai_key = "sk-..."
```

The **Saved Items** page now lets you browse stored profiles (saved in the `profiles` folder) and view recent chat history. Selecting a profile also loads it for use in the chat helper.


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

My Parent Helpers – Pairents (pairents.streamlit.app) – Version README
Overview
Pairents (accessible at pairents.streamlit.app) is a feature rich Streamlit application designed to create, manage and interact with AI powered parenting agents. Compared to the simpler mph 2025 version, Pairents offers a comprehensive configuration workflow where users can specify detailed persona settings, upload reference documents, choose memory persistence and customize the agent’s tone and interaction style. It also introduces dedicated pages for saved profiles, chat helpers and support, making it a robust tool for parents seeking personalized guidance.
Navigation structure
The application uses a side navigation bar with the following pages:
Page	Purpose
Home	Landing page with large vertical cards for Profiles and Chat. Each card briefly describes the action and includes a “NEW” button to start creating a profile or open the chat interface 
Create Profile	A long form used to configure a parenting agent with numerous options (see below). It is reached via the NEW button on the Profiles card or the Create Profile link in the side menu 
Chat Helper	A chat interface used to converse with a selected agent. If no profile is active, the page prompts the user to load a profile first 
Saved Items	Lists all saved agent profiles along with their configurations, tools and recent chats. Profiles can be activated for chat from this page 
Support	Provides links to the user manual, a contact email and privacy policy; credits the creators with “Created by agentadri.ve” 
Creating a profile
The Create Profile page is a comprehensive agent builder. It is displayed inside a smartphone style viewport and scrolls vertically. Major sections include:
•	Basic information – Input fields for Parent Name, Child Name and Child Age, along with an Agent Type and Agent Role selector 
•	Profile photo – Drag and drop file uploader for a profile picture 
•	Persona styles and uploads – Choose one or more parenting styles (e.g. Authoritative, Gentle, etc.), upload custom persona files and provide additional persona notes via file upload pairents.streamlit.app 
•	Memory options – Select whether the agent should retain information only for the current session or persist across sessions 
•	Reference documents & external data – Upload reference documents and toggle the ability for the agent to access external data APIs pairents.streamlit.app 
•	Prompt controls – Adjust AI generation parameters such as temperature, maximum tokens, top p, frequency penalty and presence penalty. Users can also set the desired tone (e.g. playful, formal) and toggle features like Enable Feedback and Shortcuts Format 
•	Audio & loop inputs – Upload audio files to use as voice prompts or loops. This allows for multimodal interaction experiments【327881475640886†screenshot】.
•	Chat test area – At the bottom of the form is an inline chat area where users can test the agent as they configure it. Messages can be sent using a “Send” button pairents.streamlit.app 
After filling out the fields, the user can save the agent profile. Saved profiles appear on the Saved Items page.
Chat Helper
The Chat Helper page acts as the main chat interface. It displays the name and persona picture of the active profile and provides a text input area for asking questions. If no profile is active, a message indicates that the user must load a profile first  Once a profile is activated, the chat helper leverages the customized settings (tone, memory option, external data access, etc.) to generate responses.
Saved Items
The Saved Items page consolidates all previously created profiles and their metadata. When a profile is selected from the drop down list, the following details are shown:
•	Persona Styles and Custom Notes Text.
•	Tools: a list of interactive tools associated with the agent, including Emotion Tracker, Story Generator, Role play Simulator, Schedule Builder, Simulation, Role Reversal, Story Prompting, Joint Reflections and more  These tools hint at specialized functions the agent can perform during chat sessions.
•	Memory Option (e.g. persistent or session only) and whether External Data access is enabled 
•	Generation parameters: temperature, verbosity (max tokens), tone and other prompt controls 
•	Intent shortcuts – Predefined chat intents such as Grow, Connect, Resolve, Explore, Support + Ask, Imagine, Challenge, Rehearse and Reflect  A Format Pref indicates whether the user prefers responses in list or narrative form.
•	Activate Profile button – Loads the selected profile into Chat Helper.
•	Recent Chats – Displays past conversations with this profile (empty when no chat has occurred yet) 
Support
The Support page is straightforward: it presents a set of links for help and legal information. Icons and labels lead to a User Manual, Contact Us (a mail to link), and the Privacy Policy. A footer indicates the project is “Created by agentadrive” 
How to use Pairents
1.	Navigate to Create Profile via the side menu or the “NEW” button on the Profiles card. Fill out the form with your parent/child details, upload documents and tweak the AI generation settings. Save the profile.
2.	Activate a profile: Go to Saved Items, select the profile from the drop down and click Activate Profile 
3.	Chat with your agent: Open Chat Helper. If a profile is active, ask questions and receive tailored responses. Use the pre configured intent shortcuts (e.g. Grow or Resolve) to guide the conversation.
4.	Review or modify profiles: Return to Saved Items to view tools, memories and preferences. Adjust parameters from Create Profile if needed.
5.	Get help: Visit Support for the user manual or to contact the developers 
Notes & considerations
•	Orientation – The smartphone view is rotated; you may need to scroll through a very long vertical interface to reach all form elements. Some labels appear sideways because of this design choice 
•	Experimental tools – The listed tools (e.g. Story Generator, Role play Simulator) suggest planned features; not all may be fully implemented.
•	Data storage – Profiles and chats are stored locally; clearing browser data may delete them.
•	Responsibility – As with any AI assistant, Pairents provides general guidance. For serious concerns, consult a qualified professional.

