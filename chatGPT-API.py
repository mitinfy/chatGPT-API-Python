#chatGPT api connection
#pip install --upgrade openai
import openai
openai.api_key = 'your API key'

txt=input('Enter text:')
output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": txt}]
)

# Print out the whole output dictionary
#print(output)

# Get the output text only
print(output['choices'][0]['message']['content'])
