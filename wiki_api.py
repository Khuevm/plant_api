from model.plant import PlantInfo
import requests

def search(keyword: str):
    # Định nghĩa đường dẫn API endpoint
    print(keyword)
    url = "https://en.wikipedia.org/w/api.php"

    # Xác định các tham số cho yêu cầu API
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": keyword
    }

    # Gửi yêu cầu API
    response = requests.get(url, params=params)
    data = response.json()

    # Trích xuất thông tin từ phản hồi API
    search_results = data["query"]["search"]

    # In kết quả tìm kiếm
    return [result["title"] for result in search_results]

def getInfo(title: str):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "pageimages|extracts",
        "exintro": True,
        "explaintext": True,
        "pithumbsize": 200
    }

    # Gửi yêu cầu API
    response = requests.get(url, params=params)
    data = response.json()

    # Trích xuất thông tin trang từ phản hồi API
    page_id = list(data["query"]["pages"].keys())[0]
    page_title = data["query"]["pages"][page_id]["title"]
    page_extract = data["query"]["pages"][page_id]["extract"]
    image_info = data['query']['pages'][page_id].get('thumbnail')

    # Extract the image information
    if image_info:
        plantInfo = PlantInfo(page_title, page_extract, image_info['source'])
    else:
        plantInfo = PlantInfo(page_title, page_extract, "")
    return plantInfo