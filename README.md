# Claude 3 API Implementation

### Generate API Key
Anthropic API key (sign up for free [here](https://www.anthropic.com/)).
<hr>

### Steps to run API call:

1. Clone this Repository.
2. Install the Anthropic Library by `pip install anthropic` in the terminal
3. Running the Script:
   
   `cd Claude3API-images/Modules/Page/Single-Image`
   
   ```bash
   python main.py <API_KEY> <MODEL_NAME_INDEX> <IMAGE_PATH> <USER_PROMPT> [MAX_TOKENS]
   ```
   <API_KEY>: Enter yout API key (REQUIRED) <br>
   <MODEL_NAME_INDEX>: `0: Claude 3 Opus` , `1: Claude 3 Haiku` and `2: Claude 3 Sonnet` (REQUIRED) <br> 
   <IMAGE_PATH>: Input Image path (REQUIRED) <br>
   <USER_PROMPT>: User Input (REQUIRED) <br>
   [MAX_TOKENS]: Default (2048) (optional) <br>
   
   For Example:
   ```bash
   python main.py <API_KEY> 0 ../../../Images/school_notes.png "Perform an OCR on the Input Image" 2048
   ```

   ### Sample Input and Output

   Input

   <img width="288" alt="school_notes" src="https://github.com/PrathameshDalal/Claude3API-images/assets/78019189/ebcbef4f-25e1-401d-8472-d8f2dd29166a">


   ![image](https://github.com/PrathameshDalal/Claude3API-images/assets/78019189/67299e3f-2b54-45e0-b1a4-e263c7b5ca47)
   

   Output

   ![image](https://github.com/PrathameshDalal/Claude3API-images/assets/78019189/cce02b60-a275-429c-b67f-e79f166f1a42)



