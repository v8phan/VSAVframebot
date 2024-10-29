import requests
from bs4 import BeautifulSoup

# Function to fetch and parse HTML page, looks for href of image 
def imageparser(hitboxfield):
    try:
        #split into separate url suffixes if multiple hitbox images
        list_of_suffixes = []
        filesplit = str(hitboxfield).split(', ')
        #print(filesplit)
        for x in filesplit:
            x = x.replace(")", "")
            x = x.replace("(", "")
            x = x.replace(",", "")
            x = x.replace("'", "")
            list_of_suffixes.append(x)
        # for i in filesplit:
        #     list_of_suffixes.append(i)
        href_list = []
        for j in list_of_suffixes:
            #print(f'https://wiki.gbl.gg/w/File:{j}')
            response = requests.get(f'https://wiki.gbl.gg/w/File:{j}')
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')
                # Find all hyperlinks on the page
                links = soup.find_all('a')
                #print("\nHyperlinks on the page:")
                #print(type(hitboxfield))
                hitboxfieldstring = ''.join(map(str,list_of_suffixes[0]))
                for link in links:
                    href = link.get('href')
                    #text = link.text.strip()
                    #if 'Original' in text:
                    #print(hitboxfield)
                    # if str(hitboxfield) in text:
                    #     print('HREF: ' + str(href))
                    #     href_list.append(href)
                    if hitboxfieldstring in str(href):
                        #print('FOUND HREF: ' + href)
                        href_list.append(str(href))
                        break
                    #print(f"Text: {text}, URL: {href}")
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")
        #print('HREF LIST: ' + str(href_list))
        return(href_list)
    except Exception as e:
        print(f"An error occurred: {e}")

# URL of the webpage to parse
#url = "https://wiki.gbl.gg/w/File:Vsav-VI-5-lk.png"
#print(imageparser('Vsav-VI-5-lp-hitbox.png'))
# Call the function with the URL
