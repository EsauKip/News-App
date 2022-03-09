class Article:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,author,title,image,description,url,urlToImage,publishedAt,content):
        self.id=id
        self.author =author
        self.title = title
        self.image=image
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

# class Source:
#     '''
#     source class to define source Objects
#     '''

#     def __init__(self,id,name,description,url,publishedAt,category,country):
#         self.id =id
#         self.name = name
#         self.description = description
#         self.url = url
#         self.publishedAt = publishedAt
#         # self.image=image
#         self.category = category
#         # self.language = language
#         self.country = country

