import requests


class Claude35Haiku:
    def __init__(self, content_chunk, description):
        self.api_url = "https://api.cb.imaginebetterai-server.com/completion/claude-35-haiku"
        self.api_headers = {
            "Authorization": "Bearer 1d168ad4-cecd-4a99-a56a-92700a325d04",
            "Content-Type": "application/json",
        }

        self.payload = {
            "statements": [
                {
                    "role": "user",
                    "content": f"""
                    You are tasked with extracting specific information from the following text content: {content_chunk}.
                    
                    Please follow these instructions carefully:
                    
                    1. **Extract Information:** Only extract the information that directly matches the provided description: {description}.
                    2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.
                    3. **Empty Response:** If no information matches the description, return an empty string ('').
                    4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text.
                    """,
                }
            ]
        }

    def extract(self):
        response = requests.post(self.api_url, headers=self.api_headers, json=self.payload)
        return response.content.decode()


def response(content_chunks, description):
    results = []

    for i, chunk in enumerate(content_chunks, start=1):
        ai_extractor = Claude35Haiku(chunk, description)
        extracted_text = ai_extractor.extract()

        print(f"Processing batch {i} of {len(content_chunks)}")

        results.append(extracted_text)

    return "\n".join(results)




