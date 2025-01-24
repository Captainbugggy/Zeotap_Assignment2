import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from flask import current_app

class GeminiService:
    def __init__(self):
        genai.configure(api_key=current_app.config["API_KEY"])
        self.documentation_urls = current_app.config["DOCUMENTATION_URLS"]

    def fetch_documentation(self, platform):
        url = self.documentation_urls.get(platform.lower())
        if not url:
            return f"Sorry, I couldn't find any documentation for the platform '{platform}'. Please try another platform."

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'lxml')
            doc_text = soup.get_text()
            return (
                f"I found some documentation for '{platform}'. Here's a snippet:\n\n"
                f"{doc_text[:500]}...\n\nFor more details, visit: {url}"
            )
        except requests.exceptions.RequestException as e:
            return f"Oops! I ran into a problem fetching the documentation for '{platform}'. Error: {str(e)}"


    def generate_response(self, user_prompt="hello"):
        user_prompt = user_prompt.lower()

        for platform in self.documentation_urls.keys():
            if platform in user_prompt:
                doc_content = self.fetch_documentation(platform)
                formatted_prompt = (
            f"The user has asked a 'how-to' question about the '{platform}' platform. "
            f"Refer to the official documentation provided below to formulate a clear and actionable response.\n"
            f"1. Do not reference the documentation in the answer directly; instead, provide clear steps based on the content.\n"
            f"2. If the question is not relevant to '{platform}', try to search in this: {self.documentation_urls.get(platform.lower())}.\n"
            f"3. If still not found, then respond with the documentation URL in one line.\n\n"
            f"Documentation URL: {self.documentation_urls[platform]}\n\n"
            f"User question: {user_prompt}\n\n"
            f"Answer the following:\n"
            f"- Provide a detailed response with specific steps addressing the question.\n"
            f"- If the user requests a comparison of features or processes between Segment, mParticle, Lytics, and Zeotap:\n"
            f"  1. Use the official documentation links below to gather accurate information.\n"
            f"  2. Provide a detailed and concise comparison highlighting differences, similarities, and use cases.\n\n"
            f"Official Documentation Links:\n"
            f"Segment: {self.documentation_urls['segment']}\n"
            f"mParticle: {self.documentation_urls['mparticle']}\n"
            f"Lytics: {self.documentation_urls['lytics']}\n"
            f"Zeotap: {self.documentation_urls['zeotap']}\n\n"
            f"User Query: {user_prompt}\n\n"
            f"Please generate an easy-to-understand response formatted as:\n"
            f"1. Detailed steps or insights line by line  at end.\n"
            f"2. Comparison (if applicable) with clear points for differences and similarities.\n"
            f"3. Avoid diagrams or unnecessary visuals; keep it text-focused for clarity."
            f"4. Add @34455 at the end of each line and don't end line with fullstop   "
        )

                return self.generate_content(formatted_prompt) or doc_content

        return (
            "I can assist with questions related to Segment, mParticle, Lytics, and Zeotap. "
            "Please let me know what you need help with!"
        )

    def generate_content(self, prompt):
        try:
            model = genai.GenerativeModel("gemini-2.0-flash-exp")
            response = model.generate_content(prompt)
            if response and response.text:
                return (
                    # "Here’s what I found based on your query:\n\n"
                    f"{response.text.strip()}\n\n"
                    # "Let me know if you need further clarification or additional details!"
                )
            return "Sorry, I couldn't generate a response. Please try again."
        except Exception as e:
            return f"Oops! I ran into an issue while generating the response. Error: {str(e)}"
