import sys
from anthropic import Anthropic
import base64
import os.path

# Function to get the base64 encoded image for Request
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base_64_encoded_data = base64.b64encode(binary_data)
        base64_string = base_64_encoded_data.decode('utf-8')
        return base64_string
# Check if the correct number of arguments are passed
if len(sys.argv) < 5 or len(sys.argv) > 6:
    print("Usage: python script.py <API_KEY> <MODEL_NAME_INDEX> <IMAGE_PATH> <USER_PROMPT> [MAX_TOKENS]")
    sys.exit(1)
API_KEY = sys.argv[1]
MODEL_NAMES = ["claude-3-opus-20240229", "claude-3-haiku-20240307", "claude-3-sonnet-20240229"]
MODEL_NAME_INDEX = int(sys.argv[2])
if MODEL_NAME_INDEX < 0 or MODEL_NAME_INDEX >= len(MODEL_NAMES):
    print("Invalid MODEL_NAME index. Use 0 for Opus, 1 for Haiku, and 2 for Sonnet.")
    sys.exit(1)
MODEL_NAME = MODEL_NAMES[MODEL_NAME_INDEX]
IMAGE_PATH = sys.argv[3]
USER_PROMPT = sys.argv[4]
MAX_TOKENS = int(sys.argv[5]) if len(sys.argv) == 6 else 2048  # Default value is 2048
# Extract file extension from the image path
IP = str(IMAGE_PATH)
media_type = IP.split('.')[-1]
media_type = f"image/{media_type}"
# Set the API key
os.environ["ANTHROPIC_API_KEY"] = API_KEY

client = Anthropic()
message_list = [
    {
        "role": 'user',
        "content": [
            {"type": "image", "source": {"type": "base64", "media_type":media_type, "data": get_base64_encoded_image(IMAGE_PATH)}},
            {"type": "text", "text": USER_PROMPT}
        ]
    }
]

response = client.messages.create(
    model=MODEL_NAME,
    max_tokens=MAX_TOKENS,
    messages=message_list
)
print(response.content[0].text)
