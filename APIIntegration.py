#Import libraries
from openai import OpenAI
import matplotlib.pyplot as plt
import EmailHandling.EmailSend as ESend
import Caching.UserCache as cache
import ApiKey

ApiKey.API_KEY

# Initialize the client with Perplexity's base URL
client = OpenAI(
    api_key=ApiKey.API_KEY,
    base_url="https://api.perplexity.ai",
)



import ConsoleManagement.ConsoleInput as CI 
CI.Introduce(ESend.caching_email)
defaultUserPrompt = CI.Query()

def initialAssetHandlingAgent():
    #This is the default agent filtering what assets does the user want to know about
    initialMessages = [
        {
            "role": "system",
            "content": """
            You are a professional economical analyst using objective data and 
            facts to create insight based what the user asks you to analyse.
            Your only task is to output the assets the user is interested in separated by
            a comma. (ex: "XRP, SOXL, etc.")
            
            If the asset is not recognised or the user is not mentionning an asset, try to correct it:
            Example:
            user inputs BTS (the k-pop group)
            you just understand they meant BTC (Bitcoin)
            """,
        },
        {"role": "user", "content": defaultUserPrompt}
    ]

    #Chat completion request and output
    initialAssetsResponse = client.chat.completions.create(
        model="sonar-pro", messages=initialMessages
    )
    return initialAssetsResponse
    

answerAssetsCorrect = CI.outputAssets(initialAssetHandlingAgent().choices[0].message.content)
assetsList = []


while answerAssetsCorrect != "y":
    defaultUserPrompt = CI.restart()
    answerAssetsCorrect = CI.outputAssets(initialAssetHandlingAgent().choices[0].message.content)
if answerAssetsCorrect == "y":
    assetsList = CI.separateAssets(assetsList, initialAssetHandlingAgent().choices[0].message.content)
    ESend.numberOfGraphImagesToAttach = 0
    for asset in (assetsList):
        ESend.numberOfGraphImagesToAttach += 1
    
def imageGeneraration(index):
    #This is the image generating agent handling the generation of image graph of price of asset
    image = [
        {
            "role": "system",
            "content": f"""
            DO NOT GENERATE ANYTHING ELSE APART THE CODE:
            After your textual analysis, fetch the most 
            recent 24-hour price data for the selected asset (cryptocurrency, stock, etc.), 
            generate a matplotlib graph containing all the data you need to represent then at the last line
            you are going to export the graph as a .png, the matplotlib package is already imported as plt.
            You only generate the code for the graph nothing else, what you are outputing is getting executed.
            Do not analyse anything apart just the code for the graph. I want the output to just start with the python,
            no "```python" header, just python code without any text.
            
            Here is a good exemple of output:
            
            import matplotlib.pyplot as plt

            # Recent 24-hour data
            hours = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
            # Assuming these are example prices to illustrate the concept
            prices = [2.06, 2.08, 2.09, 2.10, 2.11, 2.10, 2.08, 2.07, 2.09, 2.12, 2.13, 2.14, 2.12, 2.09, 2.11, 2.10, 2.08, 2.07, 2.09, 2.11, 2.10, 2.08, 2.06, 2.07]

            plt.figure(figsize=(10, 6))
            plt.plot(hours, prices, marker='o')
            plt.title('XRP Price Over 24 Hours')
            plt.xlabel('Time')
            plt.ylabel('Price (USD)')
            plt.grid(True)
            plt.savefig('xrp_price_over_24_hours.png')
            
            
            Any other text is getting deleted or commented.
            Name the exported file "graph{index}.png"

            Double check your code, run it and verify if there is any errors, if there is one, redo it.
            There should be no errors.
            """,
        },
        {"role": "user", "content": assetsList[index]}
    ]
    
    #Chat completion request and output
    imageAssetsResponse = client.chat.completions.create(
    model="sonar-pro", messages=image
    )
    return imageAssetsResponse.choices[0].message.content

images = []
for index, asset in enumerate(assetsList):
    images.append(imageGeneraration(index))
    

for image in images:
# Execute the code
    try:
        exec(image)
    except Exception as e:
        print(f"Error occurred: {e}")
        print(image)


print("graphs generated!")


#This is the analysis agent providing a markdown format insight of the user's asset
messages = [
    {
        "role": "system",
        "content": """You are a professional economical analyst using objective data and 
        facts to create insight based what the user asks you to analyse. 
        Every week, you great the user and you give him a detailed breakdown 
        on the market state of the cryptocurrency, stock, etc, which the user selected. 
        You start by briefly describing the news concerning the asset then you 
        analyse the recent price movements. Do not make tables as the markdown doesn't support it
        and do not add bracket references as there will be removed (ex: [0][1])
        
        Format:
        1. News and overview
        2. Recent prices movements & performance
        3. Key takeaways / investment suggested (sell or buy?)
        4. Summary
        
        "This was your summary! Thank you so much dear user for sticking with WealthIQ services and please refer to the graphs below for detailed price movements"
        """,
    },
    {"role": "user", "content": initialAssetHandlingAgent().choices[0].message.content},
]

#Chat completion request and output
finalResponse = client.chat.completions.create(
    model="sonar-pro", messages=messages
)

print("generating analysis...")

#Replace write type with "wb" but returns an error
# with open("graph.png", "w") as image:
#    image.write(imageAssetsResponse.choices[0].message.content)

print("generating output...")

with open("Output.md", "w") as file:
    file.write(finalResponse.choices[0].message.content)

print("preparing email...")

ESend.emailSetupAndSend()



# User caching

#This is the caching agent
messages = [
    {
        "role": "system",
        "content": """You are a professional archivist compiling data from analytical
        output provided by you to a fellow investor asking your advice on stocks and assets.
        Now you are going to summarize this whole analysis in a sentence of around 10 words listing
        the assets the user is interested and if these stocks are doing well or poorly.
        
        Do not make tables as the markdown doesn't support it
        and do not add bracket references as there will be removed (ex: [0][1])
        """,
    },
    {"role": "user", "content": finalResponse.choices[0].message.content},
]

#Chat completion request and output
cachingResponse = client.chat.completions.create(
    model="sonar-pro", messages=messages
)


cache.Caching(ESend.caching_email, cachingResponse.choices[0].message.content)

